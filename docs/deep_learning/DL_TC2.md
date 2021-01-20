<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 综述：基于深度学习的文本分类
#### 《Deep Learning Based Text Classification: A Comprehensive Review》论文总结(二)

Minaee S, Kalchbrenner N, Cambria E, et al. Deep learning based text classification: A comprehensive review[J]. arXiv preprint arXiv:2004.03705, 2020.\
原文链接：https://arxiv.org/pdf/2004.03705.pdf

参考博主「一只羊呀」:[Deep Learning Based Text Classification: A Comprehensive Review（部分翻译总结）](https://blog.csdn.net/qq_38331611/article/details/106995742)的总结

#### 3.文本分类数据集
##### 3.1 情绪分析数据集

**Yelp**:Yelp是最流行的情感分类数据集之一。在此数据集上定义了两个分类任务。一种是检测细粒度的情感标签，称为Yelp-5。另一个预测负面和正面情绪，被称为Yelp评论极性或Yelp-2。\
**IMDb**:IMDB数据集被开发用于电影评论的二进制情感分类的任务。\
**SST**:斯坦福情感树库（SST）数据集。有两个版本可用，一个带有细粒度标签（五类），另一个带有二进制标签，称为SST-1和SST-2。\
**MPQA**:多视角问答数据集，是具有两个类别的意见语料库标签。
**Amazon**：这是从亚马逊网站收集的热门产品评论语料库。\
一些受欢迎的数据集包括SemEval-2014 Task4，Twitter，SentiHood等。

##### 3.2新闻分类数据集

**AG News**：是学术新闻搜索引擎ComeToMyHead从2000多个新闻来源收集的新闻文章的集合。 每个样本都是带有四类标签的简短文本。\
**20 Newsgroups**：是发布在20个不同主题上的新闻组文档的集合。\
**Sogou News**：是SogouCA和SogouCS新闻语料库的混合。\
**Reuters news**：是用于文本分类研究的最广泛使用的数据集之一。\
为新闻分类开发的其他数据集包括：Bing news, NYTimes, BBC, Google news。

##### 3.3主题分类数据集

**DBpedia**：是大规模的多语言知识库，它是根据Wikipedia中最常用的信息框创建的。\
**Ohsumed**：每个文档都是医学摘要，由选自23种心血管疾病类别的一个或多个类别标记。\
**EUR-Lex**：包括不同类型的文档，这些文档根据几种正交分类方案进行索引以允许使用多种搜索工具。 该数据集的最流行版本基于欧盟法律的不同方面。\
**WOS**：Web of Science（WOS）数据集是可从Web of Science获得的已发表论文的数据和元数据的集合。\
**PubMed**：PubMed是由美国国家医学图书馆开发的搜索引擎，用于医学和生物科学论文。

##### 3.4 QA Datasets

**SQuAD**：斯坦福大学问答数据集（SQuAD）是从Wikipedia文章中获得的问题-答案对的集合。\
**MS MARCO**：该数据集由Microsoft发布。与SQuAD不同的是，所有问题都是由编辑产生的；在MS MARCO中，使用Bing搜索引擎从用户查询和真实Web文档的段落中抽取所有问题。\
**TREC-QA**：是用于QA研究的最受欢迎和研究最多的数据集之一。该数据集具有两个版本，称为TREC-6和TREC-50。TREC-6由6个类别的问题组成，而TREC-50由五十个类别的问题组成。\
**WikiQA**：由一组问题-答案对组成，它们被收集并注释以用于开放域QA研究。数据集还包含没有正确答案的问题，使研究人员可以评估答案触发模型。\
**Quora**：包含超过40万个问题对。为每个问题对分配一个二进制值，指示两个问题是否相同。\
其他数据集包括Adversarial Generations (SWAG), WikiQA, SelQA。

##### 3.5 NLI数据集

**SNLI**：斯坦福自然语言推断数据集被广泛用于NLI。该数据集包含550,1句子对，每对带有三个标签之一：neutral, entailment, contradiction。\
**Multi-NLI**：SNLI的扩展，涵盖更广泛的口语和书面语体裁，并支持独特的跨体裁归纳评估。\
**SICK**：英语句子对，并用三个标签进行注释：entailment, contradiction, and neutral。\
**MSRP**：通常用于文本相似性任务。每个样本都是一个句子对，并用二进制标签注释，指示两个句子是否为释义。\
其他NLI数据集还包括Semantic Textual Similarity (STS), RTE, SciTail。

#### 4.实验性能分析
##### 4.1 常用的文本分类指标
###### Accuracy and Error Rate
$$
Accuracy=\frac{\left( TP+TN \right)}{N},Error\ rate=\frac{\left( FP+FN \right)}{N}
$$
$$
Error\ rate=1-Accuracy
$$

TP,FP、TN、FN分别表示真阳性、假阳性、真阴性、假阴性
###### Precision / Recall / F1 score
对于不平衡的测试集，它们比准确性或错误率更常用，F1分数是精确度和召回率的调和平均值。F1得分的最佳值为1(完美的精度和召回)，最差值为0。例如，大多数测试样本都有一个类标签。二分类的准确率和召回率定义为
$$
Precision=\frac{TP}{TP+FP},\text{Re}call=\frac{TP}{TP+FN}\text{，}F1-score=\frac{2Pre\cdot \text{Re}c}{Pre+\text{Re}c}
$$
对于多类分类问题，我们总是可以计算每个类标签的准确率和召回率，并分析个体在类标签上的表现，或者将值取平均值，得到整体的准确率和召回率。
##### Exact Match (EM)
精确匹配指标是问答系统的一个流行指标，它衡量的是准确匹配任何一个ground truth answer的预测百分比。
##### Mean Reciprocal Rank (MRR)平均倒数排名
MRR常被用于评估NLP任务中排序算法的性能，如查询文档排序和QA。其中Q是所有可能答案的集合，$rank_i$是真实答案的排名位置。
$$
MRR=\frac{1}{|Q|}\sum_{i=1}^Q{\frac{1}{rank_i}}
$$
其他广泛使用的指标包括**Mean Average Precision** (MAP)平均精度(MAP)、**Area Under Curve**(AUC)曲线下面积、**False Discovery Rate**错误发现率，**False Omission Rate**误漏率等等

#### 5.挑战和机遇

- 为更具有挑战性的任务构建新的数据集

尽管近年来已经收集了大量的大型数据集用于常见的文本分类任务，但仍然需要新的数据集来完成更具挑战性的任务，如多步骤推理的QA和多语言文档的文本分类。为这些任务提供大规模的标记数据集有助于加速这些领域的进展。

- 建立常识知识模型

将常识性知识融入深度学习模型有可能显著提高模型性能，这与人类利用常识性知识执行不同任务的方式几乎相同。例如，一个配备常识知识库的QA系统可以回答关于真实世界的问题。常识知识也有助于在信息不完整的情况下解决问题。人工智能系统利用人们对日常事物或概念的普遍信念，以类似的方式，基于对未知事物的“默认”假设进行推理。虽然这种思想已经被研究用于情感分类，但如何在神经模型中有效地建模和使用常识知识还需要更多的研究。

- 可解释的深度学习模型

尽管深度学习模型在具有挑战性的基准测试中取得了令人满意的性能，但大多数模型都是不可解释的，并且仍然存在许多悬而未决的问题。例如，为什么一个模型在一个数据集上优于另一个模型，但在其他数据集上却表现不佳？深度学习模式到底学到了什么？什么是最小的神经网络结构，能够在给定的数据集上达到一定的精度？尽管注意和自我注意机制为回答这些问题提供了一些见解，但对这些模型的潜在行为和动力学的详细研究仍然缺乏。更好地理解这些模型的理论方面有助于开发针对各种文本分析场景的更好的模型。

- 内存效率模型

大多数现代神经语言模型需要大量的记忆来训练和推理。但是，为了满足移动设备的计算和存储限制，这些模型必须进行简化和压缩。这可以通过使用知识蒸馏来构建学生模型，或者使用模型压缩技术来实现。开发与任务无关的模型简化方法是一个活跃的研究课题。

- 少样本和零样本学习

大多数深度学习模型都是有监督的模型，需要大量的领域标签。实际上，为每个新域收集这样的标签是昂贵的。微调一个针对特定任务的预训练语言模型（PLM）如BERT和OpenGPT比从头开始训练一个模型需要更少的领域标签，从而为开发基于PLM的新的少样本和零样本学习方法提供了机会。
