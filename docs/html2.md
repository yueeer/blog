<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## HTML5的新特性
学习于黑马程序员pink老师的教程
### 1.HTML5新增的语义化标签
`<header>` :头部标签\
`<nav>`:导航标签\
`<article>` :内容标签\
`<section>` :定义文档某个区域\
`<aside>` :侧边栏标签\
`<footer>` :尾部标签

<img src="https://i.loli.net/2020/08/24/DBwWAoQMVRSsilk.png" width="400px">

注意:\
●这种语义化标准主要是针对搜索引擎、移动端的\
●这些新标签页面中可以使用多次\
●在IE9中,需要把这些元素转换为块级元素

### 2.HTML5新增的多媒体标签
#### 2.1音频(audio)

<img src="https://i.loli.net/2020/08/24/8FPVKWDbZhswxHe.png" width="600px">

```html
<audio src="文件地址" 属性值></audio>
/*为了兼容*/
<audio 属性值>
    <source src="文件地址" type="audio/mpeg">
    <source src="文件地址" type="audio/ogg">
</audio>
```

<img src="https://i.loli.net/2020/08/24/a5C3g8r7bJpFUMI.png" width="530px">

#### 2.2视频(video)

<img src="https://i.loli.net/2020/08/24/gXnI3qFCjoyedEa.png" width="580px">

```html
<video src="文件地址" 属性值></video>
/*为了兼容*/
<video 属性值>
    <source src="文件地址" type="video/mp4">
    <source src="文件地址" type="video/ogg">
</video>
```

<img src="https://i.loli.net/2020/08/24/9wI2aui7UGApYDQ.png" width="530px">

示例：
```html
 <video src="media/mi.mp4" autoplay="autoplay" muted="muted"  loop="loop" poster="media/mi9.jpg"></video>
 ```

### 3.HTML5新增的input类型

<img src="https://i.loli.net/2020/08/24/IYZCjihJ9Km6pdg.png" width="500px">

```html
<body>
    <!-- 我们验证的时候必须添加form表单域 -->
    <form action="">
        <ul>
            <li>邮箱: <input type="email" ></li>
            <li>网址: <input type="url" ></li>
            <li>日期: <input type="date" ></li>
            <li>时间: <input type="time" ></li>
            <li>数量: <input type="number" ></li>
           <li>手机号码: <input type="tel" ></li>
           <li>搜索: <input type="search" ></li>
           <li>颜色: <input type="color" ></li>
           <!-- 当我们点击提交按钮就可以验证表单了 -->
           <li> <input type="submit" value="提交"></li>
        </ul>
    </form>
</body>
```
<img src="https://i.loli.net/2020/08/24/OhvtmZVxXGD49kA.png" width="300px">

### 4.HTML5新增的表单属性

<img src="https://i.loli.net/2020/08/24/kYEuxrpdaQ6TBKm.png" width="550px">

```html
 <style>
        input::placeholder {
            color: pink;
        }
    </style>
...
<body>
    <form action="">
            <input type="search" name="sear" id="" required="required" placeholder="pink老师" autofocus="autofocus" autocomplete="off">
            <input type="file" name="" id="" multiple="multiple">
            <input type="submit" value="提交">
    </form>
</body>
```

<img src="https://i.loli.net/2020/08/24/v9HNjRfaZLpiOuK.png" width="450px">
