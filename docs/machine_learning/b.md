<center><img src="https://i.loli.net/2020/06/08/gcwel5R3MbtTxUh.png" width="20%"></center>

## 百面机器学习 Ⅱ  模型评估

### 1.评估指标的局限性

##### 准确率的局限性

准确率是指分类正确的样本占总样本个数的比例，当不同类别的样本比例非常不均衡时，占比大的类别往往成为影响准确率的最主要因素。为了解决这个问题，可以使用更为有效的平均准确率（每个类别下的样本准确率的算术平均）作为模型评估的指标。

##### 精确率与召回率的权衡

精确率是指分类正确的正样本个数占分类器判定为正样本的样本个数的比例。召回率是指分类正确的正样本个数占真正的正样本个数的比例,Precision值和Recall值是既矛盾又统一的两个指标.

为了综合评估一个排序模型的好坏，不仅要看模型在不同Top N下的Precision@N和Recall@N，而且最好绘制出模型的P-R（Precision-Recall）曲线。只用某个点对应的精确率和召回率是不能全面地衡量模型的性能，只有通过P-R曲线的整体表现，才能够对模型进行更为全面的评估。

<img src="https://i.loli.net/2020/06/07/TZSiDyPGj4Aw2oU.png" height="300" width="300">

F1 score和ROC曲线也能综合地反映一个排序模型的性能。F1 score是精准率和召回率的调和平均值，它定义为
$$
F_1=\frac{2\times precision\times recall}{precision+recall}
$$

##### 平方根误差的“意外
$$
RMSE=\sqrt{\frac{\sum_{i=1}^n{\left( y_i-\hat{y}_i \right) ^2}}{n}}
$$

一般情况下，RMSE能够很好地反映回归模型预测值与真实值的偏离程度。但在实际问题中，如果存在个别偏离程度非常大的离群点（Outlier）时,会让RMSE指标变得很差。

针对这个问题，有什么解决方案呢？第一，认定这些离群点是“噪声点”的话，就需要在数据预处理的阶段把这些噪声点过滤掉。第二，如果不认为是“噪声点”的话，就需要进一步提高模型的预测能力，将离群点产生的机制建模进去。第三，可以找一个更合适的指标来评估该模型，比如**平均绝对百分比误差**（Mean Absolute Percent Error，MAPE）相比RMSE，MAPE相当于把每个点的误差进行了归一化，降低了个别离群点带来的绝对误差的影响。
$$
MAPE=\sum_{i=1}^n{|\frac{y_i-\hat{y}_i}{y_i}|}\times \frac{100}{n}
$$

### 2.ROC曲线

##### 什么是ROC曲线？
ROC曲线是Receiver Operating Characteristic Curve的简称，中文名为“受试者工作特征曲线”。

ROC曲线的横坐标为假阳性率（False Positive Rate，FPR）；纵坐标为真阳性率（True Positive Rate，TPR）。FPR和TPR的计算方法分别为
$$
FPR=\frac{FP}{N}
$$
$$
TPR=\frac{TP}{P}
$$
TP是P个正样本中被分类器预测为正的个数，FP是N个负样本中被分类器预测为正的个数。
##### 如何绘制ROC曲线？
ROC曲线是通过不断移动分类器的“截断点”来生成曲线上的一组关键点的.

有一种更直观地绘制ROC曲线的方法。首先，根据样本标签统计出正负样本的数量，假设正样本数量为P，负样本数量为N；接下来，把横轴的刻度间隔设置为1/N，纵轴的刻度间隔设置为1/P；再根据模型输出的预测概率对样本进行排序（从高到低）；依次遍历样本，同时从零点开始绘制ROC曲线，每遇到一个正样本就沿纵轴方向绘制一个刻度间隔的曲线，每遇到一个负样本就沿横轴方向绘制一个刻度间隔的曲线，直到遍历完所有样本，曲线最终停在（1,1）这个点，整个ROC曲线绘制完成。

<img src="https://i.loli.net/2020/06/07/VntHPA1L6R7cUmv.png" height="500" width="200">
<img src="https://i.loli.net/2020/06/07/18sOIrhmGN7QUBp.png" height="300" width="300">

##### 如何计算AUC？

AUC指的是ROC曲线下的面积大小，该值能够量化地反映基于ROC曲线衡量出的模型性能。计算AUC值只需要沿着ROC横轴做积分就可以了。

##### ROC曲线相比P-R曲线有什么特点？

当正负样本的分布发生变化时，ROC曲线的形状能够基本保持不变，而P-R曲线的形状一般会发生较剧烈的变化。这个特点让ROC曲线能够尽量降低不同测试集带来的干扰，更加客观地衡量模型本身的性能。ROC曲线的适用场景更多，但如果研究者希望更多地看到模型在特定数据集上的表现，P-R曲线则能够更直观地反映其性能。

<img src="https://i.loli.net/2020/06/07/4YXiQPpaAlDBFqf.png" height="400" width="400">

图2.3（c）和图2.3（d）则是将测试集中的负样本数量增加10倍后的曲线图。

### 3.余弦距离的应用

其实在模型训练过程中，我们也在不断地评估着样本间的距离。在机器学习问题中，通常将特征表示为向量的形式，所以在分析两个特征向量之间的相似性时，常使用余弦相似度来表示。余弦相似度的取值范围是[−1,1]。如果希望得到类似于距离的表示，将1减去余弦相似度即为余弦距离。因此，余弦距离的取值范围为[0,2]。

##### 探讨为什么在一些场景中要使用余弦相似度而不是欧氏距离？

对于两个向量A和B，其余弦相似度定义为两个向量夹角的余弦
$$
\cos \left( A,B \right) =\frac{A\cdot B}{||A||_2||B||_2}
$$
关注的是向量之间的角度关系，并不关心它们的绝对大小。当一对文本相似度的长度差距很大、但内容相近时，如果使用词频或词向量作为特征，它们在特征空间中的的欧氏距离通常很大；而如果使用余弦相似度的话，它们之间的夹角可能很小，因而相似度高。此外，在文本、图像、视频等领域，研究的对象的特征维度往往很高，余弦相似度在高维情况下依然保持“相同时为1，正交时为0，相反时为−1”的性质，而欧氏距离的数值则受维度的影响，范围不固定，并且含义也比较模糊。

在一些场景，例如Word2Vec中，其向量的模长是经过归一化的，此时欧氏距离与余弦距离有着单调的关系，即
$$
||A-B||_2=\sqrt{2\left( 1-\cos \left( A,B \right) \right)}
$$
总体来说，欧氏距离体现数值上的绝对差异，而余弦距离体现方向上的相对差异。例如，我们分析两个用户对于不同视频的偏好，用户A的观看向量为(0,1)，用户B为(1,0)；更关注相对差异，显然应当使用余弦距离，此时二者的余弦距离很大，而欧氏距离很小。而当我们分析用户活跃度，以登陆次数和平均观看时长作为特征时，此时我们更关注数值绝对差异，余弦距离会认为(1,10)、(10,100)两个用户距离很近，应当使用欧氏距离。

##### 余弦距离是否是一个严格定义的距离?

距离的定义：在一个集合中，如果每一对元素均可唯一确定一个实数，使得三条距离公理（正定性，对称性，三角不等式）成立，则该实数可称为这对元素之间的距离。

余弦距离满足正定性和对称性，但是不满足三角不等式，因此它并不是严格定义的距离。

- 正定性
<img src="https://i.loli.net/2020/06/07/HCgxiBzLGybv5Dh.png" height="200" width="300">

- 对称性
$$
dist\left( A,B \right) =\frac{||A||_2||B||_2-AB}{||A||_2||B||_2}=\frac{||B||_2||A||_2-AB}{||B||_2||A||_2}=dist\left( B,A \right)
$$

- 三角不等式
<img src="https://i.loli.net/2020/06/07/A8LBcIorPFdlwmE.png" height="300" width="350">

在机器学习领域，被俗称为距离，却不满足三条距离公理的不仅仅有余弦距离，还有KL距离（Kullback-Leibler Divergence），也叫作相对熵，它常用于计算两个分布之间的差异，但不满足对称性和三角不等式。

### 4.A/B测试的陷阱

在互联网公司中，A/B 测试是验证新模块、新功能、新产品是否有效，新算法、新模型的效果是否有提升，新设计是否受到用户欢迎，新更改是否影响用户体验的主要测试方法。在机器学习领域中，A/B 测试是验证模型最终效果的主要手段。

##### 在对模型进行过充分的离线评估之后，为什么还要进行在线A/B测试？

1.离线评估无法完全消除模型过拟合的影响，得出的离线评估结果无法完全替代线上评估结果。\
2.离线评估无法完全还原线上的工程环境。一般来讲，离线评估往往不会考虑线上环境的延迟、数据丢失、标签数据缺失等情况。因此，离线评估的结果是理想工程环境下的结果。\
3.线上系统的某些商业指标在离线评估中无法计算。离线评估一般是针对模型本身进行评估，而与模型相关的其他指标，特别是商业指标，往往无法直接获得。比如，上线了新的推荐算法，离线评估往往关注的是ROC曲线、P-R曲线等的改进，而线上评估可以全面了解该推荐算法带来的用户点击率、留存时长、PV访问量等的变化。这些都要由A/B测试来进行全面的评估。

##### 如何进行线上A/B测试？

进行A/B测试的主要手段是进行用户分桶，即将用户分成实验组和对照组，对实验组的用户施以新模型，对对照组的用户施以旧模型。在分桶的过程中，要注意样本的独立性和采样方式的无偏性，确保同一个用户每次只能分到同一个桶中，在分桶过程中所选取的user_id需要是一个随机数，这样才能保证桶中的样本是无偏的。

##### 如何划分实验组和对照组

针对系统中的“美国用户”研发了一套全新的推荐模型A，而目前正在使用的是B。下面有三种实验组和对照组的划分方法，哪种划分方法是正确的？

1.根据user_id（user_id完全随机生成）个位数的奇偶性将用户划分为实验组和对照组，对实验组施以推荐模型A，对照组施以推荐模型B；\
2.将user_id个位数为奇数且为美国用户的作为实验组，其余用户为对照组；\
3.将user_id个位数为奇数且为美国用户的作为实验组，user_id个位数为偶数的用户作为对照组。

**分析与解答**:\
都不正确。黄色为实验组，棕色为对照组\
方法1没有区分是否为美国用户，实验组和对照组的实验结果均有稀释；\
<img src="https://i.loli.net/2020/06/08/oy8jXeZY9vIhPql.png" height="150" width="150">

方法2的实验组选取无误，并将其余所有用户划分为对照组，导致对照组的结果被稀释；\
<img src="https://i.loli.net/2020/06/08/j9sX8FE3fOP7DLg.png" height="150" width="150">

方法3的对照组存在偏差。\
<img src="https://i.loli.net/2020/06/08/P4AszECSNnLmaXW.png" height="150" width="150">

正确的做法是将所有美国用户根据user_id个位数划分为试验组合对照组\
<img src="https://i.loli.net/2020/06/08/KAOGyf4gxa7BbNc.png" height="150" width="150">

### 5.模型评估的方法

##### 在模型评估过程中，有哪些主要的验证方法，它们的优缺点是什么?

- Holdout检验

Holdout 检验是最简单也是最直接的验证方法，它将原始的样本集合随机划分成训练集和验证集两部分\
Holdout 检验的缺点很明显，即在验证集上计算出来的最后评估指标与原始分组有很大关系。为了消除随机性，研究者们引入了“交叉检验”的思想。

- 交叉检验

k-fold交叉验证：首先将全部样本划分成k个大小相等的样本子集；依次遍历这k个子集，每次把当前子集作为验证集，其余所有子集作为训练集，进行模型的训练和评估；最后把k次评估指标的平均值作为最终的评估指标。在实际实验中，k经常取10。

留一验证：每次留下1个样本作为验证集，其余所有样本作为测试集。在样本总数较多的情况下，留一验证法的时间开销极大。事实上，留一验证是留p验证的特例。

留p验证是每次留下p个样本作为验证集，而从n个元素中选择p个元素有$C_n^p$种可能，因此它的时间开销更是远远高于留一验证，故而很少在实际工程中被应用。

- 自助法

不管是Holdout检验还是交叉检验，都是基于划分训练集和测试集的方法进行模型评估的。然而，当样本规模比较小时，将样本集进行划分会让训练集进一步减小，这可能会影响模型训练效果。\
对于总数为n的样本集合，进行n次有放回的随机抽样，得到大小为n的训练集。采样过程中，有的样本会被重复采样，有的样本没有被抽出过，将没有被抽出的样本作为验证集，进行模型验证。

##### 在自助法的采样过程中，对n个样本进行n次自助抽样，当n趋于无穷大时，最终有多少数据从未被选择过？

<img src="https://i.loli.net/2020/06/07/twgyImPf6ukncNR.png" height="300" width="450">

### 6.超参数调优
##### 超参数有哪些调优方法？

超参数搜索算法一般包括哪几个要素。一是目标函数，即算法需要最大化/最小化的目标；二是搜索范围，一般通过上限和下限来确定；三是算法的其他参数，如搜索步长。

- 网格搜索

网格搜索可能是最简单、应用最广泛的超参数搜索算法，它通过查找搜索范围内的所有的点来确定最优值。如果采用较大的搜索范围以及较小的步长，网格搜索有很大概率找到全局最优值。然而，这种搜索方案十分消耗计算资源和时间。在实际应用中，网格搜索法一般会先使用较广的搜索范围和较大的步长，来寻找全局最优值可能的位置；然后会逐渐缩小搜索范围和步长，来寻找更精确的最优值。这种操作方案可以降低所需的时间和计算量，但由于目标函数一般是非凸的，所以很可能会错过全局最优值。

- 随机搜索

随机搜索在搜索范围中随机选取样本点。它的理论依据是，如果样本点集足够大，那么通过随机采样也能大概率地找到全局最优值，或其近似值。随机搜索一般会比网格搜索要快一些，但是和网格搜索的快速版一样，它的结果也是没法保证的。

- 贝叶斯优化算法

网格搜索和随机搜索在测试一个新点时，会忽略前一个点的信息；而贝叶斯优化算法则充分利用了之前的信息。贝叶斯优化算法通过对目标函数形状进行学习，找到使目标函数向全局最优值提升的参数。\
具体来说，它学习目标函数形状的方法是，首先根据先验分布，假设一个搜集函数；然后，每一次使用新的采样点来测试目标函数时，利用这个信息来更新目标函数的先验分布；最后，算法测试由后验分布给出的全局最值最可能出现的位置的点。对于贝叶斯优化算法，有一个需要注意的地方，一旦找到了一个局部最优值，它会在该区域不断采样，所以很容易陷入局部最优值。为了弥补这个缺陷，贝叶斯优化算法会在探索和利用之间找到一个平衡点，“探索”就是在还未取样的区域获取采样点；而“利用”则是根据后验分布在最可能出现全局最值的区域进行采样。

### 7.过拟合与欠拟合

##### 在模型评估过程中，过拟合和欠拟合具体是指什么现象？

过拟合是指模型对于训练数据拟合呈过当的情况，反映到评估指标上，就是模型在训练集上的表现很好，但在测试集和新数据上的表现较差。欠拟合指的是模型在训练和预测时表现都不好的情况。

##### 能否说出几种降低过拟合和欠拟合风险的方法？

- 降低“过拟合”风险的方法

（1）从数据入手，获得更多的训练数据,因为更多的样本能够让模型学习到更多更有效的特征，减小噪声的影响。可以通过一定的规则来扩充训练数据。比如在图像分类的问题上，可以通过图像平移、旋转、缩放等方式扩充数据；更进一步地，可以使用生成式对抗网络来合成大量的新训练数据。\
（2）降低模型复杂度。在数据较少时，适当降低模型复杂度可以避免模型拟合过多的采样噪声。例如，在神经网络模型中减少网络层数、神经元个数等；在决策树模型中降低树的深度、进行剪枝等。\
（3）正则化方法。给模型的参数加上一定的正则约束，比如将权值的大小加入到损失函数中。以L2正则化为例：
$$
C=C_O+\frac{\lambda}{2n}\cdot \sum_i{w_{i}^{2}}
$$
（4）集成学习方法。把多个模型集成在一起，来降低单一模型的过拟合风险，如Bagging方法。

- 降低“欠拟合”风险的方法

（1）添加新特征。当特征不足或者现有特征与样本标签的相关性不强时，模型容易出现欠拟合。通过挖掘“上下文特征”“ID类特征”“组合特征”等新的特征，往往能够取得更好的效果。在深度学习潮流中，有很多模型可以帮助完成特征工程，如因子分解机、梯度提升决策树、Deep-crossing等都可以成为丰富特征的方法。\
（2）增加模型复杂度。例如，在线性模型中添加高次项，在神经网络模型中增加网络层数或神经元个数等。\
（3）减小正则化系数。