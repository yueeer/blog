<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## CSS基础总结Ⅱ
学习于黑马程序员pink老师的教程
### 1.Emmet语法
使用缩写，来提高htm/css的编写速度
#### 1.1生成html结构
生成标签直接输入标签名按tab键即可，比如div，然后tab键 ,就可以生成`<div></div>`\
如果想要生成多个相同标签加上\*就可以了，比如div*3 ，就可以快速生成3个div\
如果有父子级关系的标签,可以用>，比如ul>li就可以了\
如果有兄弟关系的标签,用+就可以了，比如div+p\
如果生成带有class或者id名字的标签x，直接写x.classname或者x#idname+enter/tab键就可以了\
如果生成的div类名是有顺序的，可以用自增符号\$\
.demo$*5,得到
```html
<div class="demo1"></div>
<div class="demo2"></div>
<div class="demo3"></div>
<div class="demo4"></div>
<div class="demo5"></div>
```
如果想要在生成的标签内部写内容可以用{}示，div{good}
#### 1.2生成css样式
eg:输入lh26p得到
```css
line-height: 26px;
```

### 2.元素显示模式
元索显示模式就是元素(标签)以什么方式进行显示,比如`<div>`自己占一行,比如一行可以放多个`<span>`.

#### 2.1类别
##### 2.1.1块元素
常见的块元素有`<h1>`~`<h6>`、`<p>`、`<div>`、 `<ul>`、 `<ol>`、 `<li>`等 ,其中`<div>`是最典型的。

①自己独占一行。\
②高度,宽度、外边距以及内边距都可以控制。\
③宽度默认是容器(父级宽度)的100%。\
④是一个容器及盒子,里面可以放行内或者块级元素。\
⑤文字类的元素内不能使用块级元素，`<h1>`~`<h6>`、`<p>`主要用于存放文字,因此不能放块级元素

##### 2.1.2行内元素（内联元素）
常见的行内元素有`<a>`、`<strong>`、 `<b>`、 `<em>`、`<i>`、 `<del>`、 `<S>`、 `<ins>`、 `<U>`、 `<span>`等 ，其中`<span>`标签是最典型的行内元素。

①相邻行内元索在一行上, 一行可以显示多个。\
②高、宽直接设置是无效的。\
③默认宽度就是它本身内容的宽度。\
④行内元素只能容纳文本或其他行内元素。\
⑤特殊情况链接`<a>`里面可以放块级元素,但是给`<a>`转换一下块级模式最安全。

##### 2.1.3行内块元素

在行内元索中有几个特殊的标签`<img/>`、 `<input/>`、 `<td>`,同时具有块元素和行内元素的特点。

①行内块在一行上,但是他们之间会有空白缝隙。一行可以显示多个 (行内元素特点)。\
②默认宽度就是它本身内容的宽度(行内元索特点)。\
③高度,行高、外边距以及内边距都可以控制(块级元素特点)。

#### 2.2元素显示模式的转换
一个模式的元素需要另外一种模式的特性，比如想要增加链接`<a>`的触发范围

```html
<style>
    a{
        width: 150px;
        height: 50px;
        background-color: pink;
        /* 转换为块级元素 */
        display: block; 
    }
    div{
        background-color: purple;
        /* 转换为行内元素 */
        display: inline; 
    }
    span{
        width: 150px;
        height: 50px;
        background-color: blue;
        /* 转换为行内快元素 */
        display: inline-block; 
    }
</style>
...
<a href="#">what</a>
<div>我是块级元素</div>
<span>我是行内元素</span>
```

### 3.CSS背景（大背景或小装饰类）
#### 3.1设置背景颜色，背景图
```css
background-color : transparent(透明) / color
/*同时有背景颜色和背景图片时，图片会压住颜色。*/
background-image : none / url(图片地址)
/*背景平铺：在HTML页面上对背景图像进行平铺。*/
background-repeat : repeat(默认)/no-repeat/repeat-x(沿x轴)/repeat-y(沿轴) 
```
- 改变图片在背景中的位置
```css
background-position: x y; /*x和y坐可使用方位名词或者精确单位*/
```
<font size="2">参数值\
(1)length:百分数|由浮点数字和单位标识符组成的长度值\
(2)position:left | center | right | top |  bottom 方位名词
</font>

如果参数值是精确坐标,那么第一个是x，第二个是y，如果只指定一个,那一定是x，y垂直居中\
如果指定的两个值都是方位名词,则两个值前后顺序无关，left top=top left，如果只指定了一个,则另一个值默认居中对齐\
如果指定的两个值是精确单位和方位名词混合使用，则第一个值是x坐标，第二个值是y坐标

#### 3.2背景附着（背景图像固定）
设置背景图像是否固定或者随着页面的其余部分滚动。
```css
background-attachment : scroll / fixed
```

#### 3.3简化背景属性的代码
可以合并简写在同一个属性background中。习惯约定顺序为:
```css
/*background:背景颜色 背景图片地址 背景平铺 背景图像滚动 背景图片位置;*/
background: transparent url(image.jpg) repeat-y fixed top ;
```

#### 3.4 背景颜色半透明
```css
background: rgba(0, 0, 0, .3); /*alpha透明度,取值范围在0~1*/
```

<img src="https://i.loli.net/2020/08/23/frtTVPRWkXe5yNi.png" width="550px" height="220px">

#### 3.5 背景色渐变
```css
background: linear-gradient (起始方向，颜色1,颜色2，...);
```

例：
```css
div {
        width: 600px;
        height: 200px;
        /* 背景渐变必须添加浏览器私有前缀 */
        /* background: -webkit-linear-gradient(left, red, blue); */
        /*起始方向可以是:方位名词或者度数,，如果省略默认就是top*/
        /* background: -webkit-linear-gradient(red, blue); */
        background: -webkit-linear-gradient(top left, red, blue);
}
```

### 4.CSS非常重要的三个特性
#### 4.1层叠性
相同选择器给设置不同的样式,此时一个样式就会覆盖(层叠)另一个冲突的样式。

层叠性主要解决样式冲突的问题，遵循<font color="blue">就近原则</font>,哪个样式离结构近,就执行哪个样式
```css
div{
    color:red;
    font-size:18px;
}
div{ color:pink; } 
/*显示18px粉色*/
```

#### 4.2继承性
子标签会继承父标签的某些样式( text- , font- , line-这些元素开头的,以及color属性)
```html
div{
    color:red;
    font-size:18px;
}
...
<div>
    <p>子承父业</p>  <!--显示18px红色-->
<div>
```
行高的继承
```css
body{
    font: 12px/1.5 "Microsoft YaHei";
}
div{
    /*<继承自body,行高为font-size的1.5倍,可以根据文字大小自动调整行高*/
    font-size: 14px;
}
```

#### 4.3优先级
当同一个元素指定多个选择器,就会有优先级的产生。比较按照权重从左至右。

<img src="https://i.loli.net/2020/08/23/mZHQfTGWU8oIsdv.png" width="500px" >

```html
<style>
    #demo{ color: green } /*ID选择器*/
    div{ color: pink ！important}  /*元素选择器*/
    .test{ color: red } /*类选择器*/
</style>
...
<body>
    <div class="test" id="demo" style="color:purple">good</div>
</body>
<!--result : 粉色-->
```
```html
#father{ color: red; }
p{ color: pink; }
...
<div id="father">
    <p>good</p>
</div>
<!--result : 粉色   p作为元素选择器的权重>继承得到的权重0-->
```

权重叠加:如果是复合选择器,则会有权重叠加,需要计算权重。计算不进位。

```html
<style>
        li{ color: red; }        /*权重=0,0,0,1*/
        ul li{ color: pink; }    /*权重=0,0,0,1+0,0,0,1=0,0,0,2*/
        .nav li{ color: green; } /*权重=0,0,1,0+0,0,0,1=0,0,1,1*/
</style>
...
<body>
    <ul class="nav">
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
</body>
<!--result : 绿色-->
```

### 5.盒子模型(Box Model)
网页布局过程:\
（1）先准备好相关的网页元素,网页元素基本都是盒子Box。\
（2）利用CSS设置好盒子样式,然后摆放到相应位置。\
（3）往盒子里面装内容.

<img src="https://i.loli.net/2020/08/23/SsnwP6oJmC13VBv.png" width="500px">

#### 5.1边框(border)
##### 5.1.1边框样式
```css
border-width: 5px;
border-style: none | dashed(虚线) | solid(实线) | dotted(点线) | hidden | double | groove | ridge | inset | outset；
border-color：red
/*简写：无顺序写要求*/
border: 1px solid red 
/*分开写边*/
border-top/border-bottom/border-left/border-right:
/*border-collapse属性控制相邻单元格的边框。*/
border-collapse : collapse; /*相邻边框合并在一起/*
```

##### 5.1.2圆角边框
```css
border-radius : length(数值或占高度的百分比);
```

<img src="https://i.loli.net/2020/08/24/zmILhj6sl4BJfG3.png" width="320px">

●如果是正方形,想要设置为一个圆,把数值修改为高度或者宽度的一半即可,或者直接写为50%\
●该属性是一个简写属性，可以跟四个值,分别代表左上角、右上角、右下角、左下角\
●分开写: border-top-left-radius. border-top-right-radius. border-bottom-right-radius 和border- bottom-left- radius

#### 5.2内边距(padding)
```css
padding-top/padding-bottom/padding-left/padding-right
/*复合写法*/
padding: 5px;                /*1个值，代表上下左右都有5像素内边距*/
padding: 5px 10px;           /*2个值，代表上下内边距是5左右内边距是10*/
padding: 5px 10px 20px;      /*3个值，代表上内边距5左右内边距10下内边距20*/
padding: 5px 10px 20px 30px; /*4个值，上5右10下20左30，顺时针*/
```
padding可以做非常巧妙的运用。因为每个导航栏里面的字数不一样多，我们可以不用给每个盒子宽度了,直接给padding最合适。

如果盒子本身没有指定width/height属性,padding不会撑开盒子大小。

#### 5.3外边距(margin)
```css
margin-left/margin-right/margin-top/margin-bottom : px
/*复合写法与padding相同*/
```

##### 5.3.1实现水平居中
外边距可以让块级盒子水平居中,但是必须满足两个条件:\
①盒子必须指定了宽度( width)。\
②盒子左右的外边距都设置为 auto
```css
.one{ 
    width: 960px; 
    margin: O auto; 
}
```
<font size="2">可以写为\
●margin-left: auto; margin-right auto;\
●margin: auto;\
●margin: 0 auto;</font>

上述方法是让块级元素水平居中,行内元素或者行内块元素水平居中给其父元素添加`text-align:center`即可。

##### 5.3.2外边距合并

- 相邻块元素垂直外边距的合井

当上下相邻的两个块元索(兄弟关系)相遇时,如果上面的元素有下外边距margin-bottom,下面的元素有上外边距margin-top , 则他们之间的垂直间距不是margin-bottom+margin-top。取两个值中的较大者。

<img src="https://i.loli.net/2020/08/23/WEucTgDKf6Se7w3.png" width="400px">

解决方案:尽量只给一个盒子添加margin值。

- 嵌套块元素垂直外边距的塌陷

对于两个嵌套关系(父子)的块元索,父元素和子元索都有上外边距,此时父元素会选择值较大的外边距，并且给子元素设置的上外边距无效。

<img src="https://i.loli.net/2020/08/23/PM8fwlLJWHkAVuG.png" width="400px">

解决方案:
```html
<style>
    .father{
        width: 400px;
        height: 400px;
        background-color: purple;
        margin-top: 50px;
        /* ①可以为父元素定义上边框 border: 1px solid transparent;  */
        /* ②可以为父元素定义上内边距 padding: 1px; */
        /* ③可以为父元素添加 overflow:hidden*/
    }
    .son{
        width: 200px;
        height: 200px;
        background-color: pink;
        margin-top: 100px;
    }
</style>
...
<div class="father">
    <div class="son"></div>
</div>
```

##### 5.3.3清除内外边距
网页元素很多都带有默认的内外边距,而且不同浏览器默认的也不一致。 因此我们在布局前,首先要清除下网页元索的内外边距。
```css
*{ /*通配符选择器*/
    padding:0;/*清除内边距*/
    margin:0;/*清除外边距*/
}
```
注意:行内元素为了照顾兼容性,尽量只设置左右内外边距，但转换为块级和行内块元素就可以了


#### 5.4盒子阴影(shadow)
阴影不占空间
```css
box-shadow: h-shadow v-shadow blur(虚实) spread(范围) color(一般有透明度) inset ;
```

<img src="https://i.loli.net/2020/08/24/TmMdWt5BOpUNZvX.png" width="400px">

<font size="2">注：outside不可写</font>
