<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 从attention到transformer到BERT，精细总结

attention机制,transformer结构与BERT模型的关系如图所示

<img src="https://i.loli.net/2020/11/12/T5UnoRDjKZhSsOv.png" width=250px>

Transformer是第一个使用全attention结构的seq2seq模型，BERT模型是使用transformer的双向encoder模型，因此，按照从内到外的顺序进行介绍和总结。

### Part Ⅲ BERT模型

Transformer其实是个完整地seq-to-seq模型，使用Encoder做特征提取器，然后用Decoder做解析，可以解决输入输出为不定长句子的任务。\
BERT,全称**B**idirectional **E**ncoder **R**epresentation from **T**ransformers,作为一个预训练模型，只使用了Transformer的Encoder作特征提取器。

#### 1.结构

<img src="http://s58.99854.men/2020/11/12/86345d123c1a86e09a959cf111a85903.png" width=550px>

对比OpenAI GPT(Generative pre-trained transformer)，BERT是双向的Transformer block连接；就像单向rnn和双向rnn的区别，直觉上来讲效果会好一些。\
对比ELMo，虽然都是“双向”，但目标函数其实是不同的。ELMo独立训练处两个representation然后拼接。

#### 2.输入

<img src="http://s59.99854.men/2020/11/12/6f1e27f330d45e2392aa804c413fad47.png" width=550px>

Token Embeddings是词向量\
Segment Embeddings用来区别两种句子，因为预训练要做以两个句子为输入的分类任务\
Position Embeddings是学习出来的\

#### 3.Pre-training
##### Task 1#: Masked Language Model(MLM)
在训练过程中作者随机mask 15%的token，最终的损失函数只计算被mask掉那个token。

在训练模型时，一个句子会被多次喂到模型中用于参数学习，但是Google并没有在每次都mask掉这些单词，而是在确定要Mask掉的单词之后，80%的时候会直接替换为[Mask]，10%的时候将其替换为其它任意单词，10%的时候会保留原始Token。

- 80%：my dog is hairy -> my dog is [mask]
- 10%：my dog is hairy -> my dog is apple
- 10%：my dog is hairy -> my dog is hairy

这么做的原因是如果句子中的某个Token100%都会被mask掉，那么在fine-tuning的时候模型就会有一些没有见过的单词。加入随机Token的原因是因为Transformer要保持对每个输入token的分布式表征，否则模型就会记住这个[mask]是token ’hairy‘。至于单词带来的负面影响，因为一个单词被随机替换掉的概率只有15%*10% =1.5%，这个负面影响其实是可以忽略不计的。\
另外文章指出每次只预测15%的单词，因此模型收敛的比较慢。

##### Task 2#: Next Sentence Prediction(NSP)

训练的输入是句子A和B，B有50%几率是A的下一句，输入AB，模型预测B是不是A的下一句。让模型理解两个句子之间的联系。

#### 3.损失函数

BERT的损失函数由两部分组成，第一部分是来自 MLM ，另一部分是NSP。
$$
L\left( \theta ,\theta _1,\theta _2 \right) =L_1\left( \theta ,\theta _1 \right) +L_2\left( \theta ,\theta _2 \right)
$$

其中 θ 是 BERT 中 Encoder 部分的参数，θ1​ 是 MLM中在 Encoder 上所接的输出层中的参数，θ2​ 则是NSP中在 Encoder 接上的分类器参数。因此，在第一部分的损失函数中，如果被 mask 的词集合为 M，因为它是一个词典大小 |V| 上的多分类问题，那么具体说来有：
$$
L_1\left( \theta ,\theta _1 \right) =-\sum_{i=1}^M{\log\text{\ }p\left( m=m_i|\theta ,\theta _1 \right) ,m_i\in \left[ 1,2,...,|V| \right]}
$$

在句子预测任务中，也是一个分类问题的损失函数：
$$
L_2\left( \theta ,\theta _2 \right) =-\sum_{i=1}^N{\log\text{\ }p\left( n=n_i|\theta ,\theta _2 \right) ,n_i\in \left[ IsNext,NotNext \right]}
$$

因此，两个任务联合学习的损失函数是：
$$
L\left( \theta ,\theta _1,\theta _2 \right) =-\sum_{i=1}^M{\log\text{\ }p\left( m=m_i|\theta ,\theta _1 \right)-\sum_{i=1}^N{\log\text{\ }p\left( n=n_i|\theta ,\theta _2 \right) }}
$$

BERT 还利用了一系列策略，使得模型更易于训练，比如对于学习率的 warm-up 策略，使用的激活函数不再是普通的 ReLu，而是 GeLu，也使用了 dropout 等常见的训练技巧。

#### 4.BERT适用场景

1) NLP任务偏向在语言本身中就包含答案，而不特别依赖文本外的其它特征。典型的任务比如QA和阅读理解，正确答案更偏向对语言的理解程度，理解能力越强，解决得越好。

2) Bert特别适合解决句子或者段落的匹配类任务。就是说，Bert特别适合用来解决判断句子关系类问题。

从上面这个Bert的擅长处理句间关系类任务的特性，我们可以继续推理出以下观点：
既然预训练阶段增加了Next Sentence Prediction任务，就能对下游类似性质任务有较好促进作用，那么是否可以继续在预训练阶段加入其它的新的辅助任务？而这个辅助任务如果具备一定通用性，可能会对一类的下游任务效果有直接促进作用。

3) 越是需要深层语义特征的任务，越适合利用Bert来解决，典型的浅层特征性任务比如分词，POS词性标注，NER，文本分类等任务，只需要较短的上下文，以及浅层的非语义的特征，貌似就可以较好地解决问题。

4) Bert比较适合解决输入长度不太长的NLP任务。
主要原因在于：Transformer的self attention机制因为要对任意两个单词做attention计算，所以时间复杂度是n平方，n是输入的长度。结论是：Bert更适合解决句子级别或者段落级别的NLP任务。
