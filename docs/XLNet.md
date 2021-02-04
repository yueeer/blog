<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## BERT改进版？更强的NLP模型
#### XLNet原理介绍

参考知乎「张俊林」:[XLNet:运行机制及和Bert的异同比较](https://zhuanlan.zhihu.com/p/70257427)
参考博主「爱编程真是太好了」:[最通俗易懂的XLNET详解](https://blog.csdn.net/u012526436/article/details/93196139)

#### 怎么想的

一句话总结：XLNet引入了自回归语言模型以及自编码语言模型
- 自回归语言模型（Autoregressive LM）

根据上文内容预测下一个可能跟随的单词。比如GPT、ELMO。\
<font color="darkblue">缺点是只能利用上文或者下文的信息，不能同时利用上文和下文的信息。</font>\
<font color="purple">优点其实跟下游NLP任务有关，比如生成类NLP任务，比如文本摘要，机器翻译等，在实际生成内容的时候，就是从左向右的，自回归语言模型天然匹配这个过程。而Bert这种在生成类NLP任务中，就面临训练过程和应用过程不一致的问题，导致生成类的NLP任务到目前为止都做不太好。</font>
- 自编码语言模型（Autoencoder LM）

Bert在输入X中随机Mask掉一部分单词，然后预训练过程的主要任务之一是根据上下文单词来预测这些被Mask掉的单词，这是典型的Denoising Autoencoder(去噪自动编码器，DAE)的思路。那些被Mask掉的单词就是在输入侧加入的所谓噪音。\
<font color="darkblue">缺点主要在输入侧引入`[Mask]`标记，导致预训练阶段和Fine-tuning阶段不一致的问题。</font>\
<font color="purple">优点是它能比较自然地融入双向语言模型，同时看到被预测单词的上文和下文。</font>

XLNet的出发点就是：能否融合自回归LM和DAE LM两者的优点。就是说如果站在自回归LM的角度，如何引入和双向语言模型等价的效果；如果站在DAE LM的角度看，如何抛掉表面的那个`[Mask]`标记，让预训练和Fine-tuning保持一致。另外，Bert在预训练阶段假设句子中多个单词被Mask掉，这些被Mask掉的单词之间没有任何关系，是条件独立的，而有时候这些单词之间是有关系的，XLNet则考虑了这种关系。

XLNet仍然遵循两阶段的过程，第一个阶段是语言模型预训练阶段；第二阶段是任务数据Fine-tuning阶段。它主要希望改动第一个阶段，就是说不像Bert那种带`[Mask]`的DAE的模式，而是采用自回归LM的模式。就是说，看上去输入句子X仍然是自左向右的输入，看到单词的上文Context_before，来预测这个单词。但是又希望在Context_before里，不仅仅看到上文单词，也能看到单词后面的下文Context_after里的下文单词，这样的话，Bert里面预训练阶段引入的Mask符号就不需要了，于是在预训练阶段，看上去是个标准的从左向右过程，Fine-tuning当然也是这个过程，于是两个环节就统一起来。

#### 怎么做的

XLNet是这么做的，在预训练阶段，引入<font color="red">Permutation Language Model</font>（排列语言模型）的训练目标。就是说，比如包含单词Ti的当前输入的句子X，由x1,x2,x3,x4四个单词顺序构成。我们假设要预测的单词Ti是x3，位置在Position 3，假设我们固定住x3所在位置，之后随机排列组合句子中的4个单词，在随机排列组合后的各种可能里，再选择一部分作为模型预训练的输入X。比如抽取出x4,x2,x3,x1这一个排列组合作为模型的输入X。于是，x3就能同时看到上文x2，以及下文x4的内容了。这就是XLNet的基本思想，通过对句子中单词排列组合，把一部分Ti下文的单词排到Ti的上文位置中，于是，就看到了上文和下文，但是形式上看上去仍然是从左到右在预测后一个单词。

<img src="https://i.loli.net/2021/02/04/TRPVdHkby6S7M1U.png" height="320" width="450">

具体怎么做才能实现上述思想。首先，需要强调一点，尽管上面讲的是把句子X的单词排列组合后，再随机抽取例子作为输入，但是，实际上你是不能这么做的，因为Fine-tuning阶段你不可能也去排列组合原始输入。所以，就必须让预训练阶段的输入部分，看上去仍然是x1,x2,x3,x4这个输入顺序，但是可以在Transformer部分做些工作，来达成我们希望的目标。具体而言，XLNet采取了<font color="red">Attention Mask</font>的机制，你可以理解为，当前的输入句子是X，要预测的单词Ti是第i个单词，前面1到i-1个单词，在输入部分观察，并没发生变化，该是谁还是谁。但是在Transformer内部，通过Attention掩码，从X的输入单词里面，也就是Ti的上文和下文单词中，随机选择i-1个，放到Ti的上文位置中，把其它单词的输入通过Attention掩码隐藏掉，于是就能够达成我们期望的目标（当然这个所谓放到Ti的上文位置，只是一种形象的说法，其实在内部，就是通过Attention Mask，把其它没有被选到的单词Mask掉，不让它们在预测单词Ti的时候发生作用，如此而已。看着就类似于把这些被选中的单词放到了上文Context_before的位置了）。

具体实现的时候，普通的transformer结构是存在一定的问题的，因为无论预测目标的位置在哪里，单词组合排列后得到的所有情况都是一样的，并且transformer的权重对于不同的情况是一样的，因此无论目标位置怎么变都能得到相同的分布结果，如下图所示，假如我们的序列index表示为[1,2,3]，对于目标2与3来说，经过transformer之后得到的结果肯定也是一样的。

<img src="https://i.loli.net/2021/02/04/ELrkshDQX1Znm57.png" height="220" width="100">

目标：
- 如果目标是预测x，那么只能有其位置信息而不能包含内容信息
- 如果目标是预测其他tokens，那么应该包含内容信息这样才有完整的上下文信息。

为了解决这个问题，论文中提出来新的分布计算方法<font color="red">Two-Stream Self-Attention</font>（双流自注意力机制）

1.内容流自注意力<font color="red">content representation</font>，其实就是标准的Transformer的计算过程，同时编码上下文和自身；

<img src="https://i.loli.net/2021/02/04/XpEwvKFr9zhxZAI.png" height="160" width="280">

2.主要是引入了Query流自注意力<font color="red">query representation</font>，这个其实就是用来代替Bert的`[Mask]`标记的。该表述representation包含上下文的内容信息和目标的位置信息，但是不包括目标的内容信息。从图中可以看到，K与V的计算并没有包括Q，自然也就无法获取到目标的内容信息，但是目标的位置信息在计算Q的时候保留了下来

<img src="https://i.loli.net/2021/02/04/X6iSchCEYrLlRNt.png" height="160" width="280">

总的计算过程，首先，第一层的查询流是随机初始化了一个向量w，内容流是采用的词向量即$e^{x_i}$，self-attention的计算过程中两个流的网络权重是共享的，最后在微调阶段，只需要简单的把query stream移除，只采用content stream即可。

<img src="https://i.loli.net/2021/02/04/LtqmJ1dVzincWZP.png" height="360" width="480">

比如说序号依次为 1234 的句子，先随机取一种排列 3241。根据这个排列我们就做出类似上图的 Attention Mask，先看第 1 行，因为在新的排列方式中 1 在最后一个，根据从左到右 AR 方式，1 就能看到 234 全部，于是第一行的 234 位置是红色的（没有遮盖掉，会用到），以此类推，第 2 行，因为 2 在新排列是第二个，只能看到 3 于是 3 位置是红色，第 3 行，因为 3 在第一个，看不到其他位置，所以全部遮盖掉...

#### Transformer-XL

XLNet 借鉴了 Transformer-XL 的优点，它对于很长的上下文的处理是要优于传统的 Transformer 的

##### 片段循环机制Segment Recurrence Mechanism
对于普通的transformer由于有一个最长序列的超参数控制其长度，对于特别长的序列就会导致丢失一些信息。假设我们有一个长度为1000的序列，如果我们设置transformer的最大序列长度是100，那么这个1000长度的序列需要计算十次，并且每一次的计算都没法考虑到每一个段之间的关系，egment Recurrence Mechanism想做的就是，能不能在前一段计算完后，将它计算出的隐状态都保存下来，存到一个 Memeory 中，之后在计算当前段的时候，将之前存下来的隐状态和当前段的隐状态拼起来，作为 Attention 机制的 K 和 V，从而获得更长的上下文信息。该机制不但能保留长依赖关系还能加快训练，因为每一个前置片段都保留了下来，不需要再重新计算。在XLNet中引入片段循环机制其实也很简单，只需要在计算KV的时候做简单的修改。

<img src="https://i.loli.net/2021/02/04/fQcpBoH5PeD1UhF.png" height="180" width="300">

##### Relative Positional Encoding
在 Transformer 中，一个重要的地方在于其考虑了序列的位置信息。在分段的情况下，如果仅仅对于每个段仍直接使用 Transformer 中的位置编码，即每个不同段在同一个位置上的表示使用相同的位置编码，就会出现问题。比如，第i-2段和第i-1段的第一个位置将具有相同的位置编码，但它们对第i段的建模重要性显然并不相同。因此 Transformer-XL 提出了一种相对位置编码，不再关心句中词的绝对位置信息，而是相对的，比如说两个词之间隔了多少个词这样的相对信息

#### 总结

XLNet起作用的三个因素；
1. 与Bert采取方式不同的新的预训练目标：Permutation Language Model；这个可以理解为在自回归LM模式下，如何采取具体手段，来融入双向语言模型。这个是XLNet在模型角度比较大的贡献。
2. 引入了Transformer-XL的主要思路：相对位置编码以及分段RNN机制。实践已经证明这两点对于长文档任务是很有帮助的；
3. 加大增加了预训练阶段使用的数据规模；Bert使用的预训练数据大小13G。XLNet除了使用这些数据外，另外引入了Giga5，ClueWeb以及Common Crawl数据，并排掉了其中的一些低质量数据，大小分别是16G,19G和78G。在预训练阶段极大扩充了数据规模，并对质量进行了筛选过滤。这个明显走的是GPT2.0的路线。

对NLP应用任务的影响\
对比XLNet和BERT，对于生成类型的NLP任务（文本摘要，机器翻译等），XLNet应该会比Bert有明显优势。另外，因为XLNet还引入了Transformer XL的机制，所以对于长文档输入类型的NLP任务，也会有明显优势。
