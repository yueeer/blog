<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## css3进阶总结Ⅰ
学习于黑马程序员pink老师的教程
### 1.CSS3新增选择器
#### 1.1属性选择器
可以根据元素特定属性的来选择元素。这样就可以不用借助于类或者id选择器。

<img src="https://i.loli.net/2020/08/25/nDgIbEZU47e6uMk.png" width="450px">

```html
<style>
        /* 必须是input 但是同时具有 type这个属性 选择这个元素  [] */
        input[type] { color:pink; } 
        /* 只选择 type =text 文本框的input 选取出来 */
        input[type=text] { color: pink; }
        /* 选择首先是div 然后具有class属性 并且属性值必须是icon开头的这些元素 */
        div[class^=icon] { color: red; }
        /* 选择是section 具有class属性 并且属性值必须是data结尾的这些元素 */
        section[class$=data] { color: blue; }
        div.icon1 { color: skyblue; }
        /* 类选择器和 属性选择器 伪类选择器 权重都是 10 */
</style>
...
<body>
    <!-- 1. 不用借助于类或者id选择器 -->
    <!-- <input type="text" value="请输入用户名">
    <input type="text"> -->
    <!-- 2. 可以选择属性=值的某些元素 -->
    <input type="text" name="" id="">
    <input type="password" name="" id="">
    <!-- 3. 可以选择属性值开头的某些元素 -->
    <div class="icon1">小图标1</div>
    <div class="icon2">小图标2</div>
    <div>我是打酱油的</div>
    <!-- 4. 可以选择属性值结尾的某些元素 -->
    <section class="icon1-data">我是安其拉</section>
    <section class="icon3-ico">哪我是谁</section>
</body>
```

#### 1.2结构伪类选择器
主要根据文档结构来选择元素.常用于根据父级选择里面的子元素

<img src="https://i.loli.net/2020/08/25/JT7aiBezKMjuU4I.png" width="450px">

`E:nth-child(n)`选择某个父元素的一个或多个特定的子元素\
●n 可以是数字，关键字和公式\
●n 如果是数字，就是选择第n个子元索，里面数字从1开始...\
●n 可以是关键字: even偶数，odd奇数\
●n 可以是公式：必须是n，从0开始计算,但是第0个元素或者超出了元素的个数会被忽略

```html
<style>
            /* 选择ul里面的第一个li */
            ul li:first-child { background-color: pink; }
            /* 选择ul里面的最后一个li */
            ul li:last-child { background-color: pink; }
            /* 选择ul里面的第2个li */
            ul li:nth-child(2) { background-color: skyblue; }
            /* 把所有的偶数 even的li选出来 */
            ul li:nth-child(even) { background-color: #ccc; }
            /* 所有的偶数/奇数 等价于even/odd */
            ol li:nth-child(2n) { background-color: pink; }
            ol li:nth-child(2n+1) { background-color: skyblue; } 
    </style>
...
<body>
    <ul>
        <li>我是第1个孩子</li>
        <li>我是第2个孩子</li>
        <li>我是第3个孩子</li>
        <li>我是第4个孩子</li>
    </ul>
     <ol>
        <li>我是第1个孩子</li>
        <li>我是第2个孩子</li>
        <li>我是第3个孩子</li>
        <li>我是第4个孩子</li>
    </ol>
</body>
```

<img src="https://i.loli.net/2020/08/25/KnmlFOqTiVcbXaZ.png" width="450px">

nth-child 会把所有的盒子都排列序号，执行的时候首先看`:nth-child(1)`，之后回去看前面 div 。\ 
nth-of-type 会把指定元素的盒子排列序号，执行的时候首先看指定的元素，再看第几个孩子 。

```html
 <style>
        /*没选任何一个*/
        section div:nth-child(1) { background-color: red; }
         /*选择熊大*/
        section div:nth-of-type(1) { background-color: blue; }
    </style>
...
<body>
    <section>
        <p>光头强</p>
        <div>熊大</div>
        <div>熊二</div>
    </section>
</body>
```

#### 1.3伪元素选择器
可以帮助我们利用CSS创建新标签元素,而不需要HTML标签,从而简化HTML结构。新创建的这个元素在文档树中是找不到的，所以我们称为伪元素。
```css
/*before在父元素内容的前面创建块级元素, after在父元素内容的后面插入块级元素*/
element:: befor | after {}
```

<img src="https://i.loli.net/2020/08/25/itTIEx1sUOzofhK.png">

```html
<style>
        div {
            width: 200px;
            height: 200px;
            background-color: pink;
        }
        /* 伪元素选择器和标签选择器一样,权重为1 div::before权重是2 */
        div::before {
            /* before和after必须有content属性，创建一个行内元素  */
            /* display: inline-block; */
            content: '我';
            /* width: 30px;height: 40px;background-color: purple; */
        }
        div::after { content: '小猪佩奇'; }
    </style>
...
<body>
    <div>是</div>
</body>
```

### 2.CSS3盒子模型
可以通过`box-sizing`来指定盒模型,可指定为`content-box` or `border-box`

1.`box-sizing: content-box`盒子大小为<font color="purple">width + padding + border</font> (以前默认的)\
2.`box-sizing: border-box`盒子大小为<font color="purple">width</font>

### 3.CSS3过渡
可以在不使用 Flash 动画或JavaScript的情况下,当元索从一种样式变换为另一种样式时为元索添加效果。

注意：<font color="red">谁变化给谁加</font>
```css
transition: 要过渡的属性 花费时间 运动曲线 何时开始;
```

1.属性:想要变化的CSS属性，宽度高度、背景颜色、内外边距都可以。\
2.花费时间:单位是秒(必须写单位)\
3.运动曲线:默认是ease (可以省略)

<img src="https://i.loli.net/2020/08/25/eo3KEuAnTSrxhHW.png" width="400px">

4.何时开始: 单位是秒(必须写单位)可以设置延迟触发时间，默认是0s (可以省略)

```html
<style>
        div {
            width: 200px;
            height: 100px;
            background-color: pink;
            transition: width .5s ease 0s; 
            /* 如果想要写多个属性，利用逗号进行分割 */
            /* transition: width .5s, height .5s; */
            /* 都变化，属性写all就可以了 */
            /* transition: all 0.5s;*/
        }
        div:hover {
            width: 400px;
            /*height: 200px; background-color: skyblue;*/
        }
    </style>
...
<body><div></div></body>
```

### 4.CSS3其他特性（了解）
#### 4.1图片变模糊  
CSS3滤镜filter将模糊或颜色偏移等图形效果应用于元索。
```css
filter:函数(); 
filter: blur(5px); /*blur模糊处理 数值越大越模糊*/
```

#### 4.2计算盒子宽度
CSS3 calc函数在声明CSS属性值时执行一些计算。
```html
<style>
        .father {
            width: 300px;
            height: 200px;
            background-color: pink;
        }
        .son {
            /*子盒子宽度永远比父盒子小30像素*/
            width: calc(100% - 30px);
            height: 30px;
            background-color: skyblue;
        }
    </style>
...
<body>
    <div class="father">
        <div class="son"></div>
    </div>
</body>
```

