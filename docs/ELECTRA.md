<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 更有效率的模型:ELECTRA

参考知乎「sergio」:[ELECTRA 详解](https://zhuanlan.zhihu.com/p/118135466)
参考知乎话题「如何评价NLP算法ELECTRA的表现？」

#### 概述

ELECTRA全称pre-training text encoders as discriminators rather than generators。通过类似GAN的结构和新的预训练任务，在更少的参数量和数据下，不仅吊打BERT，而且仅用1/4的算力就达到了当时SOTA模型RoBERTa的效果。ELECTRA在多分类上不如RoBERTa，可能与预训练时采用的是二分类任务有关。

#### 原理

BERT的缺陷：
- BERT中MLM的实现，并不是非常高效的，只有15%的tokens对参数的更新有用，其他的85%是不参与gradients的update的
- 存在预训练和fine-tuning的mismatch，在fine-tuning阶段，并不会有`[MASK]`的token。

ELECTRA使用了新的预训练task：<font color="red">replaced token detection</font>

1.masked(replaced) tokens的选择

BERT是随机的，比如句子“我想吃苹果”，BERT可以mask为“我想吃苹[MASK]”，这样一来实际上去学它就很简单，如果mask为“我[MASK]吃苹果”，那么去学这个“想”就相对困难了。换句话说，BERT的mask可能会有很多简单的token，去学这些token就算是简单的bilstm都可以做的。这样一来，一个简单的想法就是，不随机mask，去专门选那些对模型来说学习困难的token。\
怎么做呢？train一个简单的MLM，当做模型对训练难度的先验，简单的自动过滤（在这里就是sample出来的和原句子一样）。MLM的作用就是为自动选择masked tokens提供了一种非常有效的方法。

2.training objective

既然MLM选择了一些token，那么该怎么去学呢？当然这个地方也可以像BERT那样，如果MLM采样的保持不变，就相当于原BERT中不mask；如果变了，就mask，然后再用BERT的方法去train。然而ELECTRA另辟蹊径，用一个二分类去判断每个token是否已经被换过了。这就把一生成式的MLM预训练任务改成了判别式的RTD任务。

#### 模型结构
<img src="https://i.loli.net/2021/02/04/nzAO4pc7BbDMIWQ.png" height="120" width="470">

模型由generator以及discriminator构成，两个都是transformer的encoder结构，两者的size不同：
- generator：一个小的 MLM（通常是 1/4 的discriminator的size），generator的目标函数和bert一样，希望被masked的能够被还原成原本的original tokens：
  - 首先随机选取15%的tokens，替代为[MASK]token
  - 使用generator去训练模型，使得模型预测masked token，得到corrupted tokens
- discriminator：接收corrupted tokens，分辨输入的每一个token是original（与原始token一致）的还是replaced（与原始token不一致）
  - 对于每个token，discriminator都会进行一个二分类，最后获得loss

与GAN的区别：
<img src="https://i.loli.net/2021/02/04/cf6rWxuwKdIbpqD.png" height="160" width="600">

#### 模型优点
（1）每个token都能contribute to some extent；
（2）缓解distribution的问题。如果像BERT那样去预测真正的token，也即通过一个classifier的话，那么它相比二分类器而言就需要更多的计算量，而且还要suffer 由于|V|较大导致的分布问题。

<img src="https://i.loli.net/2021/02/04/JKZc8yT9ORlSkd7.png" height="70" width="350">

#### 模型训练
上述结构有个问题，输入句子经过生成器，输出改写过的句子，因为句子的字词是离散的，所以梯度在这里就断了，判别器的梯度无法传给生成器，于是生成器的训练目标还是MLM，判别器的目标是序列标注（判断每个token是真是假），两者同时训练，目标函数如下：
$$
\min_{\theta _G,\theta _D}\sum_{x\in \mathcal{X}}{\mathcal{L}_{MLM}}\left( x,\theta _G \right) +\lambda \mathcal{L}_{\text{Disc\,\,}}\left( x,\theta _D \right)
$$
因为判别器的任务相对来说容易些，RTD loss相对MLM loss会很小，因此加上一个系数，作者训练时使用了50。

#### 总结
1.提出了新的模型预训练的框架，采用generator和discriminator的结合方式，但又不同于GAN
将Masked Language Model的方式改为了replaced token detection
2.因为masked language model 能有效地学习到context的信息，所以能很好地学习embedding，所以使用了weight sharing的方式将generator的embedding的信息共享给discriminator
3.该模型采用了小的generator以及discriminator共同训练，两者loss相加，使得discriminator的学习难度逐渐地提升，学习到更难的token（plausible tokens）
4.模型在fine-tuning 的时候，丢弃generator，只使用discrinator
