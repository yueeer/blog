<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## Latex排版教程

#### 1. Latex源文件的基本结构

```latex
% 导言区 用于全局设置
\documentclass{article} % book, report, letter

\usepackage{ctex} %中文

\title{My First Document}
\author{ZhangYue}
\date{\today}

% 正文区
\begin{document}
    \maketitle %输出标题
    Hello World!
\end{document}
```

#### 2. 大纲目录

`\section{}` 一级标题, `\subsection{}` 二级标题，`\subsubsection{}` 三级标题\
空行和`\par`用于分割段落，`\\` 用于换行，`\par` 也用于换行,`\newpage`和`\clearpage`用于分页，注意命令与文字之间用空格间隔\
`\chapter{}` 章节大纲\
`\tableofcentonts` 生成目录

#### 3. 文字设置

##### 3.1字体族设置

###### 3.1.1英文
罗马字体、无衬线字体、打字机字体

```latex
\textrm{Roman Family}%在花括号内的字体都是罗马字体
\textsf{Sans Serif Family}
\texttt{Typewriter Family}

{ %括号限制作用范围
\rmfamily Roman Family\\
Xiamen, located in Fujian province, is a famous coastal city. It's not only renowned for its natural beauty, but also for its modernization.
}

\sffamily Sans Serif Family %该命令下面的字体都是是无衬线字体字体，直到新的声明出现覆盖该声明。

{\ttfamily Typewriter Family\\
As far as I'm concerned, Xiamen is very clean and pretty. In that city, we can enjoy clear sky, beautiful sea, and green tropical plants. I guess living there must be very pleasant.
}
```

<img src="https://i.loli.net/2021/01/07/fGAHmrVcIBtebUQ.png" width="520" height="180" align="center">

###### 3.1.2中文
```latex
{\songti 宋体}
{\heiti 黑体}
{\fangsong 仿宋}
{\kaishu 楷书}
```
<img src="https://i.loli.net/2021/01/07/Si71nIsl4v9dcfO.png" width="520" height="110" align="center">

##### 3.2字体粗细宽度设置

```latex
\textmd{Medium Series}
\textbf{Boldface Series}

{\mdseries Medium Series}
{\bfseries Boldface Series}
```
##### 3.3 字体形状设置
直立、斜体、伪斜体、大小写
```latex
\textup{Upright Shape}
\textit{Italic Shape}
\textsl{Slanted Shape}
\textsc{Small Caps Shape}

\upshape Upright Shape
\itshape Italic Shape
\slshape Slanted Shape
\scshape Small Caps Shape
```

<img src="https://i.loli.net/2021/01/07/HFlacOBCNpIjRSi.png" width="400" height="150" align="center">

##### 3.4字体大小设置
与文档相对
###### 3.4.1英文
```latex
{\tiny hello}\\
{\scriptsize hello}\\
{\footnotesize hello}\\
{\small hello}\\
{\normalsize hello}\\
{\large hello}\\
{\Large hello}\\
{\LARGE hello}\\
{\huge hello}\\
{\Huge hello}
```
<img src="https://i.loli.net/2021/01/07/rBqynTmDHOF3Law.png" width="420" height="260" align="center">

###### 3.4.2中文
```latex
\subsection{中文字号}
\zihao{-0} 你好\\
\zihao{5} 你好
```
<img src="https://i.loli.net/2021/01/07/v4SyfTIVB6rxphm.png" width="320" height="280" align="center">

#### 4. 特殊字符

空白字符
- 英文多个空格，当作一个空格处理
- 中英文混合时，自动产生空格间隔
- 中文空格`~`
```latex
a\quad b % 1em(当前字体一个M的大小)
a\qquad b % 2em
a\, b 或者 a\thinspace b % 1/6的个em
a\enspace b % 0.5em
```
控制符
```latex
%转义字符 其中‘\’ 用\textbackslash
\# \$ \% \{ \} \~{} \_{} \^{} \& \textbackslash
```
引号
```latex
` ' %单引号
`` " %双引号
```
<img src="https://i.loli.net/2021/01/07/v5jDadpKiTJ8cyH.png" width="400" height="80" align="center">

博客[《LaTeX学习系列之---LaTeX的特殊字符》](https://www.jianshu.com/p/5250a4625dfb)总结的很详细

#### 5. 插入图片
##### 5.1普通插图
```latex
\usepackage{graphicx} %导入图片的宏包
\graphicspath{{figures/},{pics/}} %图片搜索路径

%includegraphics[<选项>]{<文件名>}
%格式：EPS PDF PNG JPEG BMP
\includegraphics[scale=0.1]{IMG_1148}
```
`scale=0.3` 设置缩放比例\
`height=3cm` 设置图片的高度\
`width=100pt` 设置图片的宽度\
`height=1\textheight` 设置图片的相对高度\
`width=1\textwidth` 设置图片的相对宽度
`angle=-45` 设置角度\
同时设置多个参数时，用","进行分割
##### 5.2浮动体环境
浮动体就是会移动的文本框
```latex
如图\ref{fig:fig-fudong}所示 %交叉引用

\begin{figure}[htbp]
	\centering %居中排版
	\includegraphics[scale=0.1]{IMG_1148.JPG}
  %标题和标签
	\caption{浮动图}\label{fig:fig-fudong}
\end{figure}
```
`\ref`交叉引用可以用于公式，表格，图片\
`h`：此处（here）-代码所在的上下文\
`t`：页顶（top）-代码所在页的顶部或者之后页的顶部\
`b`：底页（botton）-代码所页的底部，或者下一页的底部\
`p`：独立的一页（page）-浮动页面

#### 6. 表格插入
可以通过使用<font color=purple>Excel2LaTeX</font>工具，将excel表格快速转化为latex代码。打开Excel后，双击“Excel2LaTex.xla”，选择“启用宏”即可加载。

<img src="https://i.loli.net/2021/01/08/UueH6htK4AnoylE.png" width="400" height="200" align="center">

##### 6.1普通插表
设置宽度：p{宽度值},内容超过宽度时，自动换行
```latex
\begin{tabular}{l|c c c||r} %l 左, c 居中, r 对齐; | 竖线, || 双竖线
		1 & 2 & 33333333333333 & 4 & 5\\
		1 & 2 & 3 & 4 & 5\\
		\hline        %横线
		1 & 2 & 3 & 4 & 5\\
		\hline \hline %双横线
		1 & 2 & 3 & 4 & 5\\
		1 & 2 & 3 & 4 & 5
\end{tabular}
```
<img src="https://i.loli.net/2021/01/07/GQvwR7hctLlYF5q.png" width="250" height="100" align="center">

##### 6.2浮动体环境
```latex
\usepackage{bigstrut,multirow,rotating}
\usepackage{booktabs}
\usepackage[table ]{ xcolor}

\begin{table}[htbp]
	\centering
	\begin{tabular}{lrrrr}
	\toprule
			& \multicolumn{2}{c}{a} & \multicolumn{2}{c}{b} \\
			& \multicolumn{1}{l}{type1} & \multicolumn{1}{l}{type2} & \multicolumn{1}{l}{type3} & \multicolumn{1}{l}{type4} \\
	\midrule
	sn    & 2.35  & 2.69  & 7.34  & 5.48 \\
	sp    & 6.32  & 5.32  & 9.13  & 7.46 \\
	\bottomrule
	\end{tabular}%
	\caption{Add caption1}\label{tab:addlabel1}
\end{table}%


\begin{table}[htbp]
	\centering
	\begin{tabular}{crrrrr}
	\toprule
			&       & \multicolumn{1}{l}{type1} & \multicolumn{1}{l}{type2} & \multicolumn{1}{l}{type3} & \multicolumn{1}{l}{type4} \\
	\midrule
	\multirow{2}[1]{*}{sn} & 1     & 2.35  & 2.69  & 7.34  & 5.48 \\
			& \cellcolor[rgb]{ .906,  .902,  .902} 2 & \cellcolor[rgb]{ .906,  .902,  .902} 2.35 & \cellcolor[rgb]{ .906,  .902,  .902} 2.69 & \cellcolor[rgb]{ .906,  .902,  .902} 7.34 & \cellcolor[rgb]{ .906,  .902,  .902} 5.48 \\
	\multirow{2}[1]{*}{sp} & 3     & 6.32  & 5.32  & 9.13  & 7.46 \\
			& \cellcolor[rgb]{ .906,  .902,  .902} 4 & \cellcolor[rgb]{ .906,  .902,  .902} 6.32 & \cellcolor[rgb]{ .906,  .902,  .902} 5.32 & \cellcolor[rgb]{ .906,  .902,  .902} 9.13 & \cellcolor[rgb]{ .906,  .902,  .902} 7.46 \\
	\bottomrule
	\end{tabular}
	\caption{Add caption2}\label{tab:addlabel2}
\end{table}%
```
<img src="https://i.loli.net/2021/01/07/ylSQAGHZfs1MVuY.png" width="280" height="260" align="center">

##### 6.3长表格处理
如果表格内容超过一页，就必须对表格内容进行拆分。
```latex
\usepackage{longtable}
\begin{center}
	\begin{longtable}{|l|l|l|}
		\caption[Feasible triples for a highly variable Grid]{Feasible triples for
			highly variable Grid, MLMMH.} \label{grid_mlmmh} \\

		\hline \multicolumn{1}{|c|}{\textbf{Time (s)}} & \multicolumn{1}{c|}{\textbf{Triple chosen}} & \multicolumn{1}{c|}{\textbf{Other feasible triples}} \\ \hline
		\endfirsthead

		\multicolumn{3}{c}%
		{{\bfseries \tablename\ \thetable{} -- continued from previous page}} \\
		\hline \multicolumn{1}{|c|}{\textbf{Time (s)}} &
		\multicolumn{1}{c|}{\textbf{Triple chosen}} &
		\multicolumn{1}{c|}{\textbf{Other feasible triples}} \\ \hline
		\endhead

		\hline \multicolumn{3}{|r|}{{Continued on next page}} \\ \hline
		\endfoot

		\hline \hline
		\endlastfoot

		0 & (1, 11, 13725) & (1, 12, 10980), (1, 13, 8235), (2, 2, 0), (3, 1, 0) \\
		2745 & (1, 12, 10980) & (1, 13, 8235), (2, 2, 0), (2, 3, 0), (3, 1, 0) \\
	  ...
		101565 & (1, 13, 13725) & (2, 2, 2745), (2, 3, 0), (3, 1, 0) \\
		104310 & (1, 13, 16470) & (2, 2, 2745), (2, 3, 0), (3, 1, 0) \\
	\end{longtable}
\end{center}
```
注意：需编译二到三次才能得到

<img src="https://i.loli.net/2021/01/08/yORlbNmDFQ9Cr5j.png" width="320" height="560" align="center">

#### 7.公式插入
##### 7.1单行公式
```latex
\usepackage{amsmath}
\usepackage{amssymb}`

\begin{equation} %产生带编号的公式
	f(x)=a+b
	\label{eq:eq1}
\end{equation}
\begin{equation}
	f(x)=a-b
	\label{eq:eq2}
\end{equation}

%一个公式的多行排版， & 对齐位置
\begin{equation}
	\begin{split}
		\cos 2x &= \cos^2 x -\sin^2 x\\
				    &= 2\cos^2 x - 1
	\end{split}
\end{equation}
```
`\begin{equation*}`产生不带编号的公式

<img src="https://i.loli.net/2021/01/07/dVIo7SmbBJ86lpv.png" width="400" height="180" align="center">

##### 7.2矩阵
```latex
\begin{equation}
	\left[ \begin{matrix}
		a& b& \cdots& d\\
		& a& \cdots& d\\
		& &	\ddots&	\vdots\\
		0& & & d\\
	\end{matrix} \right]
\end{equation}

\begin{pmatrix}
	a& b& \cdots& d\\
	& a& \cdots& d\\
	& &	\ddots&	\vdots\\
	0& & & d\\
\end{pmatrix}

\[
\begin{bmatrix}
	a& b& \cdots& d\\
	& a& \cdots& d\\
	& &	\ddots&	\vdots\\
	0& & & d\\
\end{bmatrix}
\begin{Bmatrix}
	a& b& \cdots& d\\
	& a& \cdots& d\\
	& &	\ddots&	\vdots\\
	0& & & d\\
\end{Bmatrix}
\begin{vmatrix}
	a& b& \cdots& d\\
	& a& \cdots& d\\
	& &	\ddots&	\vdots\\
	\text{\huge 0}& & & d\\
\end{vmatrix}
\begin{Vmatrix}
	a& b& \cdots& d\\
	& a& \cdots& d\\
	& &	\ddots&	\vdots\\
	\text{\large 0}& & & d\\
\end{Vmatrix}
\]
```
<img src="https://i.loli.net/2021/01/07/sLNUxYkBWQt8iFn.png" width="400" height="250" align="center">

```latex
这是行内小矩阵
\begin{math}
	\left(
		\begin{smallmatrix}
			x & -y \\ y & x
		\end{smallmatrix}
	\right)
\end{math}
```
<img src="https://i.loli.net/2021/01/07/tgH9VCTWnejy5a4.png" width="380" height="25" align="center">

##### 7.3多行公式
###### 7.3.1居中对齐
```latex
\begin{gather}
	a + b = b + a\\
	a - b = c
\end{gather}
%gather带编号，gather*不带编号
\begin{gather*}
	a + b = b + a\\
	a - b = c
\end{gather*}
```
###### 7.3.2指定对齐位置
```latex
\begin{align}
	x &= t + \cos t + 1\\
	y &= 2\sin t
\end{align}
```
<img src="https://i.loli.net/2021/01/07/AdWHb6N974F1mzq.png" width="350" height="250" align="center">

###### 7.3.3带括号
```latex
\begin{equation}
	D\left( x \right) =\left\{ \begin{array}{l}
		1,if\ x>0\\
		0,if\ x<0\\
	\end{array} \right.
\end{equation}
```
<img src="https://i.loli.net/2021/01/07/ycRt7idhxZwSgGa.png" width="350" height="50" align="center">

#### 8.版面设计
1.纸张大小的设置
```latex
\usepackage{geometry}
%\geometry{papersize={宽, 高}}
\geometry{papersize={20cm, 15cm}}
```

2.边距的设置
```latex
\usepackage{geometry}
%\geometry{left=左边距,right=右边距,top=上边距,bottom=下边距}
\geometry{left=5cm,right=5cm,top=5cm,bottom=5cm}
```

3.页眉页脚的设置
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}

%设置页眉
\lhead{页眉左}
\chead{页眉中}
\rhead{页眉右}

%设置页脚
\lfoot{左页脚}
\cfoot{中页脚}
\rfoot{右页脚}
```

4.横分割线的设置
```latex
%\renewcommand{\headrulewidth}{上分割线的宽度}
%\renewcommand{\headwidth}{\textwidth}
%\renewcommand{\footrulewidth}{下分割线的宽度}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\headwidth}{\textwidth}
\renewcommand{\footrulewidth}{0.4pt}
```

5.行间距与段间距
```latex
\usepackage{setspace}
\onehalfspacing %命令：设置行间距,1.5倍
%设置段落间距
%\addtolength{\parskip}{宽度}
```

6.文字对齐
`\begin{flushleft}...\end{flushleft}` 左对齐\
`\begin{center}...\end{center}`居中\
`\begin{flushright}...\end{flushright}`右对齐

综合示例
```latex
%导言区
\usepackage{geometry} %导入版面设置的宏包
\usepackage{fancyhdr} %导入页眉页脚需要的宏包
\pagestyle{fancy}
\usepackage{setspace} %行间距所用的包


\geometry{papersize={20cm, 15cm}} %设置纸张的大小
\geometry{left=2cm,right=5cm,top=5cm,bottom=5cm}%设置边距
%设置页首
\lhead{张一根}
\chead{理工大学}
\rhead{\today}
%设置页眉
\lfoot{左页脚}
\cfoot{\thepage}
\rfoot{右页脚}
%设置横线分割的宽度
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\headwidth}{\textwidth}
\renewcommand{\footrulewidth}{0.4pt}
\onehalfspacing %设置行间距,1.5倍
\addtolength{\parskip}{0.4em} %设置段落间距

%正文区
\begin{document}
    秋风用时光的旋律，...，渲染得天地间空旷而又阳刚。

    酷热的夏天刚刚过去，...说上一晚悄悄话。
\end{document}
```
<img src="http://s64.555889.xyz/2021/01/07/ac92f2ae22a774b9c69e993c905e254c.png" width="350" height="200" align="center">

#### 9.参考文献
把所以的参考文献放在一个后缀名为.bib的文件里
```latex
\bibliographystyle{plain} %在导言区需要导入

%再在需要导入文献的地方，使用
\cite{标签名}

\bibliography{test.bib} %在文字末尾使用
```
**Endnote导出Bib文件**\
1、在endnote中选中你要导出的文献，选择“edit-output style-Open style manager..” 在弹出来的界面中找到有name和category的两列的表格中一列，选择name那一列，然后按键盘b，往下翻，直到看到 BibTex Export那一项，然后勾上。这样就选择了输出bibtex输出方式。\
2、直接关掉刚才那个界面，注意不要关掉整个界面，关掉刚才弹出的那个即可。选择所有要导出的文献，然后在file-export，进入导出界 面。在界面中选择输出txt格式，在output style中选择bibtex export，然后给个名字，保存就ok。
#### 10.自定义
##### 10.1自定义命令
`\newcommand {name}[num]{definition}`，`name`是想要定义的命令的名称，`num`，可选，用于指定命令所需参数的数目，`definition`，命令的定义，也是要执行的操作\
对已有命令进行重写，需换成`\renewcommand`
##### 10.2自定义环境
`\(re)newenvironment{name}[num]{before}{after}`，`name`是想要定义的环境的名称，`num`，可选，所需参数数目，`before`中提供的内容,将在`begin{name}`命令包含的文本之前处理，`after`中提供的内容,将在包含的文本之后，`\end{name}` 的前面处理
