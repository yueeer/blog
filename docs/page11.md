<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 深度学习的主要流程

#### 1. 数据的收集和预处理

要考虑：原始数据raw data，metadata，写入内存的方法，变成数据矩阵的shape，如何进行预处理，耗费的时间等等

(1)数据清洗：检测和去除数据集中的噪声数据和无关数据，处理遗漏数据，去除空白数据域，非法值、不一致数据、重复记录的检测和处理

【空值数据的处理方法】\
删除：空值的数据占总体比例较低时\
自动补全方法：根据数据集中记录的取值分布情况来对空值进行自动填充\
手工补全\
【不一致数据的处理方法】\
分析不一致产生原因的基础，用各种变换函数，格式化函数去实现清洗\
【噪声数据的处理方法】\
计算机检查和人工检查相结合：可以通过计算机将被判定数据与已知的正常值比较，将差异程度大于某个阈值的模式输出到一个表中，人工审核后识别出噪声数据。\
分箱：特征离散化 可以用pandas实现\
回归：找到恰当的回归函数来平滑数据。\
聚类：将落在聚类集合之外的值被视为孤立点。孤立点可能是垃圾数据，也可能是提供信息的重要数据。

(2)数据变换

【数据泛化】\
用高层次概念替换低层次原始数据，如age,映射到较高层概念young, middle -age,old\
【数据降维】\
将数据从高维特征空间向低纬特征空间映射，如线性判别式分析法LDA、主成分分析法PCA\
【数据规范化】\
将数据按比例缩放，使之落入特定区间。如归一化(current - min)/(max - min)、标准化	(current - mean)/ var\
【特征构造】\
利用平方等方法挖掘新的属性加入属性集，用日销售数据，计算月和年销售额等

(3)拿到数据后的一般步骤：

明确有数据集有多少特征，哪些是连续的，哪些是类别的\
检查有缺失值，重复值\
对连续的数值型特征进行标准化，对类别型的特征进行编码\
根据实际分析对特征进行相应的函数转换

#### 2. 确定网络结构

输入：数据矩阵形式，shape\
输出：矩阵形式，考虑输出embdding或者经过softmax、sigmoid处理的概率值\
考虑网络的配置

#### 3. 训练，找到凸函数并且优化

训练的参数：batch_size、epoch、learning rate、weight-decay等\
训练的流程：1.凸函数构建、2. 凸函数的优化\
会估算训练的时间、训练的资源。

#### 4. 评测，很多的方法

(1) 指标

对于二分类混淆矩阵，可以得到：

真实值 ⬇ 预测值➡ | Positive | Negtive |
---|---|---
正 | TP | FN
假 | FP | TN

TP(True Positives)：正样本被正确识别的个数；\
TN(True Negative)：负样本被正确识别的个数；\
FP(False Positives)：负样本被错误识别的个数；\
FN(False Negatives)：正样本被错误识别的个数。

**敏感性(Sensitivity，SN)**：预测正确的正样本占总样本的比例，体现了模型对正样本的预测能力。 SN = TP/(TP+FN)，属于[0,1]，值越大表示模型效果越好\
**特异性(Specificity，SP)**：预测正确的负样本占总样本的比例，体现了模型对负样本的预测能力。SP = TN/(TN+FP)，属于[0,1]，越大越好\
**准确率(Accuracy，ACC)**：预测正确的样本占总样本的比例，体现了模型整体预测效果。但受极偏的数据影响大，在数据的类别不均衡的情况下，Acc不能客观评价算法的优劣。ACC = (TN+TN)/(TP+FN+TN+FP)，属于[0,1]，越大越好\
**查准率/精确率(Precision，P)**：预测为正的样本中真实正样本所占比例，P = TP/(TP+FP)，属于[0,1]，越大越好\
**查全率/召回率(Recall,R)**：所有正样本中被预测为的正的占比，R = TP/(TP+FN)，属于[0,1]，越大越好。\
**PRC(Precision Recall Curve)**：查准率和查全率是一对矛盾的度量
<img src="https://i.loli.net/2020/05/07/ejuYWBhorLfNTRi.png" width="220" height="200" align="center">

**F1度量(F1-score)**：综合考虑precision和recall，F1 = 1/(1/P+1/R) = (2×P×R)/(P+R)\
**马修相关系数(Mattew's correlation coefficient，Mcc)**，即使样本不均衡也可以使用，反映了样本真实标签和预测结果之间的相关性。 属于[-1,1]，值越高越好，说明预测结果越接近真实标签。Mcc值为1时，说明预测完全正确，为-1时，说明预测完全错误。
<img src="https://i.loli.net/2020/05/07/kb6dqvKeyzECupI.png" width="300" height="40" align="center">

**受者操作特征曲线(Receiver Operating Characteristic，ROC)曲线**。纵轴：真正率(True Positive Rate , TPR)，表示模型对正样本的召回程度,也就是SN；横轴:假正率(False Positive Rate , FPR)是负样本预测错误数与负样本总数的比值，也就是(1-SP)。TPR值越大，同时FPR值越低，即ROC曲线越陡，表明模型的预测性能越好。对于不同的阈值，计算出一系列相应的真阳率和假阳率，将它们对应的点绘制在图上，连接这些点就得到了ROC曲线。\
**曲线下面积(Area Under Curve,AUC)**，ROC曲线下方部分的面积，能比ROC更清晰直观的体现模型效果。属于[0.5,1.0]，越大越好。

<img src="https://i.loli.net/2020/05/07/2nflGjKCTJ6eWhy.png" width="200" height="200" align="center">

(2)评估方法

**留出法(hold-out)**：直接将数据集拆分为训练集和测试集，两集合互斥但同分布。可以采用进行多次随机划分，训练出多个模型，最后取平均值。\
**k-折交叉验证法(k-fold Cross Validation)**\
**留一法(Leave-one-out Cross Validation，LOO)**：可以看作k-折交叉验证法的特例，它将数据集中的每个数据作为一个独立的数据集。结果比较准确，不会受到样本随机划分带来的影响，但是计算成本过大。\
**自助法(bootstrapping)**：对全体数据进行m次有放回抽样，得到包含m个样本的训练集(部分样本会重复出现)。原始数据集中会有大约36.8%的样本不被抽到，将其作为测试集。适用于数据量较小，难以进行划分的情况，但是改变了初始的数据集分布，会引入估计偏差。

#### 5. 耦合，模块化的操作，方便代码重用

例如

网络写成
```
def network（input-tensor，bn_training，）:
   resnet（输入一个字典，表示网络的参数）   #第一个conv的窗口【x，y】   x=config.conv1.size【0】
   seresnet（输入一个字典，表示网络的参数）
   ...
   return network
```
评测方法写成一个函数库，每种方法抽象化输入和输出
```
def test_method (labels, net_result, ):
  tpr, fpr = roc（embddings，labels，threshhold，）
  ...
  return ...
```
