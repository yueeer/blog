<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## CSS基础总结Ⅲ
学习于黑马程序员pink老师的教程
### 1.浮动(float)
网页布局的本质一用CSS来把盒子摆放到相应位置。

CSS提供了三种传统布局方式(简单说,就是盒子如何进行排列顺序) :\
●普通流(标准流):就是标签按照规定好默认方式排列.（以块级、行内）\
●定位\
●浮动\
有很多的布局效果标准流没有办法完成，此时就可以利用浮动，因为浮动可以改变元素标签默认的排列方式。

<font color="red">网页布局第一准则:多个块级元索纵向排列找标准流,多个块级元索横向排列找浮动。</font>

float属性用于创建浮动框,将其移动到一边,直到边缘或在边缘触及包含块或另一个浮动框的边缘。
```
选择器{ float: none/left/right; }
```

#### 1.1浮动特性

- 脱离标准普通流的控制(浮)，移动到指定位置(动), (俗称脱标)

浮动的盒子不再保留原先的位置，只会影响后面的标准流不会影响前面的标准流.

<img src="https://i.loli.net/2020/08/24/AtXLkhTfRs813eu.png" width="300px" height="120px">

- 如果多个盒子都设置了浮动,则它们会按照属性值一 行内显示并且顶端对齐排列。互相贴靠在一起(不会有缝隙)。如果父级宽度装不下这些浮动的盒子，多出的盒子会另起一行对齐。

- 浮动的元素具有行内块元素的特性，因此可以直接设置宽高。如果块级盒子没有设置宽度,默认和父级一样宽,但是添加浮动后,它的大小根据内容来决定

#### 1.2浮动元素和标准流父级搭配使用

先用标准流的父元素排列上下位置,之后内部子元素采取浮动排列左右位置.

#### 1.3清除浮动
父级盒子很多情况下不方便给高度,但是子盒子浮动又不占有位置,最后父级盒子高度为0时，就会影响下面的标准流盒子。清除浮动的本质是清除浮动元素造成的影响。清除浮动之后,父级就会根据浮动的子盒子自动检测高度。父级有了高度,就不会影响下面的标准流了

<img src="https://i.loli.net/2020/08/24/I29lamiDKXkeGjy.png" width="350px">

##### 1.3.1额外标签法(隔墙法)
是W3C推荐的做法。在浮动元索末尾添加一个空的标签(必须是行内元素)。
```
选择器 { clear: left/right/both/none; }
```
<img src="https://i.loli.net/2020/08/24/kaUTHtBCAVlrf3I.png" width="350px">

```html
<style>
    .box {}
    .damao, .ermao{
        float: left;
    }
    .footer {}
    .clear{
        clear: both;
    }
</style>
<div class="box">
    <div class="damao">大毛</div>
    <div class="ermao">二毛</div>
    <div class="clear"></div>
</div>
<div class="footer"></div>
```

##### 1.3.2父级添加overflow属性
```css
.box{
    overflow: hidden;
    width: 800px;
    border: 1px solid blue;
    margin: 0 auto;
}
```

##### 1.3.3父级添加after伪元素
```html
<style>
    . clearfix::after {
        content: "";
        display: block;  /*插入元素必须是块级*/
        /*不要看见这个元素*/
        height: 0; 
        visibility: hidden;
        /*清除浮动*/
        clear: both;
    }
    . clearfix { /* IE6、7专有*/
        *zoom: 1;
    }
</style>
...
<div class="box clearfix">
```

##### 1.3.4父级添加双伪元素
```css
<style>
. clearfix:before, .clearfix:after {
    content:"";
    /*转化为块级元素并且before和after两块一行显示*/
    display:table;
}
. clearfix:after {
    clear:both;
}
. clearfix {
    *zoom: 1;
}
</style>
...
<div class="box clearfix">
```

### 2.CSS定位
#### 2.1为什么需要定位
浮动可以让多个块级盒子一行没有缝隙排列显示 ,经常用于横向排列盒子。定位则是可以让盒子自由的在某个盒子内移动位置或者固定屏幕中某个位置,并且可以压住其他盒子。

#### 2.2定位组成
定位=定位模式+边偏移。

定位模式用于指定一个元索在文档中的定位方式。 通过CSS的position属性来设置。

<img src="https://i.loli.net/2020/08/24/XFpzs2ut6lbqBOV.png" width="550px">

边偏移决定了该元素的最终位置，有4个属性。

<img src="https://i.loli.net/2020/08/24/jYD1kzNfAIbhWx8.png" width="600px">

##### 2.2.1静态定位static
是元索的默认定位方式,无定位的意思。
```css
选择器{ position: static; }
```

##### 2.2.2相对定位relative (重要)
元素在移动位置的时候,是相对于它原来的位置来说的。
```css
选择器{ 
    position: relative;
    top: 100px; 
}
```
原来在标准流的位置继续占有，后面的盒子仍然以标准流的方式对待它。(<font color="purple">不脱标,继续保留原来位置</font>)

##### 2.2.3绝对定位absolute (重要)
元索在移动位置的时候,是相对于它祖先元索来说的。
```css
.grandfa{
    position: relative;
    ...
}
.father{
    width= 500px;
    height= 500px;
    background-color: skyblue;
}
/*以grandfa为准*/
.son{ 
    position: absolute;
    left: 10px;
    ...
}
```
如果没有祖先元素或者祖先元素没有定位,则以浏览器为准定位(Document文档)。\
如果祖先元素有定位(相对、绝对、固定定位) , 则以最近一级的有定位祖先元素为参考点移动位置。\
绝对定位<font color="purple">不再占用原来位置。</font>

**子绝父相**\
①子级绝对定位,不会占有位置,可以放到父盒子里面的任何一个地方,不会影响其他的兄弟盒子。\
②父盒子需要加定位限制子盒子在父盒子内显示。\
③父盒子布局时,需要占有位置,因此父亲只能是相对定位。

##### 2.2.4固定定位fixed (重要)
元索固定于浏览器可视区的位置。浏览器页面滚动时元索位置不变。
```css
选择器{ 
    position: fixed;
    top: 0;
    right: 0; 
}
```
以浏览器的可视窗口为参照点移动元素，与父元素无关。\
<font color="purple">不再占用原来位置</font>

如何固定在版心右侧位置:\
1.让固定定位的盒子left: 50%.走到浏览器可视区(也可以看做版心)的一半位置。\
2.让固定定位的盒子margin-left:版心宽度的一半距离。多走版心宽度的一半位置。
```html
<style>
    .w{
        width: 800px;
        height: 1400px;
        background-color: pink;
    }
    .fixed{
        position: fixed;
        left: 50%;  /*1.走到浏览器可视区(也可以看做版心)的一半位置*/
        margin-left: 400px; /*2.走版心宽度的一半*/
        width: 50px;
        height: 150px;
        background-color: skyblue;
    }
</style>
<body>
    <div class="fixed"></div>
    <div class="w">版心盒子 800像素</div>
</body>
```

##### 2.2.5粘性定位sticky (了解)
可以认为是相对定位和固定定位的混合。
```css
选择器{ 
    position: sticky; 
    /*当距离可视区域top10px时，固定不动*/
    top: 10px; 
}
```

1.以浏览器的可视窗口为参照点移动元素(固定定位特点)\
2.粘性定位<font color="purple">占有原先的位置</font>(相对定位特点)\
3.必须添加top. left. right. bottom其中一个才有效

<img src="https://i.loli.net/2020/08/24/Ae1yoPOFUWabnqY.png" width="450px">

#### 2.3定位叠放次序z-index
在使用定位布局时,可能会出现盒子重叠的情况。此时,可以使用z-index来控制盒子的前后次序(z轴)。
```css
选择器{ z-index: 1; }
```

●数值可以是正整数、负整数或0,默认是auto ,数值越大,盒子越靠上\
●如果属性值相同,则按照书写顺序,后来居上

#### 2.4拓展
##### 2.4.1绝对定位的盒子居中
加了绝对定位的盒子不能通过`margin:0 auto`水平居中，通过以下方法实现水平和垂直居中。
```css
box {
    position: absolute;
    /*1.left走50%父容器宽度的一半*/
    left: 50%;
    top: 50%
    /* 2. margin 负值往左边走自己盒子宽度的一半*/
    margin-left: -100px;
    margin-top: -100px
    width: 200px;
    height: 200px ; 
    background-color: pink ;
}
```

##### 2.4.2定位特殊特性
绝对定位和固定定位也和浮动类似。\
1.行内元素添加绝对或者固定定位,可以直接设置高度和宽度。\
2.块级元素添加绝对或者固定定位,如果不给宽度或者高度,默认大小是内容的大小。

浮动元素只会压住它下面标准流的盒子,但是不会压住盒子里面的文字(图片)，可作文字环绕效果，但是绝对定位(固定定位)会压住下面标准流所有的内容。




### 3.元素显示与隐藏
#### 3.1 display 显示隐藏
●display：none ; 隐藏对象，隐藏后不占有原来的位置\
●display : block ;除了转换为块级元索之外,同时还有显示元素的意思
#### 3.2 visibility 显示隐藏
●visibility : hidden;元素隐藏，隐藏后占有原来的位置\
●visibility : visible; 元素可视
#### 3.3 overflow 溢出显示隐藏
●overflow : hidden; 溢出元素隐藏\
●overflow : visible; 溢出元素可视\
●overflow : scroll; 显示滚动条\
●overflow : auto; 如果溢出显示滚动条

### 4.网页布局
#### 4.1页面布局整体思路
1.必须确定页面的版心(可视区) , 测量可得知。\
2.分析页面中的行模块,以及每个行模块中的列模块。\
3.一行中的列模块经常浮动布局,先确定每个列的大小,之后确定列的位置。\
4.制作HTML结构。

遵循,<font color="red">先有结构,后有样式的原则。</font>

#### 4.2标准流 vs. 浮动 vs. 定位
1.标准流\
可以让盒子上下排列或者左右排列,<font color="red">垂直的块级盒子显示就用标准流布局。</font>

2.浮动\
可以让多个块级元素一行显示或者左右对齐盒子,<font color="red">多个块级盒子水平显示就用浮动布局。</font>

3.定位\
定位最大的特点是有层叠的概念,就是可以让多个盒子前后叠压来显示。<font color="red">如果元素自由在某个盒子内移动就用定位布局。</font>

#### 4.3CSS属性书写建议顺序

1.布局定位属性: display / position/ float / clear / visibility/ overflow\
2.自身属性: width/ height / margin/ padding /border/ background\
3.文本属性: color/ font / text-decoration/ text-align/ vertical-align/ white-space/ break-word\
4.其他属性( CSS3 ) : content/ cursor / border-radius/ box-shadow / text-shadow/background:linear-gradient...

#### 常见的图片格式

1.jpg图像格式\
JPEG ( JPG )对色彩的信息保留较好,高清,颜色较多,我们<u>产品类的图片</u>经常用jpg格式的。\
2.gif图像格式\
GIF格式最多只能储存256色,所以通常用来显示简单图形及字体,但是可以保存透明背景和<u>动画效果</u>。\
3.png图像格式\
结合了GIF和JPEG的优点,具有存储形式丰富的特点,能够保持透明背景.如果想要切成<u>背景透明</u>的图片,请选择png格式。\
4.PSD图像格式\
是 Photoshop的专用格式,里面可以存放图层、通道、遮罩等多种设计稿，对前端人员来说,最大的优点可以直接从上面复制文字,获得图片,还可以测量大小和距离。
