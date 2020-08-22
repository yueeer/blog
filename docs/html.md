<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## HTML基础总结
学习于黑马程序员pink老师的教程

Web标准的构成主要包括结构( Structure)、表现 ( Presentation )和行为( Behavior )三个方面。

| 构成 | 作用 |
|--|--|
| 结构  | 结构用于对网页元素进行整理和分类，现阶段主要学的是HTML. |
| 表现  |  表现用于设置网页元素的版式、颜色、大小等外观样式，主要指的是CSS |
| 行为 |  行为是指网页模型的定义及交互的编写，现阶段主要学的是Javascript |

主要结构

```html
<!DOCTYPE html> <!--文档类型声明标签-->
<html lang="en"> <!--zh-CN定义语言为中文-->>
<head>
    <meta charset="UTF-8"> <!--必须写.采取UTE-8来保存文字-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>利用vscode创建的第一个页面</title>
</head>
<body>
    <h1>标题1</h1>
    <p>段落1</p>
    <p>段落2换行前<br /> 段落2换行后</p>
</body>
```
#### 1.格式标签

| 语义 | 标签 | 说明 |
|--|--|--|
| 加粗 | <strong></strong>或者<b></b>  | 更推荐使用<strong></strong>，语义更强烈|
| 倾斜 | `<em></em>`或者`<i></i>`  | 更推荐使用`<em></em>`，语义更强烈|
| 删除线 | `<del></del>`或者`<b></b>`  | 更推荐使用`<del></del>`，语义更强烈|
| 下划线 | `<ins></ins>`或者`<u></u>`  | 更推荐使用`<ins></ins>`，语义更强烈|

#### 2.图像
```html
<img src="图像的路径" />
```
图像标签的其他属性:

| 属性 |属性值 |说明|
|--|--|--|
| alt | 文本 | 替换文本。图像不能显示的文字|
| title | 文本 | 提示文本。鼠标放到图像上，显示的文字|
| width | 像素 | 只修改一个的话，另一个会等比例缩放|
| height | 像素 | 只修改一个的话，另一个会等比例缩放|
| border | 像素 | 图像边框的粗细|

#### 3.链接
```html
<a href="跳转目标的url地址" target="目标窗口的弹出方式">文本或图像</a>
```
target：_self为默认值，_blank为在新窗口中打开。

1.外部链接:例如`< a href="http:// www.baidu.com">百度</a>`。\
2.内部链接:网站内部页面之间的相互链接, 直接链接内部页面名称即可,例如`<a href= "index.html">颜</a>`.\
3.空链接:如果当时没有确定链接目标时，`<a href="#">首页</a >`\
4.下载链接: 如果href里面地址是一个文件或者压缩包,会下载这个文件,`<a href="package.zip">压缩包</a >`。\
5.网页元素的链接：给图片加超链接`<a href="http://...><img src="img.jpg"/></a>`\
6.锚点链接:点我们点击链接可以快速定位到页面中的某个位置.\
●在链接文本的href属性中,设置属性值为#名字的形式,如`<a href= "#two">第2集</a>`\
●找到目标位置标签,里面添加一个id属性=刚才的名字, 如: `<h3 id="two" >第2集介绍</h3>`\

#### 4.特殊字符

<img src="https://i.loli.net/2020/08/22/4OxtGJpMulY1oz8.png"  width="500px" height="250px">

#### 5.表格
```html
<table>
        <tr>
            <th>A</th><th>B</th><th>C</th>
        </tr>
        <tr>
            <td>单元格内容</td><td>单元格内容</td><td>单元格内容</td>
        </tr>
</table>
```
- 表头单元格

<th>标签(table head的缩写)，表头单元格里面的文本内容加粗居中显示.

- 表格属性 (写在table标签里，实际开发通过CSS来设置.）

|属性名| 属性值| 描述|
|--|--|--|
|align |left. center. right |规定表格相对周围元素的对齐方式。
|border |1或"“ |规定表格单元是否拥有边框，默认为""，表示没有边框
|cellpadding |像素值 |规定单元边沿与其内容之间的空白，默认1像素。
|cellspacing |像素值 |规定单元格之间的空白，默认2像素。
|width |像素值或百分比| 规定表格的宽度。
|height |像素值或百分比| 规定表格的高度。

-  分别用: <thead>标签表格的头部区域、<tbody>标签表格的主体区域.

<img src="https://i.loli.net/2020/08/22/XkDJ8YeTquVdLEx.png"  width="300px" height="150px">

- 合并单元格

<img src="https://i.loli.net/2020/08/22/rEF6cCD1t9T7auI.png"  width="400px" height="120px">

在目标单元格:上写合并代码\
跨行:最上侧单元格为目标单元格；跨列:最左侧单元格为目标单元格

```html
<table border="1" cellspacing="0">
        <tr>
            <th>A</th>
            <th colspan="2">B&nbsp;C</th>
        </tr>
        <tr>
            <td rowspan="2">aaa <br>aaa</td>
            <td>aaa</td>
            <td>aaa</td>
        </tr>
        <tr>
            <td>aaa</td>
            <td>aaa</td>
        </tr>
    </table>
```
#### 6.列表
表格是用来显示数据的,列表是用来布局的。

##### 6.1.无序列表
```html
<ul> <!--ul中只能放li,li中什么都可以放-->
    <li>1</li>
    <li>2</li>
</ul>
```
<img src="https://i.loli.net/2020/08/22/hEdXGokzMstVWI6.png"  width="100px" height="50px">

##### 6.2.有序列表
```html
<ol>
     <li>1</li>
     <li>2</li>
</ol>
```
<img src="https://i.loli.net/2020/08/22/ZLTqmn3tRj8p1lU.png"  width="80px" height="50px">

##### 6.3.自定义列表
`<dl>` 标签用于定义描述列表(或定义列表) , 该标签会与`<dt>` ( 定义项目/名字)和`<dd>` (描述每一个项目名字) 一起使用。

```html
<dl>
        <dt>关注我们</dt>
        <dd>新浪微博</dd>
        <dd>官方微信</dd>
</dl>
```
<img src="https://i.loli.net/2020/08/22/euX9scho6KZRBtQ.png"  width="100px" height="50px">

#### 7.表单
一个完整的表单通常由表单域、表单控件(也称为表单元素)和提示信息3个部分构成。

- 表单域是一个包含表单元素的区域。

`<form>` 标签用于定义表单域,把它范围内的表单元素信息提交给服务器，以实现用户信息的收集和传递。

```html
<form action="ulr地址" method="提交方式" name="表单域名称">
   各种控件
</form>
```
action : url地址  用于指定接收并处理表单数据的服务器程序的url地址。\
method: get/post  用于设置表单数据的提交方式\
name: 用于指定表单的名称，以区分同一个页面中的多个表单域。

- 表单元素

`<input>`输入表单元素，包含一个type属性,根据不同的type,输入字段拥有很多种形式。

```html
<input type="属性值" />
```

<img src="https://i.loli.net/2020/08/22/4XKqHxkPEGct7a5.png"  width="500px" height="300px">

其他属性

<img src="https://i.loli.net/2020/08/22/dSylUirzAuIm6xs.png"  width="500px" height="130px">

<font size=2>name和value是每个表单元素都有的属性值,name在后端有用，value在前端展示</font>

```html
<label for="man">男</label> <input type="radio" name="sex" value="男" id="man" checked="checked"> <label for="woman">女</label> <input type="radio" name="sex" value="女" id="woman"><br>
<!--<label>标签用于绑定一个表单元素 当点击<label>标签内的文本时,浏览器就会自动将焦点(光标)转到或者选择对应的表单元素上来增加用户体验.（for和id内容相同）-->

姓名：<input type="text" name="username" value="请输入用户名" maxlength="5"><br>

<input type="submit" name="submit" value="免费注册">

<input type="reset">

<input type="file">

password: <input type="password"></input><br>

hobbies: read<input type="checkbox" name="read" id="阅读"><br>
football <input type="checkbox" name="football" id="足球"><br>
dance <input type="checkbox" name="dance" id="跳舞"><br>
```

<img src="https://i.loli.net/2020/08/22/HJchtGOUZyAYNqE.png"  width="500px" height="100px">

`<select>`下拉表单元素

```html
 <select>
    <option selected="selected">A</option> <!--默认选项-->
    <option>B</option>
    <option>C</option>
</select>
```

`<textarea>`文本域元素 定义多行文本输入

```html
<textarea rows="3" cols="20">默认文字</textarea>
```

<img src="https://i.loli.net/2020/08/22/1lvAMEmswWIrTqO.png"  width="150px" height="70px">
