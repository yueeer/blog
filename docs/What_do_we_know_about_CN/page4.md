<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## Chapter 4 Current status
本章将介绍在尝试理解不同的 CNN 层所学习的内容上的当前趋势。同时，我们还将重点说明这些趋势方面仍有待解决的问题。
### 4.1current trends
为什么某些工作会有更好的效果？\
有很多用于理解的方法：对所学习到的过滤器和提取出的特征图进行可视化、受视觉皮层的生物学方法启发的ablation study、通过向网络设计中引入分析原理来最小化学习过程。
#### 4.1.1 Understanding ConvNets via visualization
##### DeConvNet
以下参考博文：[http://blog.csdn.net/hjimce/article/details/50544370 ](http://blog.csdn.net/hjimce/article/details/50544370)

为了理解网络中间的每一层提取到特征，通过反卷积的方法，进行可视化。反卷积网络可以看成是卷积网络的逆过程。

![图片10.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvWXA2dUlUYkNGYVc3SnpMLnBuZw?x-oss-process=image/format,png)

<font size=2>
网络的整个过程，从右边开始:
输入图片-》卷积-》Relu-》最大池化-》得到结果特征图-》反池化-》Relu-》反卷积</font>

特征可视化结果:

![图片11.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvdVI2VU5pREZ4c3ZUNWFWLnBuZw?x-oss-process=image/format,png)

<font size=2>
从layer 1、layer 2学习到的特征基本上是颜色、边缘等低层特征;
layer 3则开始稍微变得复杂，学习到的是纹理特征，比如上面的一些网格纹理；
layer 4学习到的则是比较有区别性的特征，比如狗头；
layer 5学习到的则是完整的，具有辨别性关键特征。
</font>

#### 4.1.2 Understanding ConvNets via ablation studies
（消融实验）ablation study就是为了研究模型中所提出的一些结构是否有效而设计的实验：看取消掉一些模块后性能有没有影响。 比如你提出了某某结构，但是要想确定这个结构是否有利于最终的效果，那就要将去掉该结构的网络与加上该结构的网络所得到的结果进行对比 。

#### 4.1.3 Understanding ConvNets via controlled design
通过分析输入信号的性质来研究网络架构本身的设计（比如层的数量或每层中过滤器的数量）。这种方法有助于让架构达到适宜应用的复杂度。

### 4.2 open problems
关键研究方向：
* ·首要的一点：开发使可视化评估更为客观的方法是非常重要的，可以通过引入评估所生成的可视化图像的质量和/或含义等指标来实现。
* ·尽管看起来以网络为中心的可视化方法更有前景，但也有必要标准化它们的评估流程。一种可能的解决方案是使用一个基准来为同样条件下训练的网络生成可视化结果。
* ·另一个发展方向是同时可视化多个单元以更好地理解处于研究中的表征的分布式方面，甚至同时还能遵循一种受控式方法。

受控方法是很有前景的未来研究方向；因为相比于完全基于学习的方法，这些方法能让我们对这些系统的运算和表征有更深入的理解。这些有趣的研究方向包括：
* ·逐步固定网络参数，分析对网络行为的影响。这个渐进式的方法有望揭示学习的作用，而且也可用作最小化训练时间的初始化方法。
* ·通过分析输入信号的性质来研究网络架构本身的设计（比如层的数量或每层中过滤器的数量）。这种方法有助于让架构达到适宜应用的复杂度。
* ·将受控方法用在网络实现上的同时可以对 CNN 的其它方面的作用进行系统性的研究，比如，可以在大多数所学习的参数固定时，研究各种池化策略和残差连接的作用。
