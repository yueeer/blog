<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## CSS基础总结Ⅰ

CSS主要用于设置HTML页面中的**文本内容**(字体、大小对齐方式等)、**图片的外形**(宽高、边框样式、边距等)以及**版面的布局**和**外观显示样式**。

### 1.CSS语法规范
CSS规则由两个主要的部分构成:选择器以及一条或多条声明。
<img src="http://s54.99854.men/2020/08/23/a18e408de8ee77096fba1a60d8b3d5b4.png" width="300px" height="100px">
### 2.CSS选择器
选择器(选择符)就是根据不同需求把不同的标签选出来。简单来说 ,就是选择标签用的。

选择器分为基础选择器和复合选择器。基础选择器是由单个选择器组成的，又包括:标签选择器、类选择器、id选择器和通配符选择器

#### 2.1基础选择器
##### 2.1.1标签选择器(元素选择器)
用HTML标签名称作为选择器,为页面中某一类标签指定统一的CSS样式。（全部）

```html
<!DOCTYPE html>
<html lang="en">
<head>
   ...
    <style>
        /* 给谁改样式,即HTML标签{改什么样式} */
        p {
            color: red;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <p>尝试使用css</p>
</body>
</html>
```
##### 2.1.2类选择器
如果想要差异化选择不同的标签,单独选一个或者某几个标签 ,可以使用类选择器。

```html
<style>
·类名{属性1：属性值1；} /* ·red {color: red;} */
</style>
...
<div class='类名'></div>
<!--<div class='red'>变红色</div>-->
```
我们可以给一个标签指定多个类名,这些类名都可以选出这个标签. 多类名之间空格分开。
##### 2.1.3id选择器
id选择器可以为标有特定id的HTML元素指定特定的样式。（只能调用一次）id选择器以"#" 来定义。

```html
<style>
#id名{属性1：属性值1；} /* #red {color: red;} */
</style>
...
<div id='id名'></div>
<!--<div id='red'>变红色</div>-->
```
类选择器在修改样式中用的最多, id选择器一般用于页面唯一性的元素上,经常和JavaScript搭配使用。
##### 2.1.4通配符选择器
选取页面中所有元素（标签），不需要调用

```html
<style>
*{属性1：属性值1；} /* *{color: red;} */
</style>
```
<img src="http://s55.99854.men/2020/08/23/2f98a367bfb6878556e603450b30ea23.png" width="500px" height="180px">

#### 2.2复合选择器
##### 2.2.1后代选择器(包含选择器)
可以选择父元索里面子元素。其写法就是把外层标签写在前面,内层标签写在后面,中间用空格分隔。

```html
<head>
    <style>
        ol li {color: red;} /*父元素 待改后代元素 {样式}*/
        .nav li a {color: yellow;}
    </style>
</head>
<body>
    <ol>
        <li>我是ol的孩子</li>
        <li>我是ol的孩子</li>
    </ol>
    <ul>
        <li>我是ul的孩子</li>
        <li>我是ol的孩子</li>
    </ul>
    <ol class="nav">
        <li>我是ol的孩子</li>
        <li>我是ol的孩子</li>
        <li><a href="#">我是孙子</a></li>
    </ol>
</body>
```
##### 2.2.2子选择器
只能选择作为元素的最近一级子元素。 简单理解就是选亲儿子元素.

```
父元素 > 子元素 {样式声明}
```
##### 2.2.3并集选择器
可以选择多组标签同时为他们定义相同的样式。通常用于集体声明，任何形式的选择器都可以作为并集选择器的一部分。

```
元素1, 元素2，..., 元素n {样式声明}
```
##### 2.2.4伪类选择器
用于向某些选择器添加特殊的效果,比如给链接添加特殊效果,或选择第1个,第n个元素。用冒号(:)示

- 链接伪类

```
a:link /*选择所有未被访问的链接*/
a:visited /*选择所有己被访问的链接*/
a:hover /*选择鼠标指针位于其上的链接*/
a:active /*选择活动链接(鼠标按下未弹起的链接)*/
```
为了确保生效,请按照LVHA的循顺序声明。\
因为a链接在浏览器中具有默认样式,所以我们实际工作中都需要给链接单独指定样式。
实际开发常用写法：

```css
/* 所有的链接 */
a{
    color: gray;
    text-decoration: none;
}
/* 鼠标经过 */
a:hover { color: red; }
```
- focus伪类

用于选取获得焦点的表单元素。焦点就是光标，一般情况`<input>`类表单元素才能获取。

```html
<type>
input:focus { background-color: yel1ow;}
</type>
...
<body>
    <input type="txt">
    <input type="txt">
</body>
```
<img src="https://i.loli.net/2020/08/23/4nhPmp3lCsVXKT6.png" width="500px" height="200px">

### 3.CSS属性
#### 3.1字体

<img src="https://i.loli.net/2020/08/23/8oZlAW6YQB4d9yu.png" width="520px" height="160px">

```css
p {
    font-family:"微软雅黑";
    font-size: 20px;
    font-weight: 700/bold|400/normal;/*无px*/
    font-style: normal/italic;
}
div {font-family:Arical,"Microsoft Yahei";} /*按从前往后的顺序搜索是否有*/
p {font: font-style font-weight font-size/line-height font-family;}
```
字体颜色
```
color: 颜色属性值
```
<img src="https://i.loli.net/2020/08/23/p2u8kjKGZdtAQoS.png" width="450px" height="110px">

#### 3.2文本

text-align属性用于设置元素内文本内容的水平对齐方式。\
text-decoration属性规定添加到文本的修饰。可以给文本添加下划线、删除线、上划线等。\
text-indent属性用来指定文本的第一行的缩进,通常是将段落的首行缩进(可以是负数)。em是一个相对单位，是当前元索1个文字的大小。\
line-height属性用于设置行间的距离(行高=上间距+文本高度+下间距)。\
text-shadow: 属性用于设置文本阴影，h-shadow水平阴影位置、v-shadow垂直阴影位置、blur虚实。
```css
div {
    text-align :center/left/right;
    text-decoration: none/underline/overline/line-through;
    text-indent: 20px/2em;
    line-height: 26px;
    text-shadow: h-shadow(px) V-shadow(px) blur(px) color ;
}
```

### 4.CSS引入方式
按照CSS样式书写的位置(或者引入的方式) , CSS样式表可以分为三大类。
#### 4.1内部样式表(嵌入式)
写到htm|页面内部,可以方便控制当前整个页面中的元素样式设置。\
是将所有的CSS代码抽取出来,单独放到`<style>`标签中，`<style>`一般放在`<head>`中。
#### 4.2行内样式表(行内式)
是在元素标签内部的style属性中设定CSS样式。适合于修改简单样式
```html
<div style="color: pink; font-size: 12px;">lalalal</div>
```
#### 4.3外部样式表(链接式)
实际开发都是外部样式表，适合于样式比较多的情况。样式单独写到CSS文件中,之后把CSS文件引入到HTML页面中使用.

(1)创建css文件，文件中只有样式没有标签\
(2)在HTML页面中,在`<head>`中使用`<link>`标签引入这个文件。
```html
<link rel=" stylesheet" href="css文件路径">
```
