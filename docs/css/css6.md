<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## css3进阶总结Ⅱ
学习于黑马程序员pink老师的教程
### 1.2D转换(transform)
转换(transform)可以实现元素的位移(translate)、旋转(rotate)、缩放(scale)等效果。

<img src="https://i.loli.net/2020/08/24/3ZbRqfXpz7QGJjK.png" width="300px">

#### 1.1移动(translate)

```css
transform: translate(x,y); 
/*或者分开写*/
transform: translateX(n) ;
transform: translateY(n) ;
/*只移动x*/
transform: translate(x,0); 
transform: translateX(x);
/*只移动y*/
transform: translate(0,y); 
transform: translateY(y);
```
translate最大的优点:不会影响到其他元素的位置\
translate中的百分比单位是相对于自身的宽度和高度。`translate:(50%,50%);`常用于实现盒子居中\
对行内标签没有效果

#### 1.2旋转(rotate)
```css
transform:rotate (度数)
```
rotate里面跟度数，单位是deg比如`transform:rotate(45deg)`。角度为正时,顺时针,负时,为逆时针。

默认旋转的中心点是元素的中心点，设置元素转换的中心点：
```css
transform-origin: x(px) y(px);
transform-origin: left bottom;/*设置左下角为中心点*/
```
可以给x y设置方位名词( top bottom left right center)，默认50%  50%  等价于 center  center 

#### 1.3缩放(scale)
```css
transform: scale(x,y) ;
```
`transform:scale(2)` : 只写一个参数，两个参数一 样,相当于scale(2,2)，放大两倍\
`transform:scale(0.5,0.5)` :缩小\
scale缩放最大的优势:默认以中心点缩放的，而且不影响其他盒子。\
可以用transform-origin设置转换中心点缩放。

#### 1.4综合写法
```css
transform: translate() rotate() scale() 
```
顺序会影转换的效果( 改变坐标轴方向)。同时有位移和其他属性的时候,要将位移放到最前。

### 2.CSS3动画
#### 2.1用keyframes定义动画
```css
@keyframes 动画名称{
    0%{ 
        width: 100px;
    }
    100%{
        width: 200px;
    }
}
```

可以改变任意多的样式任意多的次数。\
用百分比来规定变化发生的时间,百分比就是总的时间的划分，或用关键词"from"和"to" ,等同于0%和100%。

#### 2.2元素使用动画
```css
div {
    width: 200px;
    height: 200px;
    background-color: aqua; 
    margin: 100px auto;
    /*调用动画,可以添加多个动画，用逗号分隔*/
    animation-name:动画名称;
    /** 持续时间*/
    animation-duration:持续时间;
}
```

#### 2.3动画常用属性

<img src="https://i.loli.net/2020/08/25/qMz9hJZKCuBLsli.png" width="600px">

简写属性（前面2个属性 name  duration 一定要写）
```css
animation :动画名称 持续时间 运动曲线 何时开始 播放次数 是否反方向 动画起始或者结束的状态;
```

animation-timing-function :\
<img src="https://i.loli.net/2020/08/25/tAyBaiG37mLIjWT.png" width="550px">

### 3.3D转换

<img src="https://i.loli.net/2020/08/25/PNw2TIuHslCbpXV.png" width="300px" height="250px">

#### 3.1 3D位移
```css
transform: translateX(100px) /*在x轴上移动*/
transform: translateY(100px) /*在Y轴上移动*/
transform: translateZ(100px) /*在Z轴上移动(translateZ-般用px单位 )*/
transform: translate3d(x,y,z)
/*= transform: translateX(x) translateY(y) translateZ(z)*/
```
<font size="2">xyz是不能省略的，如果没有就写0。</font>

#### 3.2透视
如果想要在网页产生3D效果，需要透视\
透视也称为视距d，是人的眼睛到屏幕的距离。距离视觉点越近的在电脑平面成像越大,越远成像越小。\
z:就是z轴,物体距离屏幕的距离, z轴越大(正值)，我们看到的物体就越大。

<img src="https://i.loli.net/2020/08/25/6nvAj9RrBc8hxQL.png" width="300px">

透视写在被观察元索的父盒子上,但是影响的是子盒子
```html
<style>
    body {      
            perspective: 200px; /*透视的单位是像素*/
    }
    div {
            width: 200px;
            height: 200px;
            background-color: pink;
            transform: translate3d(400px, 100px, 100px);
        }
</style>
...
<body>
    <div></div>
</body>
```

#### 3.3 3D旋转
```css
transform: rotateX(45deg) /*沿着x轴正方向旋转45度*/
transform: rotateY(45deg) /*沿着y轴正方向旋转45deg*/
transform: rotateZ(45deg) /*沿着Z轴正方向旋转45deg*/
transform: rotate3d(x,y,z,deg) /*沿着自定义轴旋转deg角度*/
```

#### 3.4 3D呈现左手准则
<font color="red">左手准则</font>\
●左手的手拇指指向 x轴(yz)的正方向\
●其余手指的弯曲方向就是该元素沿着x轴(yz)旋转的方向

控制子元索是否开启三维立体环境。
```css
transform-style: flat;/*子元素不开启3d立体空间,默认的*/
transform-style: preserve-3d;/*子元素开启立体空间*/
```

### 4.浏览器私有前缀
是为了兼容老版本的写法,比较新版本的浏览器无须添加。

-moz- :代表firefox浏览器私有属性\
-ms- :代表ie浏览器私有属性\
-webkit- :代表safari、老版本chrome 私有属性\
-o-:代表Opera私有属性

以radius为例
```css
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
-o-border-radius: 10px;
border-radius: 10px;
```