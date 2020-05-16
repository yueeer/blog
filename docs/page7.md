<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 典型的信息度量指标及算法

### 指标

#### 1 熵（entropy自信息）
表示随机变量的不确定性。一个随机变量的熵越大,它的不确定性越大，那么正确估计其值的可能性就越小。
如果X是一个离散型随机变量，其概率分布为$p(x)=P(X=x), x∈X$，$X$的熵$H(X)$为：$$
H\left( X \right) =-\underset{x\in X}{\varSigma}p\left( x \right) \log _2p\left( x \right) $$

#### 2 熵的变形
##### 2.1 联合熵（joint entropy）
联合熵实际上就是描述一对随机变量平均所需要的信息量。
如果$X,Y$是一对离散型随机变量，$X,Y\sim p(x,y)$,$X,Y$的联合熵$H(X,Y)$为：
<font size=2>
$$H\left( X,Y \right) =-\underset{x\in X}{\varSigma}\underset{y\in Y}{\varSigma}p\left( x,y \right) \log _2p\left( x,y \right) $$
</font>

##### 2.2 条件熵（conditional entropy）
给定$X$的值前提下随机变量$Y$的随机性的量，表示在一个条件下，随机变量的不确定性。
<font size=2>
$$H\left( Y|X \right) = \underset{x\in X}{\varSigma}p\left( x \right) H\left( Y|X=x \right)= \underset{x\in X}{\varSigma}p\left( x \right) \left[ -\underset{y\in Y}{\varSigma}p\left( y|x \right) \log _2p\left( y|x \right) \right]
= -\underset{x\in X}{\varSigma}\underset{y\in Y}{\varSigma}p\left( x,y \right) \log _2p\left( y|x \right)$$
</font>

##### 2.3 相对熵（relative entropy，KL距离，信息散度）
衡量两个概率分布的匹配程度，两个分布差异越大，KL散度越大，设$P(x),Q(x)$是随机变量$X$上的概率分布
<font size=2>
$$KL\left( P||Q \right) =\varSigma P\left( x \right) \log \frac{P\left( x \right)}{Q\left( x \right)}\\
KL\left( P||Q \right) =\int{P\left( x \right) \log \frac{P\left( x \right)}{Q\left( x \right)}dx}$$
</font>

##### 2.4 交叉熵（cross entropy）

$$ H\left( p,q \right) =-\varSigma _{i=1}^{n}p\left( x_i \right) \log \left( q\left( x_i \right) \right) $$


#### 3 信息增益
信息增益=信息熵-条件熵    \
表示在一个条件下，信息不确定性减少的程度。在特征选择的时候常常用信息增益，如果IG（信息增益大）的话那么这个特征对于分类来说很关键

#### 4 困惑度（perplexity）
用来度量一个概率分布或概率模型预测样本的好坏程度。语言模型训练完之后，测试集中的句子都是正常的句子，在测试集上的概率越高，迷惑度越小，语言模型越好
<font size=2>
$$PP\left( W \right) =P\left( w_1,w_2,...,w_N \right) ^{-\frac{1}{N}}=\sqrt[N]{\frac{1}{P\left( w_1,w_2,...,w_N \right)}}$$
</font>

#### 5 互信息（mutual information)
如果 $(X, Y) \sim P(x, y)$, $X, Y$ 之间的互信息 $I(X; Y)$定义为:
<font size=2>
$$
I\left( X;Y \right) =\underset{x\in X}{\varSigma}\underset{y\in Y}{\varSigma}p\left( x,y \right) \log \frac{p\left( x,y \right)}{p\left( x \right) p\left( y \right)}
$$
</font>
 $I (X; Y)$取值为非负。当$X、Y$相互独立时，$I(X,Y)$最小为0

#### 6 点互信息PMI（Pointwise Mutual Information）
 点互信息只是对其中两个点进行相关性判断，互信息其实就是对X和Y的所有可能的取值情况的点互信息PMI的加权和
 <font size=2>
 $$
PMI\left( x;y \right) =\log \frac{p\left( x,y \right)}{p\left( x \right) p\left( y \right)}=\log \frac{p\left( x|y \right)}{p\left( x \right)}=\log \frac{p\left( y|x \right)}{p\left( y \right)}
$$
</font>

#### 7 对称不确定性SU（symmetrical uncertainty）
如果直接使用互信息量来选取特征，会导致倾向于选取取值较大的特征，SU修正了使用互信息选取特征的偏置，并对互信息量做了归一化处理，使得在进行特征相关性比较时相对公平。对称不确定性将取值标准化到0到1之间，取值为1是表示两个特征完全相关，即根据一个变量的值完全可以预测出另一个变量的值。取值为0时表示两个变量是完全独立的。$I(X;Y)$表示信息增益
<font size=2>$$
SU\left( X,Y \right) =\frac{I\left( X;Y \right)}{H\left( X \right) +H\left( Y \right)}
$$</font>

#### 8 信息标准变化NVI（Normalized variation of information）
$R(X,Y)$反映了变量间独立性的偏离程度。引入规范化的$NVI∈[0,1]$来描述变量间的独立程度。
<font size=2>
$$
R\left( X,Y \right) =\frac{I\left( X;Y \right)}{H\left( X,Y \right)}\\
NVI=1-R\left( X,Y \right) =\frac{VI\left( X,Y \right)}{H\left( X,Y \right)}
$$
</font>

### 相关算法描述
#### 1 基于相关的快速滤波器选择算法 FCBF(fast correlation-based filter selection algorithm)
FCBF算法实验基于信息论的**对称不确定性度量SU**来衡量两个特征的相关性，并提出一个可以有效分析冗余特征的快速过滤特征选择算法。

该算法的核心思想是如果一个特征和类别之间的不确定程度很高，且它与已选特征之间的不确定性程度很低，那么这个特征就是重要的，该特征将给分类性能带来更多的信息含量，即特征与类别之间是**强相关关系**（predominant correlation）。

*强相关关系：当且仅当在相关子集S中不存在另外一个特征，它们之间的 SU 值大于该特征与类别之间的 SU 值。*

算法框架：\
1.选择与类别相关的特征。采用对称不确定性度量方法SU，计算每个特征与类别之间的相关性，根据设置的阈值，选出其中最相关的特征，形成相关子集S，并对其按照SU的值排序。\
2.去除冗余特征，保留强相关特征。从相关子集S的第一个特征 F1开始判断，如果这个特征与S中其它特征Fp（Fp是相关子集中第二个特征到最后一个特征）的SU值大于该特征与类别之间SU值，那么说明特征Fp的信息对于已选子集而言是多余的，直接从相关子集中删除，反之说明特征Fp是重要的，它包含了特征F1没有包含的分类信息，因此必须保留。以F1为基准判断完成之后，从F2开始判断, 重复以上过程，知道没有特征被移走或者全部判断完毕为止。

#### 2 最大相关最小冗余算法 mRmR
常用的特征选择方法是最大化特征与分类变量之间的相关度，就是选择与分类变量拥有最高相关度的前k个变量。但是单个好的特征的组合并不一定能增加分类器的性能，因为有可能特征之间是高度相关的，这就导致了特征变量的冗余。

mRMR的核心思想即最大化特征与分类变量之间的相关性，而最小化特征与特征之间的相关性。特征集S与类c的相关性由各个特征f i和类c之间的所有互信息值的平均值定义：
<font size=2>
$$D\left( S,c \right) =\frac{1}{|S|}\underset{f_i\in S}{\varSigma}I\left( f_i;c \right) $$
</font>
集合S中所有特征的冗余是特征f i和特征f j之间的所有互信息值的平均值定义：
<font size=2>
$$R\left( S \right) =\frac{1}{|S|^2}\underset{f_i,f_j\in S}{\varSigma}I\left( f_i;f_j \right)  $$
</font>
mRMR标准是上面给出的两种措施的组合，定义如下：
<font size=2>
$$mRMR=\ \underset{S}{\max}\left[ D\left( S,c \right) -R\left( S \right) \right] $$
</font>
