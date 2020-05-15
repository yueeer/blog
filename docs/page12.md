<center><img src="https://s2.ax1x.com/2019/12/21/QvumPx.jpg" width="20%"></center>

## 如何通俗地理解卷积

截取自 CSDN博主「yyl424525」:[《图卷积网络 GCN Graph Convolutional Network（谱域GCN）的理解和详细推导-持续更新》](https://blog.csdn.net/yyl424525/article/details/100058264)中关于卷积理解的部分

#### 1. 连续形式的一维卷积

在泛函分析中，卷积是通过两个函数f(x)和g(x)生成第三个函数的一种算子，它代表的意义是：<font color=#660066>两个函数中的一个(取g(x)，可以任意取)函数，把g(x)经过翻转平移,然后与f(x)的相乘，得到的一个新的函数，对这个函数积分，也就是对这个新的函数求它所围成的曲边梯形的面积。</font>

设f(t),g(t)是两个可积函数，f(t)与g(t)的卷积记为f(t)∗g(t)，它是其中一个函数翻转并平移后与另一个函数乘积的积分，是一个自变量是平移量的函数。也就是：
积的积分，是一个自变量是平移量的函数。也就是：
$$f(t)*g(t)= \int_{-\infty}^{+\infty}f(\tau)g(t-\tau)d\tau= \int_{-\infty}^{+\infty}f(t-\tau)g(\tau)d\tau$$
<img src="https://i.loli.net/2020/05/07/ZT5tKirCSI14ycw.png" height="500" width="400">

#### 2. 离散形式的一维卷积

对于定义在整数Z上的函数f,g,卷积定义为
$$(f*g)(t)={\sum}_{\tau=-\infty}^{\infty}f(\tau)g(t-\tau) $$

#### 3. 实例:掷骰子问题

想象现在有两个骰子，两个骰子分别是f跟g，f(1)表示骰子f向上一面为数字1的概率。同时抛掷这两个骰子1次，它们正面朝上数字和为4的概率是多少呢？它包含了三种情况，分别是：
- f向上为1，g向上为3；
- f向上为2，g向上为2；
- f向上为3，g向上为1；

最后这三种情况出现的概率和即问题的答案，如果写成公式，就是$\sum_{\tau =1}^3{f\left( \tau \right) g\left( 4-\tau \right)}$可以形象地绘制成下图：

<img src="https://i.loli.net/2020/05/07/ctf5udw2FbgHl9r.png" height="80" width="250">

如果稍微扩展一点，比如说认为 f(0) 或者 g(0)等是可以取到的，只是它们的值为0而已。那么该公式可以写成$\sum_{\tau=-\infty}^{\infty}f(\tau)g(4-\tau)$。

仔细观察，这其实就是卷积(f∗g)(4)。如果将它写成内积的形式，卷积其实就是$[f(-\infty),\cdots,f(1),\cdots,f(\infty)] \cdot [g(\infty),\cdots,g(3),\cdots,g(-\infty)]$
这么一看，<font color=#660066>所谓卷积，其实就是把一个函数卷(翻)过来，然后与另一个函数求内积。</font>

对应到不同方面，卷积有不同的解释：g 既可以看作我们常说的核(Kernel)，也可以对应到信号处理中的滤波器(Filter)。而 f 可以是我们所说的机器学习中的特征(Feature)，也可以是信号处理中的信号(Signal)。<font color=#660066>f和g的卷积 (f∗g)就可以看作是对f的加权求和。</font>

因此<font color=#660066>离散卷积本质就是一种加权求和。</font>本质上就是利用一个共享参数的过滤器，通过计算中心像素点以及相邻像素点的加权和来构成feature map实现空间特征的提取，加权系数就是卷积核的权重系数。系数是随机化初值，然后根据误差函数通过反向传播梯度下降进行迭代优化。

<img src="https://note.youdao.com/yws/api/personal/file/WEBdd79317327e3fcc627b8820c45ad637a?method=download&amp;shareKey=ba48914077f85c3a9f4c69cfa1cf76d0" height="300" width="300">
