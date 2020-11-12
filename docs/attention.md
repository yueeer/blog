<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 从attention到transformer到BERT，精细总结

attention机制,transformer结构与BERT模型的关系如图所示

<img src="https://i.loli.net/2020/11/12/T5UnoRDjKZhSsOv.png" width=250px>

Transformer是第一个使用全attention结构的seq2seq模型，BERT模型是使用transformer的双向encoder模型，因此，按照从内到外的顺序进行介绍和总结。
### Part Ⅰ attention机制

#### 1.历史

最早是应用于图像领域的，2014年google mind团队在RNN上使用了attention机制进行图像分类，取得了很好的性能。\
论文《Neural Machine Translation by Jointly Learning to Align and Translate》中使用attention在机器翻译任务上，第一个将attention机制应用到NLP领域中。\
2017年，google机器翻译团队发表的《Attention is all you need》中大量使用了自注意力来学习文本表示。自注意力机制开始在各种NLP任务上进行探索。

#### 2.直观理解
Attention机制的核心逻辑就是<font color="red">从关注全部到关注重点</font>。

像人类看图片的逻辑，当我们看一张图片的时候，我们并没有看清图片的全部内容，而是将注意力集中在了图片的焦点上。

<img src="https://i.loli.net/2020/11/12/7JfTBNXQLamhjzH.png" width="200px">
<img src="https://i.loli.net/2020/11/12/KiqSFmNYHru12RJ.png" width="200px">

对文本的attention：

<img src="https://i.loli.net/2020/11/12/YhdQbPqHSR8r5FZ.png" width="400px">

#### 3.与传统Encoder-Decoder 差异

传统Encoder-Decoder结构先将输入数据编码成一个上下文向量c\
得到c有多种方式，最简单的方法就是把Encoder的最后一个隐状态赋值给c，还可以对最后的隐状态做一个变换得到c，也可以对所有的隐状态做变换。\
<img src="https://i.loli.net/2020/11/12/UzpQGj6cWJxqOBt.png" width="250px">

拿到c之后，就用另一个RNN网络对其进行解码。具体做法就是将c当做之前的初始状态h0输入到Decoder中，或将c当做每一步的输入

<img src="https://i.loli.net/2020/11/12/kSTVZXWHwAELg4l.png" width="250px">
<img src="https://i.loli.net/2020/11/12/Vmiao2uxbnvZOKy.png" width="250px">

缺陷：\
1）Encoder把所有的输入序列都编码成一个统一的语义特征c再解码，因此， c中必须包含原始序列中的所有信息，它的长度就成了限制模型性能的瓶颈\
2）Decoder对每一个输入都赋予相同向量，也就是每一个元素的重要程度都是一样的。比如“我爱你”翻译成“I love you”,实际上，‘我’这个元素对target中的'I'的结果是影响最大的，其他元素的影响可以说是微乎其微。在上述模型中，这个重要程度没有被体现出来。

#### 4.attention机制原理

注意力模型就是要从序列中学习到每一个元素的重要程度，然后按重要程度将元素合并，本质上就是一个加权求和的过程。将source中的构成元素想像成一系列的（key，value）数据对构成，对于某个给定的Query，我们去计算Query和各个Key之间的相关性，得到每个key对应value的权重系数，然后对value进行加权求和，即最终的attention score。

<img src="https://i.loli.net/2020/11/12/r9yH2mtj7aM51bl.png" width="600px">

#### 5.计算流程

<img src="https://i.loli.net/2020/11/12/gCI53DwY9K6odLl.png" width="380px">

其中，求Query和Key之间相关性的方法
1)点积 \
$Similarity\left( Q,K \right) =Q\cdot K$\
2)Cosine相似性 \
$Similarity\left( Q,K \right) =Q\cdot K$\
3)MLP网络\
$Similarity\left( Q,K \right) =MLP\left( Q,K \right) $

#### 6.self-attention
在一般任务中，输入Source和输出Target内容是不一样的，比如对于英-中机器翻译来说，Source是英文句子，Target是对应的翻译出的中文句子，Attention是输入对输出的权重(我爱你对I的权重)。而Self Attention顾名思义，指的是Source内部元素之间或者Target内部元素之间发生的Attention机制。K=V=Q，例如输入一个句子，那么里面的每个词都要和该句子中的所有词进行attention计算，目的是学习句子内部的词依赖关系。

计算self attention的第一步是从Encoder输入的每个单词，创建一个Query，一个Key和一个Value。这些向量是通过词嵌入乘以我们训练过程中创建的3个训练矩阵而产生的。

<img src="https://i.loli.net/2020/11/12/tYLRrje2BiA9Zqv.png" width="550px">

<img src="https://i.loli.net/2020/11/12/XRfqtusk8lUDOba.png" width="450px">

引入Self Attention后会<font color="purple">更容易捕获句子中长距离的相互依赖的特征</font>，因为如果是RNN，对于远距离的相互依赖的特征，要经过若干时间步步骤的信息累积才能将两者联系起来，距离越远，有效捕获的可能性越小。但是Self Attention在计算过程中会直接将句子中任意两个单词的联系通过一个计算步骤直接联系起来。

#### 7.优缺点
##### 7.1优点

- 参数少

跟 CNN、RNN 相比，复杂度更小，参数也更少，对算力的要求也就更小。

- 速度快

Attention机制每一步计算不依赖于上一步的计算结果，解决了 RNN 不能并行计算的问题。

- 效果好

attention的优势之一，它可以灵活的捕捉长期和local依赖，而且是一步到位的。全局联系是因为在求相似度的时候，序列中元素与其他所有元素的相似度计算，然后加权得到了编码向量。局部联系可以这么解释，因为它所计算出的attention value是属于当前输入的。

RNN长距离的信息会被弱化，Attention 先是进行序列的每一个元素与其他元素的对比，在这个过程中每一个元素间的距离都是一，因此它比RNNs的一步步递推得到长期依赖关系好的多。

##### 7.2缺点

attention机制不能捕捉语序顺序(就是元素的顺序)。 当然这个缺点也好搞定，添加位置信息就好了，所以就有了 transformer中position-embedding的概念。
