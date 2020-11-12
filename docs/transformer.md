<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 从attention到transformer到BERT，精细总结

attention机制,transformer结构与BERT模型的关系如图所示

<img src="https://i.loli.net/2020/11/12/T5UnoRDjKZhSsOv.png" width=250px>

Transformer是第一个使用全attention结构的seq2seq模型，BERT模型是使用transformer的双向encoder模型，因此，按照从内到外的顺序进行介绍和总结。

### Part Ⅱ transformer结构

Seq2seq model with "self-attention"

#### 1.结构

seq2seq模型大都是结合rnn和attention的模型，transformer模型，用全attention的结构代替了lstm。

<img src="https://i.loli.net/2020/11/12/DmFjVySAEMliRO1.png" width="250px">

#### 2.encoder

由N=6个的layer组成。每个Layer由两个sub-layer组成，分别是**multi-head self-attention mechanism**和**fully connected feed-forward network**。其中每个sub-layer都加了**residual connection**和**normalisation**，因此可以将sub-layer的输出表示为：
$$
sub\_layer\_output=LayerNorm(x+(SubLayer(x)))
$$

##### 2.1 Multi-head self-attention
通过h个不同的线性变换对Q，K，V进行投影，最后将不同的attention结果拼接起来：(类似于多核卷积，学习不同特征空间的特征)
$$
MultiHead\left( Q,K,V \right) =Concat\left( head_1,...,head_h \right) W^O \\
head_i=Attention\left( QW_{i}^{Q},KW_{i}^{K},VW_{i}^{V} \right)
$$

self-attention取Q，K，V相同。\
transformer中的attention的计算采用了**scaled dot-product**，即：
$$
Attention\left( Q,K,V \right) =soft\max \left( \frac{QK^T}{\sqrt{d_k}} \right) V
$$

<font size=2>
训练上的意义: 随着词嵌入维度dk的增大, q,k 点积后的结果也会增大, 在训练时会将softmax函数推入梯度非常小的区域, 可能出现梯度消失的现象, 造成模型收敛困难.

数学上的意义: 假设q和k的统计变量是满足标准正态分布的独立随机变量, 意味着q和k满足均值为0, 方差为1. 那么q和k的点积结果就是均值为0, 方差为$d_k$, 为了抵消这种方差被放大$d_k$倍的影响, 在计算中主动将点积缩放1/$sqrt(d_k)$, 这样点积后的结果依然满足均值为0, 方差为1.
</font>

<img src="https://i.loli.net/2020/11/12/WH3Z7XGrzIQAeq6.png" width="200px">

mask 表示掩码，它对某些值进行掩盖，使其在参数更新时不产生效果。Transformer 涉及两种 mask，分别是 **padding mask** 和 **sequence mask**。其中，padding mask 在所有的 scaled dot-product attention 里面都需要用到，而 sequence mask 只有在 decoder 的 self-attention 里面用到。

1.Padding Mask\
因为每个批次输入序列长度是不一样的也就是说，我们要对输入序列进行对齐。给在较短的序列后面填充 0。如果输入的序列太长，则截取左边的内容。具体的做法是，把这些位置的值加上一个非常大的负数(负无穷)，这样的话，经过 softmax，这些位置的概率就会接近0！

2.Sequence mask\
sequence mask 是为了使得 decoder 不能看见未来的信息。产生一个上三角矩阵，上三角的值全为0。把这个矩阵作用在每一个序列上，就可以达到我们的目的。
简单来说就是只会attention到已经generated的sentence上

对于 decoder 的 self-attention，里面使用到的 scaled dot-product attention，同时需要padding mask 和 sequence mask 作为 attn_mask，具体实现就是两个mask相加作为attn_mask。

##### 2.2 Position-wise feed-forward networks

这层主要是提供非线性变换（由两个线性变换组成，中间有一个ReLU激活函数）。
$$
FFN\left( x \right) =\max \left( 0,xW_1+b_1 \right) W_2+b_2
$$

#### 3.decoder

输入：\
encoder的输出 & 对应i-1位置decoder的输出。所以中间的attention不是self-attention，它的K，V来自encoder，Q来自上一位置decoder的输出\
因此解码不是一次把所有序列解出来的，而是像rnn一样一个一个解出来的

<img src="https://i.loli.net/2020/11/12/YeyHqhsdiEvz5UK.png" width="500px">

输出：\
对应i位置的输出词的概率分布

解码过程：\
将encoder的每一个隐藏状态设定一个权重，根据权重的不同决定decoder输出更侧重于哪一个编码状态。

#### 4.Positional Encoding

以前在RNN、CNN模型中其实都出现过Position Embedding，但在那些模型中，Position Embedding是锦上添花的辅助手段，因为RNN、CNN本身就能捕捉到位置信息。但是在这个纯Attention模型中，Position Embedding是位置信息的唯一来源，因此它是模型的核心成分之一。所以文章中提出两种Positional Encoding的方法，将encoding后的数据与embedding数据求和，加入了相对位置信息。

1.用不同频率的sine和cosine函数直接计算\
2.学习出一份positional embedding\
经过实验发现两者的结果一样，所以最后选择了第一种方法，公式如下：
$$
PE\left( pos,2i \right) =\sin \left( pos/10000^{2i/d_{model}} \right) \\
PE\left( pos,2i+1 \right) =\cos \left( pos/10000^{2i/d_{model}} \right)
$$

这里的意思是将id为pos的位置映射为一个d维的位置向量，这个向量的第i个元素的数值就是$PE(p,i)$。

Position Embedding本身是一个绝对位置的信息，但在语言中，相对位置也很重要，Google选择前述的位置向量公式的一个重要原因是：由于我们有$sin(α+β)=sinαcosβ+cosαsinβ,cos(α+β)=cosαcosβ−sinαsinβ$，这表明位置p+k的向量可以表示成位置p的向量的线性变换，这提供了表达相对位置信息的可能性。

#### 5.Add & Norm模块

Add & Norm模块接在Encoder端和Decoder端每个子模块的后面，其中Add表示残差连接，Norm表示LayerNorm，残差连接来源于论文Deep Residual Learning for Image Recognition，LayerNorm来源于论文Layer Normalization

#### 6.优点

1) 每层计算复杂度
2) 可以被并行化的计算
3) cnn需要增加卷积层数来扩大视野，rnn需要从1到n逐个进行计算，而self-attention只需要一步矩阵计算就可以，比rnn更好地解决长时依赖问题。
4) self-attention模型更可解释，attention结果的分布表明了该模型学习到了一些语法和语义信息
