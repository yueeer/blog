<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 网站制作
学习于黑马程序员pink老师的教程

### 1.网站制作流程
1.客户沟通，指定方案\
2.签订合同，预付定金\
3.初稿审核（网页美工会制作原型图和psd效果图）\
4.前台页面设计，后台功能开发\
5.测试验收\
6.上线培训\
7.后期维护

### 2.网站favicon图标
#### 2.1制作favicon图标
1.把图标切成png图片。\
2.把png图片转换为ico图标,这需要借助于第三方转换网站,例如: http://www.bitbug.net/
#### 2.2favicon图标放到网站根目录下
#### 2.3HTML页面引入favicon图标
```html
<head>
    <link rel="shortcut icon" href="favicon.ico" >
</head>
```

### 3.SEO优化
#### 3.1网站TDK三大标签SEO优化
网站TDK：title、description、keywords\
SEO (Search Engine Optimization )搜索引擎优化：是一种利用搜索引擎的规则提高网站在有关搜索引擎内自然排名的方式。\
页面的三大标签用来符合SEO优化

##### 3.1.1 title 网站标题
重要标签，是搜索引擎了解网页的入口和对网页主题归属的最佳判断点。\
建议:网站名(产品名)-网站的介绍(尽量不要超过30个汉字)
```html
<title>...</title>
```

##### 3.1.2 description网站说明
作为网站的总体业务和主题概括,多采用“我们.."、“我们提供.." 、"xxx网作为.."之类语句。
```html
<meta name="description" content="..." >
```

##### 3.1.3 keywords关键字
最好限制为6~8个关键词,关键词之间用英文逗号隔开
```html
<meta name="keywords" content="..." >
```

#### 3.2 LOGO SEO优化
1.logo 里面首先放一个h1标签,目的是为了提权,告诉搜索引擎, 这个地方很重要。\
2.h1里面再放一个链接，可以返回首页的,把logo的背景图片给链接即可。\
3.为了搜索引擎收录我们,我们链接里面要放文字(网站名称) , 但是文字不要显示出来。\
    ●方法1: 将文字移到盒子外面( `text-indent: -9999px`) ,然后隐藏（ `overflow:hidden`），淘宝的做法。\
    ●方法2:直接给`font-size:0;`，就看不到文字了,京东的做法。\
4.最后给链接一个title属性,这样鼠标放到logo上就可以看到提示文字了。
```html
<style>
    .logo a {
        display: block;
        width: ;
        height: ;
        background: url(../images/logo.png) no-repeat;
        /* font-size: 0;京东的做法*/
        /* 淘宝的做法让文字隐藏 */
        text-indent: -9999px;
        overflow: hidden;
    }
</style>
 ...
 <div class="logo">
      <h1>
            <a href="index.html" title="品优购商城">品优购商城</a>
      </h1>
</div>
```

ps:注册页面比较隐私,为保护用户信息,不需要做SEO优化。

### 4.常用的模块类命名

 名称 | 说明 
--|-- 
 快捷导航栏 | shortcut 
 头部 | header
 标志 | logo
 搜紊 | search
 热点词 | hotwords
 导航 | nav
 页面底部 | footer

### 5.将自己的网站上传到远程服务器
