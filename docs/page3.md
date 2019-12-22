<center><img src="https://s2.ax1x.com/2019/12/21/QvumPx.jpg" width="20%"></center>

## Chapter 3 理解Convnet构建块
本章研究典型的CNN中各处理层的作用和意义。特别是，将从理论和生物学的角度介绍ConvNet各种组件。每种组件的介绍后面都有discussion，总结了我们当前的理解水平。
### 3.1卷积层
卷积层可以说是ConvNet体系结构中最重要的结构之一。 基本上，卷积是一种**线性的、平移不变性**的运算，对输入信号进行**局部加权组合**。 根据所选择的权重集合（即所选择的*点扩散函数（point spread function）*）的不同，也将揭示出输入信号的不同性质。同时，选择正确的**kernel**以捕获输入信号中的最显著和最重要的信息至关重要，这可以使人们对信号的内容进行有力的推断。 本节讨论了进行核选择的一些不同方法。

*点扩展函数( PSF)描述了成像系统对点源或点对象的响应。PSF更一般的术语是一个系统的脉冲响应（impulse response）*

卷积核的可优化参数是通过训练网络最小化损失函数$L$来调节的：
![图片5.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvZ1dudW9Wa3dQbFFoMVJVLnBuZw?x-oss-process=image/format,png)

其中$L_{conv}$是卷积层数,$L$是总层数. 在上式中, $L_fc$和$L_{conv}$是fc层和conv层的非监督损失函数. 它们的作用是最小化重建误差，并使用未标记的数据进行训练. 与之对应的$L_{task}$是一个监督损失函数, 该函数是用来训练最大化分类准确率的.
#### 生物学视角
哺乳动物视觉皮层中分层处理的神经为空间和时空的ConvNets提供了启发。特别通过从简单到复杂的单元层叠，逐步提取视觉输入的抽象属性。在视觉皮层处理的早期阶段，简单单元能够检测原始特征，例如定向的光栅，条和边缘，后续阶段会提取更复杂的特征。

比较流行的选择是：一组不同比例的*定向Gabor滤波器*或高斯导数。更一般地，通常选择定向带通滤波器。实际上，这些相同的Gabor内核也扩展到了色域和时域，以分别解释颜色和运动敏感神经元。

<font  size=2 >
Gabor滤波器的频率和方向表示接近人类视觉系统对于频率和方向的表示.
下图为gabor滤波器和脊椎动物视觉皮层感受野响应的比较：第一行代表脊椎动物的视觉皮层感受野，第二行是Gabor滤波器，第三行是两者的残差。可见两者相差极小。</font>

![图片6.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvRGhydk9UN2JFZkplUTV1LnBuZw?x-oss-process=image/format,png=10x10)

<font  size=2 >Gabor滤波器的这一性质，使得其在视觉领域中经常被用来作图像的预处理。
在空域，一个2维的Gabor滤波器是一个正弦平面波和高斯核函数的乘积。实际应用中，Gabor滤波器可以在频域的不同尺度，不同方向上提取相关特征。</font>
#### HMAX
基于特征组合的物体识别框架HMAX模型的主要思想是通过组合来自先前层的过滤器获得层次结构较高层的过滤器，这种方法最终应该允许模型在更高层上响应越来越复杂的模式。 这种方法与**Hebbian理论**很好地联系在一起，后者说“一起激发的神经元连在一起（Cells that fire together, wire together）” 。
![7.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvQjZVdXlITmNHSk1kMnpnLnBuZw?x-oss-process=image/format,png)
### 3.2 整流
多层网络通常是高度非线性的，而整流（rectification）则通常是将非线性引入模型的第一个处理阶段。

整流是指将**激活函数**(点方面的非线性)应用到卷积层的输出上。计算神经科学家引入整流步骤的目的是寻找能最好地解释当前神经科学数据的合适模型。机器学习研究者使用整流的目的是为了让模型能更快和更好地学习。
![8.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvZE1oV05iRkhmcmdjU0xsLnBuZw?x-oss-process=image/format,png)
### 3.3 归一化
所以多层架构是高度非线性的,除了前一节讨论的激活函数，归一化（normalization）是 CNN 架构中有重要作用的又一种非线性处理模块。

CNN 中最广泛使用的归一化形式是所谓的 **Divisive Normalization**（DN，也被称为局部响应归一化）。

### 3.4 池化
池化运算的目标是为位置和尺寸的改变带来一定程度的不变性。在 CNN 网络上，主要的争论点是池化函数的选择。使用最广泛的两种池化函数分别是**平均池化**和**最大池化**。
<font size=2>平均池化和最大池化在 Gabor 滤波后的图像上的比较。</font>
![图片9.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvRHQ4NU93eFVsTjNxUTZLLnBuZw?x-oss-process=image/format,png)
<font  size=2 >

其中上面一行是应用于原始灰度值图像的结果，下面一行是应用于 Gabor 滤波后的图像上的结果。\
（a）展示了不同尺度的平均池化的效果，平均池化能得到灰度值图像的更平滑的版本，而稀疏的 Gabor 滤波后的图像则会褪色消散。\
（b）给出了不同尺度的最大池化的效果，可以看到，最大池化会导致灰度值图像质量下降，而 Gabor 滤波后的图像中的稀疏边则会得到增强。</font>
