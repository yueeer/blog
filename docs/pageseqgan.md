<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## SeqGAN总结
seqGan出自AAAI 2017

> SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient

#### 1.背景
虽然现在GAN的变种越来越多，用途广泛，但是它们的对抗思想都是没有变化的。就是在生成的过程中加入一个可以鉴别真实数据和生成数据的鉴别器，使生成器G和鉴别器D相互对抗，D的作用是努力地分辨真实数据和生成数据，G的作用是努力改进自己从而生成可以迷惑D的数据。当D无法再分别出真假数据，则认为此时的G已经达到了一个很优的效果。

#### 2.Motivation
论文的出发点也是意识到了标准的GAN在处理像序列这种离散数据时会遇到的困难，主要体现在两个方面：<font color = "darkblue">Generator难以传递梯度更新</font>，<font color = "purple">Discriminator难以评估非完整序列。</font>

对于前者，作者给出的解决方案是<font color = "darkblue">把整个GAN看作一个强化学习系统，用强化学习的Policy Gradient算法更新Generator的参数</font>；对于后者，作者则借鉴了<font color = "purple">蒙特卡洛树搜索（Monte Carlo tree search，MCTS）的思想，对任意时刻的非完整序列都可以进行评估。</font>

<font color="darkblue">
Policy Gradient算法

不通过误差反向传播，它通过观测信息选出一个行为直接进行反向传播，他并没有误差，而是利用reward奖励直接对选择行为的可能性进行增强和减弱，好的行为会被增加下一次被选中的概率，不好的行为会被减弱下次被选中的概率。
</font>

<font color="purple">
蒙特卡洛树搜索

Monte Carlo Tree Search（简称 MCTS），是一种做出最优决策的方法，一般是在组合博弈中的行动规划形式。基本的 MCTS 算法非常简单：根据模拟的输出结果，按照节点构造搜索树。
</font>

#### 3.大体思路
G采用RNN结构，为了防止梯度爆炸和消失问题，选择了LSTM模型。
D采用CNN结构，利用了<font color="green">highway net</font>模型。

<font color="green"> Highway Network的出现也是为了解决深层网络难以训练的问题，通过门控机制来实现。</font>

<img src = "https://img-blog.csdnimg.cn/img_convert/9373b706ad721950a552d3d099112196.png" width="500px">

真实数据加上G的生成数据来训练D，paper中将policy network当做G，因为D需要对一个完整的序列评分，所以就是用MCTS（蒙特卡洛树搜索）将每一个动作的各种可能性补全，D对这些完整的序列产生reward，回传给G，通过增强学习更新G，训练出一个可以产生下一个最优的action的生成网络。

#### 4.问题定义
根据强化学习的设定，在时刻t，当前的状态s被定义为“已生成的序列”$(y_1,...,y_{t-1})$，记作$Y_{1:t-1}$，而动作a是接下来要选出的元素$y_t$，所以生成模型定义为:$G_\theta(y_t|Y_{1:t-1})$($\theta$是模型参数)，输出的是动作的概率分布。

根据Policy Gradient算法，Generator的优化目标是令从初始状态$s_0$开始的value（累积的reward期望值）最大化：

$$J(\theta) = E[R_T|s_0,\theta] = \sum_{y_1\in \gamma}{G_{\theta}\left( y_1|s_0 \right) \cdot Q_{D_{\phi}}^{G_{\theta}}\left( s_0,y_1 \right)}$$

其中,$R_T$是完整序列的reward，$Q_{D_{\phi}}^{G_{\theta}}\left( s_0,y_1 \right)$表示序列的行为值函数（action-value），是指“在状态s下选择动作a，此后一直遵循着policy $G_\theta$做决策，最终得到的value”。所以对于最右边的式子我们可以这样来理解：在初始状态下，对于$G_\theta$可能选出的每个$y_1$，都计算对应的value，把这些value根据$G_\theta$的概率分布加权求和，就得到了初始状态的value。

Discriminator只能对生成的完整序列$Y_{1:T}$进行评估，因此目前只能对状态为$Y_{1:T-1}$的value进行定义：
$$Q_{D_{\phi}}^{G_{\theta}}\left( a = y_T,s = Y_{1:T-1}  \right) = D_{\phi}(Y_{1:T})$$
$D_{\phi}(Y_{1:T})$表示整个序列输入到判别器D中输出的奖励。

这是远远不够的，必须要对任意状态的value都有定义。对于非完整的序列$Y_{1:t}$，以$g_{\beta}$（等同于Generator）作为roll-out policy，将剩余的T-t个元素模拟出来，这样就可以利用Discriminator进行评估了。为了减小对value估计的误差，会进行N次模拟，对这N个结果取平均值。
$$
Q_{D_{\phi}}^{G_{\theta}}\left( s=Y_{1:t-1},a=y_t \right) =\left\{ \begin{array}{l}
	\frac{1}{N}\sum_{n=1}^N{D_{\phi}\left( Y_{1:T}^{n} \right) ,Y_{1:T}^{n}\in MC^{G_{\beta}}\left( Y_{1:t};N \right) \ t<T}\\
	D_{\phi}\left( Y_{1:t} \right) \ t=T\\
\end{array} \right.
$$

生成模型的参数更新为:
$$
\theta \ =\ \theta +\alpha _h\nabla _{\theta}J\left( \theta \right)
$$
对于判别模型，它的目标是提高判断真实数据的概率并且减少判断生成数据的概率，故目标为:
$$
\min\text{\ }-E_{YP_{data}}\left[ \log D_{\phi}\left( Y \right) \right] -E_{YG_{\theta}}\left[ \log \left( 1-D_{\theta}\left( Y \right) \right) \right]
$$

#### 5.算法
<img src = "https://i.loli.net/2020/09/19/XTEGsePyugBFpct.png" width = 500px>

1.首先随机初始化Gθ网络和D网络参数

2.预训练$G_θ$网络，目的是提高$G_θ$网络的搜索效率。\
首先利用一个完美训练的神经网络target_lstm生成一些真实数据，利用这些数据通过MLE(最大似然估计)训练Generator。

3.预训练Discriminator\
将target_lstm生成的真实数据作为正样本，$G_θ$生成的数据作为负样本，用来通过最小化交叉熵来预训练一个二分类的神经网络。(具有highway的CNN)

4.开始进行对抗训练，循环直到收敛。\
1）首先重复执行g次更新生成模型：\
(1)首先利用当前的$G_θ$生成batch_size大小sequence，\
(2)利用roll out网络进行MC search并采样句子喂给Discriminator进行评价返回
$Q_{D_{\phi}}^{G_{\theta}}\left( s = Y_{1:t-1} ,a = y_t \right)$\
(3)基于下式更新Generator参数。
$$
\theta =\theta +\alpha _h\nabla _{\theta}J\left( \theta \right)
$$

2）重复执行d次更新判别模型\
更优的G生成更好的负样本，和真实数据一起训练D。
