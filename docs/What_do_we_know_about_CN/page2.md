<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## Chapter 2 Multilayer Networks
本章简要概述了计算机视觉中使用的最著名的多层体系结构。本章的目的是为本文其余部分的详细介绍和目前人们对卷积网络在视觉信息处理上的详细应用打下基础。
### 2.1 多层架构
在基于深度学习的网络取得成功之前，最先进的计算机视觉识别系统依赖于两个独立但相辅相成的步骤：\
(1)首先，通过一组手工设计的操作（例如卷积）将输入数据转换为合适的形式。这种转换的目的是改变数据以便它们更容易被分类器分离\
(2)转换后的数据被用来训练某种分类器(例如支持向量机)。通常，任何分类器的性能都受第一步的转换的严重影响。

具有学习能力的多层体系结构不仅对分类器进行学习，而且还直接从数据中学习所需的转换操作。 这种学习形式通常称为表示学习，在深度多层体系结构中使用时称为深度学习。

表示学习允许计算机学习使用特征的同时，也学习如何提取特征，也就是**学习如何学习**。

通常，多层体系结构被设计为放大输入的重要方面，同时对不太重要的变化变得越来越健壮。 大多数多层体系结构以线性和非线性函数进行交替叠加。 多年来，提出了多种多样的多层体系结构，其中人工神经网络架构具有突出的地位。

#### 2.1.1神经网络
![典型的神经网络结构](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTEvMmlZVEN2OFdzanRST3phLnBuZw?x-oss-process=image/format,png)

通常，每个隐藏单元$h_j$在前一层接收来自所有单元的输入，并定义为输入的加权组合,激活函数是一些非饱和线性函数例如$sigmoid$

**感知机 （perceptron）**
感知机是神经网络的起源算法，学习感知机的构造是通向神经网络和深度学习的一种重要思想。
感知机是二分类的线性分类模型，假设输入空间（特征空间）是$x\subseteq R^n$,输出空间是$y=\{+1,-1\}$。输入$x∈X$表示实例的特征向量，输出$y∈Y$表示实例的类别。由输入空间到输出空间的如下函数$f(x)=sign(w*x+b)$称为感知机。

最初感知器无法对诸如XOR之类的简单操作进行建模，缺乏适当的训练算法，阻碍了对感知器的进一步研究，直到将其推广到多层, 反向传播算法普及。更大的障碍是它们依赖大量参数，意味着需要大量训练数据和计算资源来支持参数学习。

假设你想要解决一个复杂的任务，当然应该尝试收集更多的有标签的训练数据，但是如果这太难或太昂贵，你可以尝试用无监督预训练进行网络参数的初始化，提供先验。从最低层开始，然后上升，使用无监督的特征检测算法，如**限制玻尔兹曼机**（RBM）或自动编码器。 一旦所有层都以这种方式进行了训练，就可以使用监督式学习（反向传播）对网络进行微调。
> G. E. Hinton, S. Osindero, and Y-W. Teh. A fast learning algorithm for deep belief nets. Neural Computation, 18(7):1527–1554, 2006. 2.1.1, 2.1.1

#### 2.1.2递归神经网络
在考虑依赖顺序输入的任务时，最成功的多层结构之一是递归神经网络(RNN)。

![递归神经网络](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTEvNzh3ZGdzbVVHM1NxQkE5LnBuZw?x-oss-process=image/format,png)

RNN每个隐藏单元从它在当前时间观察到的数据中获取输入，并在前一时间步骤中获取其状态。$h_t = σ(w_ix_t + u_ih_{t-1})$，σ是一类非线性压缩函数，wi和UI是控制当前和过去信息相对重要性的网络参数。

RNN的主要问题之一是它们对长期依赖关系建模的能力有限。在训练过程中，从当前时间步长反向传播到初始时间，传播的梯度将与网络的权重相乘。 由于这种乘法累加，如果权重较小，则会出现梯度消失，而权重较大则导致梯度爆炸。 由此引入了**长期短期记忆**（LSTM）。

![典型LSTM单元的图示](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTEvZW93Q1hPdHBOcTdBVnpQLnBuZw?x-oss-process=image/format,png)

该单元在当前时间$x_t$以及上一时间状态$h_{t-1}$处获取输入，并输出要在下一时间输入的$h_t$。 LSTM单元的最终输出由输入门（$i_t$），遗忘门（$f_t$）和输出门（$o_t$）以及存储单元状态($c_t$)控制。
#### 2.1.3卷积网络
卷积网络（ConvNets）是一种特殊类型的神经网络，计算机视觉中成功应用卷积结构有两个关键的设计思想：\
(1)首先，ConvNets利用图像的2D结构以及一个像素点邻域内的像素通常高度相关这一事实。 因此避免在所有像素单元之间使用一对一连接。\
(2)**特征共享**，通过在所有位置使用相同的滤波器进行卷积来输出特征图。与标准神经网络相比，ConvNets的这一特征导致其所依赖的结构要少得多。\
(3)引入了**池化**步骤，该步骤提供了一定程度的平移不变性，从而使体系结构不受位置的微小变化的影响。
网络可以随着深度的增加来表示更多抽象特征。 例如，对于对象识别的任务，ConvNets层首先关注对象部分的边缘，最终覆盖整个对象。

![卷积神经网络结构](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTEvdGVVY3hidkxpSnB1ZnJrLnBuZw?x-oss-process=image/format,png)

经过培训，神经网络可以学习输入feature map和cell之间的连接,学习过程可以概括为两个步骤：\
(1)首先，每次在输入端出现新的刺激时，将最大程度响应该刺激的cell选作该刺激类型的代表单元。\
(2)其次，输入和响应单元间的连接在每次有相同输入类型的输入时都会加强

最近的计算机视觉中部署的大多数CONVENET体系结构受到1998年提出的的**Lenet**的启发，Lenet用于手写识别。Lenet引入**反向传播**，以相对有效地学习卷积参数。

尽管CONVERNET与全连接的神经网络相比需要少得多的参数，但是它们的主要缺点仍然是他们对学习和标记数据的严重依赖。这种数据依赖可能是Convnet直到2012年才被广泛使用的主要原因之一，当时大型**ImageNet**数据集和相应的计算资源的可用性，使人们恢复对Convnet的兴趣。ConvNets在ImageNet上的成功导致了各种ConvNet体系结构的飞速创新，这一领域的大部分贡献都是基于Convnet的*不同构造*，这将在2.2节后面讨论。

#### 2.1.4生成对抗网络
GANS最初是在2014年推出的，虽然它们本身并没有提出不同的网络搭建，但是引入一种无需标签数据的无监督学习方法。 一个典型的GaN是由两个子网络：生成网络和判别网络组成的，通过两个网络互相对抗来达到最好的生成效果。

![通用的GAN结构](https://img-blog.csdnimg.cn/20191111170629486.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjU3NTc5Ng==,size_16,color_FFFFFF,t_70)

GAN的一些成功应用包括：文本转化为图像(网络输入是要呈现的图像的文本描述)，图像高分辨率转化(GAN输入低分辨率图像生成高分辨率图像)，图像修补(GAN的作用是合成真实的信息纹理，填补输入图像中缺失的信息)。

#### 2.1.5多层网络训练
使用**梯度下降**进行反向传播这种简单的梯度下降方法特别适合于训练多层网络，这要归功于使用**链规则**来计算不同层的各种网络参数的导数。

梯度下降算法的主要问题之一是学习速率的选择。学习速率太小会导致收敛速度慢，而学习速度过高则会导致跳过最优位置或在最优附近波动。为此，提出了几种改进方法，**momentum**等。另一种简单的方法是按照**固定的时间表递减学习率**，但这并不理想，因为这个时间表必须在训练之前预先设定，是完全独立于数据的。其他更复杂的方法（例如，**Adagrad ，Adadelta，Adam**）通过在频繁更改的参数上执行较小的更新而在不频繁的参数上执行较大的更新来使训练期间的学习速率适应每个要更新的参数。

使用梯度下降以及其变体的训练的主要缺点是需要大量的标记数据。解决这一困难的方法之一是求助于无监督的学习。

#### 2.1.6迁移学习
训练多层体系结构的好处之一，是学习到的特征在不同数据集甚至不同任务之间有惊人的适应性。这可以归因于其层次性，在这种层次结构中，从简单的局部的到抽象的全局的进行进行特征提取，因此，不同任务在较低级别层次结构上提取的特征往往是相同的，从而使多层体系结构更易于迁移。

 在进行迁移学习时，考虑以下几点：\
 (1)与微调整个网络相比，仅微调高层会带来系统上更好的性能。\
 (2)研究表明，进行迁移的任务差别越大，转移学习的效率就越低。\
 (3)即使对初始任务下的网络进行了微调，迁移效果也不会受到特别的影响。

### 2.2空间卷积网络
从理论上讲，卷积网络可以应用于任意维度的数据。 借助大规模数据集和功能强大的计算机进行训练，在各种应用中使用ConvNets的研究数量激增。 本节描述了最杰出的2D ConvNet体系结构，这些体系结构在2.1.3节中描述的原始LeNet基础上引入了新组件。
#### 2.2.1ConvNet发展过程中的关键架构
##### · AlexNet
重新引起人们对ConvNet体系结构兴趣的Krishevsky的AlexNet。AlexNet打破了ImageNet数据集上的识别记录。它共8层，5卷积层，3全连接层，在两个不同的GPU上并行训练。

![图片7.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvbEtyR3hmZGIyOXdFdXp5LnBuZw?x-oss-process=image/format,png)

AlexNet成功的关键有四点：\
(1)AlexNet使用**ReLU**代替饱和非线性函数（例如Sigmoids），后者在以前的ConvNet体系结构中使用过（例如LeNet )。ReLU的使用减少了梯度消失的问题，并加快训练。\
(2)AlexNet首次使用**Dropout**，随机删除（即设置为零）给定百分比的图层参数。此技术允许在每次训练略有不同的体系结构，并人为地减少每要学习的参数，最终可以帮助打破单元之间的相关性，从而避免过度拟合。\
(3)依靠**数据增强**来提高网络学习能力。例如，通过随机移动和翻转训练图像扩充训练集。\
(4)依靠几种技术来使训练过程收敛得更快，例如使用momentum和随时间降低学习率。
##### · VGG
更深层的网络可以获得更好的结果，这首先在深层VGG-Net 中得到了证明。 VGG-Net遵循AlexNet引入的标准实践，通过简单堆叠更多的层来增加深度。

VGG-Net的新颖之处在于**使用了较小的filters**（即整个网络中的3×3filters，而不是AlexNet中使用的11×11filters），增加深度而不会显着增加数量网络需要学习的参数。

![图片8.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvWXpUdWxMbnQyR2lQOFc3LnBuZw?x-oss-process=image/format,png)
##### · GoogLeNe
后来提出了一种更深的体系结构，通常称为GoogLeNet，具有22层，是第一个运用简单堆叠卷积和池化层策略的网络。 尽管比VGG-Net更深，但GoogLeNet所需的参数要少得多，这要归功于使用的**inception**模块。

![图片9.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIveWdmb0Q3UFcyelVHYzl0LnBuZw?x-oss-process=image/format,png)

在一个inception模块中，不同规模的卷积和池化操作并行进行。该模块还增加了**1×1conv**用于降低维度，保持网络规模可管理。 堆叠许多inception model构成现在广泛使用的GoogLeNet。

![图片10.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvOFJFSW11MmlUVWNuWWE0LnBuZw?x-oss-process=image/format,png)
##### · ResNet
紧随其后的是迄今为止最深的架构之一，ResNet残差网络，其主要贡献在于**残差模块**$H(x) = F(x) + x$。

![图片11.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvYlM3WDV1bHBObzlCc2Y4LnBuZw?x-oss-process=image/format,png)

通过使用跳跃式连接不同层的组件。 信号x的直接传播解决了反向传播过程中的梯度消失问题，从而可以训练非常深的网络。

![图片12.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvS3hEUHBiWWs0dGZtZVpJLnBuZw?x-oss-process=image/format,png)
##### · DenseNet
最近在ResNet的成功基础上建立DenseNet 。 在DenseNet中，每一层都连接到所有后续层。

![图片13.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvdWdsclFqaUdlb0x2MjdJLnBuZw?x-oss-process=image/format,png)

因为将一层提取的特征推到其他层，这种策略允许denseNet在每一层使用较少的过滤器，可以避免可能的冗余信息，同时减少的参数和过拟合。

![图片14.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvbVFUWWxLd2ZMUHFwbmszLnBuZw?x-oss-process=image/format,png)
#### 2.2.2  ConvNet 不变性
##### · 数据增强
使用ConvNets的挑战之一是需要非常大的数据集来学习所有底层参数。即使是像ImageNet 这样的大型数据集，有超过一百万张图像，对于训练某些深度架构来说也太小了。应对大型数据集需求的一种方法是，通过随机翻转，旋转等来更改图像，从而人为地扩充数据集。

这些扩充的主要优点是，所得网络对于各种变化变得更加稳定。实际上，这项技术是AlexNet取得巨大成功的主要原因之一。

##### · 空间变化网络
STN是显着解决网络不变性问题的著名卷积网络。在任何ConvNet体系结构的任意层添加这样的模块，就可以从输入中自适应地学习各种转换，提高其不变性，从而提高其准确性。

如下图所示，STN的输入为U，输出为V，因为输入可能是中间层的feature map，所以画成了立方体（多channel），STN主要分为下述三个步骤\
1.**Localisation net**：是一个自己定义的网络，它输入U，输出变化参数Θ，这个参数用来映射U和V的坐标关系\
2.**Grid generator**：根据V中的坐标点和变化参数Θ，计算出U中的坐标点。这里是因为V的大小是自己先定义好的，当然可以得到V的所有坐标点.\
3.**Sampler**：要做的是填充V，根据Grid generator得到的一系列坐标和原图U来填充，因为计算出来的坐标可能为小数，要用另外的方法来填充，比如双线性插值。

![图片15.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvVTNGSnVFODJ6V0xjN1JBLnBuZw?x-oss-process=image/format,png)
##### · Deformable ConvNet和Active ConvNet
引入了一种灵活的卷积模块。 它向标准卷积中中添加了2D偏移。

![图片16.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvb3FMNEY1RzZ5Q3RPMnZXLnBuZw?x-oss-process=image/format,png)

(a) 所示的正常卷积规律的采样 9 个点（绿点），(b) (c) (d) 为可变形卷积，在正常的采样坐标上加上一个位移量（蓝色箭头），其中 (c) (d) 作为 (b) 的特殊情况，展示了可变形卷积可以作为尺度变换，比例变换和旋转变换的特殊情况

![图片17.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvVzdRNEQ4bUVsdjNIclB1LnBuZw?x-oss-process=image/format,png)

一个3X3的变形卷积 ，首先通过一个小卷积层（绿色）的输出得到可变形卷积所需要的位移量，然后将其作用在卷积核（蓝色）上，达到可变形卷积的效果

与空间变化网络**交替学习**子模块参数和网络权重的方法不同，Deformable network**同时学习**权重和偏移量，因此可以更快，更轻松地在各种体系结构中进行部署。
#### 2.2.3 ConvNet 定位
除了简单的分类任务（例如对象识别）以外，最近，ConvNets在要求**精确定位**的任务（例如语义分段和对象检测）上也表现出色。
##### · FCN
在最成功的**语义分割**网络中，有所谓的**完全卷积网络**。 FCN对图像进行**像素级**的分类。

与CNN在卷积层使用全连接层得到固定长度的特征向量进行分类不同，FCN可以接受任意尺寸的输入图像，采用反卷积层对最后一个卷基层的feature map进行上采样，使它恢复到输入图像相同的尺寸，从而可以对每一个像素都产生一个预测，同时保留了原始输入图像中的空间信息，最后在上采样的特征图进行像素的分类。FCN将传统CNN中的全连接层转化成一个个的卷积层。所有的层都是卷积层，故称为全卷积网络。

![图片18.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvWFQ2elNHQTIxcEVhYjNKLnBuZw?x-oss-process=image/format,png)

在上采样步骤中使用体系结构较低层的feature起着重要作用, 低层特征倾向于捕获更细粒度的细节。
##### · 区域卷积神经网络
在**对象定位**方面，ConvNet框架内最早的方法之一就是区域卷积神经网络

以下参考CSDN博主「六月的雨唯你」的原创文章[https://blog.csdn.net/u013187057/article/details/84023468](https://blog.csdn.net/u013187057/article/details/84023468)

目标检测三阶段：\
(1)**区域选择**:利用不同尺寸的滑动窗口框住图中的某一部分作为候选区域。\
(2)**特征提取**：由于目标的形态多样性，光照、背景多样性等因素使得设计一个鲁棒的特征并不是那么容易，然而提取特征的好坏直接影响到分类的准确性。\
(3)**分类器**：进行识别，比如SVM
###### R-CNN
流程:\
(1)用selective search(选择性搜索)算法在图像中*提取多个侯选框*，通常是在多个尺度下选取的，每个提议区域将被标注类别\
(2)把所有*候选框缩放(wrap)*成固定大小，并进行归一化后输入CNN(AlexNet)网络，*提取特征*\
(3)将提取到的特征用*SVM分类*，用*线性回归模型*来微调边框位置与大小，其中每个支持向量机用来判断样本是否属于某一个类别\
(4)**非极大值值抑制**(NMS)来滤除IOU较大的区域

![图片19.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvQlgxaVJhR2dNalVyb3VRLnBuZw?x-oss-process=image/format,png)
![图片20.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvck9nNzNRRjhYMUlSQ1VxLnBuZw?x-oss-process=image/format,png)

问题：\
训练时间长、测试时间长、占用磁盘空间大
###### SPP-Net
主要贡献：\
(1)结合**空间金字塔池化**(SPP)方法实现\
CNNs的对尺度输入一般CNN需要固定的输入尺寸，因此不得不对输入数据进行crop或者warp，而这些预处理会造成数据的丢失或几何的失真。SPP-Net在卷积层和全连接层之间加入了SPP layer，此时网络的输入可以是任意尺度的，在SPP layer中每一个pooling的filter会根据输入调整大小，而SPP的输出尺度始终是固定的。

![图片22.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvN1phUVBmNU1WM2dzOVV2LnBuZw?x-oss-process=image/format,png)

(2)只对原图提取一次卷积特征\
在R-CNN中，每个候选框先resize到统一大小，然后分别作为CNN的输入.SPP Net只对原图进行一次卷积得到整张图的feature map，然后找到每个候选框上的映射patch，节省了大量的计算时间。

![图片21.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvQlB0NUtKTUNseGp3OTdzLnBuZw?x-oss-process=image/format,png)

问题:\
继承R-CNN的剩余问题:需要存储大量特征,复杂的多阶段训练\
带来新的问题:SPP层之前所有conv参数不能fine-tune
###### Fast R-CNN
主要贡献：\
(1)用**ROI pooling layer**替换SPP-Net中的SPP层，使得conv层参数可以进行fine-tune\
(2)用softmax替代SVM分类，采用**多任务损失函数**(Multi-task loss)，将分类loss和回归loss统一，不用再保存提取特征，减小存储压力，可以实现“end-to-end”的全参数训练

![图片23.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvYmcyTjlWZFRRYUwzNldILnBuZw?x-oss-process=image/format,png)

问题:\
选择性搜索提取候选框的方法非常耗时
###### Faster R-CNN (RPN+Fast R-CNN)
主要贡献:\
为解决Fast R-CNN的候选框提取的耗时问题，引用**RPN**网络（将RPN网络放在最后一个conv层后面），得到量少质优的约300个候选框。

 ![图片24.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvRjVQVjYxeU96cnV4Sm1YLnBuZw?x-oss-process=image/format,png)

 ### 2.3时空卷积网络
如第2.2节所述，通过使用ConvNet，显着提高了图像应用程序的性能，引发了人们对将2D空间ConvNets扩展到**3D时空ConvNets**进行视频分析的兴趣。 通常，文献中提出的各种时空架构只是试图将2D架构从空间域（x，y）扩展到时空域（x，y，t）。 在基于时空的ConvNet领域，有三种不同的体系结构设计脱颖而出：**LSTM**，**3D convNet**和**Two-Stream ConvNets** ， 将在本节进行描述。
#### 2.3.1基于LSTM的时空CONVnet
LST是将2D网络扩展到时空处理的早期尝试。 LSTM通过**门控状态**来控制传输状态，内部主要有三个阶段：\
(1) 忘记阶段。这个阶段主要对上一节点传进来的输入进行选择性忘记。\
(2) 选择记忆阶段。这个阶段对此阶段的输入进行选择性记忆将上面两步得到的结果相加，即可得到传输给下一阶段的状态\
(3) 输出阶段。这个阶段决定哪些会被当成当前状态的输出。
![图片1.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvTG5yWHk5YjZWa1VGS1JKLnBuZw?x-oss-process=image/format,png)

基于LSTM的ConvNets的目标是逐步集成时间信息，同时又不限于严格的输入大小。 这种架构的好处之一是使网络具备了文本描述的能力，但它们可能无法捕获更细粒度的运动。 此外，这些模型通常较大，需要更多数据，很难训练。
#### 2.3.2 3D ConvNet
3D ConvNet非常适合于时空特征学习。在3D ConvNets中，卷积和池化操作在时空上执行，而在2D ConvNets中，它们仅在空间上完成。
![图片2.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvUUdnbXF6T1o4aGY2YXNqLnBuZw?x-oss-process=image/format,png)

如上图所示，a) 在一个图像上应用2D卷积会产生一个图像。b) 在视频卷上应用2D卷积(多个帧作为多个通道)也会产生一个图像。c)在视频卷上应用3D卷积可产生另一个卷，保留输入信号的时间信息。
##### C3D
网络架构：使用目前的GPU内存，设计的C3D ConvNet，具有8个卷积层、5个池化层、两个全连接层，以及一个softmax输出层。所有3D卷积滤波器均为3×3×3，步长为1×1×1。为了保持早期的时间信息设置pool1核大小为1×2×2、步长1×2×2，其余所有3D池化层均为2×2×2，步长为2×2×2。每个全连接层有4096个输出单元。
![图片3.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvZWxLeFphSnV2T3B0aEJMLnBuZw?x-oss-process=image/format,png)

最近的一种略有不同的方法建议通过将ResNet架构修改为**T-ResNet**来整合时间。特别是，T-ResNet用1×1×T滤波器扩展了残差单元，该滤波器沿时间维学习滤波操作。

此类3D ConvNet架构的目标是直接在整个模型中集成时空，以便同时捕获信息。 这些方法的主要缺点是必须增加参数数量。
#### 2.3.3Two-Stream ConvNet
双流CNN效仿人体视觉过程理解视频信息，在处理视频图像中的环境空间信息的基础上，对视频帧序列中的时序信息进行理解。

选用卷积神经网络对获得的数据样本进行特征提取和分类，得到的单帧彩色图像与光流图像作为网络输入，在两条平行的2D ConvNet体系结构中并行运行,分别对图像进行分类后，再对不同模型得到的结果进行融合获得最终结果。\
(1) 单独的视频单帧作为表述空间信息的载体，称为**空间信息网络**；\
(2) 光流信息作为时序信息的载体输入到另外一个卷积神经网络中，用来理解动作的动态特征，称为**时间信息网络**

最近的工作称为**I3D**，它建议在两个流上使用3D卷积来同时使用3D过滤和双流架构。但是，除了网络在基准动作识别数据集上获得更好的结果这一事实之外，作者并没有提出令人信服的论据来支持除了3D滤波之外还需要冗余光流。
![图片4.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMTkvMTEvMTIvOThNRGFOUjRnalpHYnB0LnBuZw?x-oss-process=image/format,png)
### 2.4全面讨论
多层表示在计算机视觉中一直发挥着重要作用。总体而言，虽然有关多层网络的文献非常多，每个派别都主张一种体系结构优于另一种体系结构，已经出现了一些“最佳实践”。尽管这些网络在许多计算机视觉应用中都取得了良好的结果，但它们的主要缺点仍然是：对所学表征的确切性质的理解很有限，依赖大量训练数据集，没有精确的性能界限，对网络超参数（滤波器大小，非线性度，池化函数、层数和体系结构本身）的选择不明确。在下一章将讨论在ConvNets的背景下，如何选择这些参数。
