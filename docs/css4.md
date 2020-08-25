<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## CSS基础总结Ⅳ
学习于黑马程序员pink老师的教程
### 1.精灵图
为了有效地减少服务器接收和发送请求的次数，提高页面的加载速度，出现了CSS精灵技术(也称CSS Sprites、CSS雪碧)。

<img src="https://i.loli.net/2020/08/24/N92SaZbYF6wW7EJ.png" width="350px">

使用精灵图核心:\
1.精灵技术主要针对于背景图片使用。就是把多个小背景图片整合到一张大图片中。\
2.这个大图片也称为sprites精灵图或者雪碧图。\
3.移动背景图片位置，此时可以使用background-position。\
4.移动的距离就是这个目标图片的x和y坐标。注意网页中的坐标有所不同，向左向上移动是负值。

<img src="https://i.loli.net/2020/08/24/SmqIgxDp5vFriy6.png" width="150px">

```html
<style>
    .box1{
        width: 60px;
        height: 60px;
        margin: 100px auto;
        background: url(image/sprites.png);
        background-position: -182px 0; /*背景图片左移182px*/
        /*可直接写 background: url(image/sprites.png) no-repeat -182px 0;*/
    }
</style>
...
<body>
    <div class="box1"></div>
</body>
```

精灵图是有诸多优点的,但是缺点很明显。\
1.图片文件还是比较大的。\
2.图片本身放大和缩小会失真。\
3.一旦图片制作完毕想要更换非常复杂。

### 2.字体图标

字体图标主要用于显示网页中通用、常用的一些小图标。展示的是图标,本质属于字体。

优点：\
1.轻量级:一个图标字体要比一系列的图像要小。字体加载了,图标就会马上渲染出来\
2.灵活性:本质是文字,可以随意改变颜色、产生阴影、透明效果、 旋转等\
3.兼容性:几乎支持所有的浏览器

<font color="red">结构和样式比较简单的小图标,就用字体图标；复杂点的小图片,就用精灵图。</font>

#### 2.1字体图标的下载
icomoon字库https://icomoon.io\
阿里iconfont字库https://www.iconfont.cn/

#### 2.2字体图标的引入htm页面中
1.把下载包里面的fonts文件夹放入页面根目录下\
2.把字体文件通过css引入到页面中
```html
<style>
    @font-face {
      font-family: 'icomoon';
      src:  url('fonts/icomoon.eot?p4ssmb');
      src:  url('fonts/icomoon.eot?p4ssmb#iefix') format('embedded-opentype'),
            url('fonts/icomoon.ttf?p4ssmb') format('truetype'),
            url('fonts/icomoon.woff?p4ssmb') format('woff'),
            url('fonts/icomoon.svg?p4ssmb#icomoon') format('svg');
      font-weight: normal;
     font-style: normal;
     font-display: block;
}
span {
    font-family: 'icomoon' ;
}
</style>
...
<span></span>
```

#### 2.3字体图标的追加
把压缩包里面的selection.json重新上传,选中自己想要新的图标,重新下载压缩包,并替换原来的文件。

### 3.CSS三角
#### 3.1三角写法
```html
<style>
    .box1 {
        width: 0;
        height: 0;
        /* border: 10px solid pink; */
        border-top: 10px solid pink;
        border-right: 10px solid red;
        border-bottom: 10px solid blue;
        border-left: 10px solid green;
    }
    .box2 {
        width: 0;
        height: 0;
        /* 为了照顾兼容性
        line-height: 0;  
        font-size: 0; */
        border: 50px solid transparent; /*50px调节粗细即三角大小*/
        border-left-color: pink;
        margin: 100px auto;
    }
</style>
...
<body>
    <div class="box1"></div>
    <div class="box2"></div>
</body>
```

<img src="https://i.loli.net/2020/08/24/Dpxyo39eAzdHgMS.png" width="200px">

#### 3.2三角强化

```css
.box1 {
        width: 0;
        height: 0;
        /* 把上边框宽度调大，颜色调为透明 */
        border-top: 100px solid transparent;
        /* 只保留右边的边框有颜色 */
        border-right: 50px solid skyblue; */
        /* 左边和下边的边框宽度设置为0 */
        border-bottom: 0 solid blue;
       border-left: 0 solid green; 
}
```

<img src="https://i.loli.net/2020/08/24/FmqMApCZQdRyiBe.png" width="300px">

等价于
```css
.box1 {
        width: 0;
        height: 0;
        /* 只保留右边的边框有颜色 */
        border-color: transparent red transparent transparent;
        /* 样式都是solid */
        border-style: solid;
        /* 3上边框宽度要大， 右边框宽度稍小， 其余的边框该为 0 */
        border-width: 100px 50px 0 0 ;
}
```

### 4.CSS用户界面样式
#### 4.1更改用户的鼠标样式
```css
li { cursor: move; } /*十字架形状*/
```

<img src="https://i.loli.net/2020/08/24/aWN9wokpBjFIg6X.png" width="500px">

#### 4.2取消表单轮廓(去掉默认的蓝色边框)
```html
<style>
    input{
        outline: none; /*或0*/
    }
</style>
...
<body><input type="text"></body>
```

#### 4.3防止文本域拖拽改变大小
```html
<style>
    textarea{ 
        resize: none; 
    }
</style>
...
<body>
    /*textarea最好写在一行*/
    <textarea name="" id="" cols="30" rows="10"></textarea>
</body>
```

### 5.vertical-align属性应用
#### 5.1用于设置图片或者表单(行内块元索或行内元素)和文字垂直对齐。
```css
vertical-align: baseline | top | middle | bottom
```
<img src="https://i.loli.net/2020/08/24/ijguAYqZkfLKQrS.png" width="600px">

<img src="https://i.loli.net/2020/08/24/4tnT73WajA6hs9N.png" width="550px">

<img src="https://i.loli.net/2020/08/24/hlJNnt5FTzabIcg.png" width="650px">

#### 5.2解决图片底部默认空白缝隙问题

<img src="https://i.loli.net/2020/08/24/CfZ4qGJl6pKmWOQ.png" width="">

给图片添加`vertical-align: middle | top | bottom`等(提倡使用)。或者把图片转换为块级元素。
```html
<style>
    div{ border: 2px solid red }
    img{ 
        vertical-align: middle/top/bottom; 
        /*或 display: block;*/
    }
</style>
...
<div>
    <img src="imges/ldh.jpg" alt="">
</div>
```

### 6.溢出文字的省略号显示
#### 6.1单行文本溢出显示省略号
```css
/*1.先强制一行内显示文本，默认normal自动换行*/
white-space: nowrap; 
/*2.超出的部分隐藏*/
overflow: hidden;
/*3.文字用省略号替代超出的部分*/
text-overflow: ellipsis; 
```

#### 6.2多行文本溢出显示省略号（有比较大的兼容性问题）
```css
overflow: hidden;
text-overflow: ellipsis;
/*弹性伸缩盒子模型显示*/
display: -webkit-box;
/*限制在一个块元素显示的文本的行数*/
-webkit-line-clamp: 2; /*第二行显示省略号*/
/*设置或检索伸缩盒对象的子元素的排列方式*/
-webkit-box-orient: vertical; /*垂直居中*/
```

### 7.常见布局技巧
#### 7.1margin负值的运用
原始

<img src="https://i.loli.net/2020/08/24/Kzver79hj2PToI1.png" width="400px">

```css
ul li {
            float: left;
            list-style: none;
            width: 150px;
            height: 200px;
            border: 1px solid red;
            margin-left: -1px;
        }
```

<img src="https://i.loli.net/2020/08/24/7lzxUikNFqPQTbe.png" width="400px">

#### 7.2文字围绕浮动元素
巧妙运用浮动元素不会压住文字的特性。

#### 7.3行内块的巧妙运用
父盒子`text-align: center;`居中，则父盒子内的行内块元素一起居中