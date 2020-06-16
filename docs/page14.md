<center><img src="https://i.loli.net/2020/06/08/gcwel5R3MbtTxUh.png" width="20%"></center>

## Github & Git基础操作总结

学习教程来自b站：[【教程】学会Git玩转Github【全】](https://www.bilibili.com/video/BV1Xx411m7kn?p=10)\
参考CSDN总结[：Git和Github详细入门教程（别再跟我说你不会Git和Github)](https://blog.csdn.net/jiahuan_/article/details/105933423)\
参考GitHub总结：[Git笔记](https://github.com/yezhaodan/-Git/blob/master/GitLearning.md)

### Ⅰ Github

**Github**是全球最大的社交编程及代码托管网站,借助git来管理项目代码

#### 1.基本概念
**仓库（Repository）**:用来存放项目代码，每个项目对应一个仓库，多个开源项目则有多个仓库\
**收藏（Star）**:收藏项目，方便下次查看\
**复制克隆项目（Fork）**:fork的项目是独立存在的,复制过来自己用\
**发起请求（Pull Request）**:你新增了功能，觉得不错，想和原本项目一起,就可以发起合并请求\
**关注（Watch）**:关注项目，当项目更新可以接收到通知\
**事务卡片（Issue）**:发现代码BUG，但是目前没有成型代码，需要讨论时用

#### 2.创建仓库
![1.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvaENSc3U0OGsyTkxNaWpILnBuZw?x-oss-process=image/format,png)
仓库主页
![2.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvM0ZhZ09BWlVWejlOanhLLnBuZw?x-oss-process=image/format,png)
#### 3.仓库管理

##### 3.1创建文件
![3.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvZ1V0YWxvTlI1NkhYUHBpLnBuZw?x-oss-process=image/format,png)![4.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvTmlXbEdVdWs1QWI4alNILnBuZw?x-oss-process=image/format,png)
![5.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvT2xLSXF2clNSeTdrUEZoLnBuZw?x-oss-process=image/format,png)
![6.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvblNxSTRKZVoyY0R1alB3LnBuZw?x-oss-process=image/format,png)

##### 3.2编辑文件

![7.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvSzNiWEpxMkdaUkw2amhFLnBuZw?x-oss-process=image/format,png)
![8.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvaDFjTGQ0emJhM0pGSDlOLnBuZw?x-oss-process=image/format,png)
![9.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvaU93VjVxNDNySWs3U3VuLnBuZw?x-oss-process=image/format,png)
##### 3.3删除文件
![1.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvUm9tYzduMTM5dlFObGJJLnBuZw?x-oss-process=image/format,png)

##### 3.4上传文件
![2.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvWTdIbnY4a2lBMmZPSmJtLnBuZw?x-oss-process=image/format,png)
![3.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvOVRxY3ltbklEWDVsamRLLnBuZw?x-oss-process=image/format,png)

##### 3.5搜索文件
![4.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvM1k1RXFHWEpsMWtpSXlVLnBuZw?x-oss-process=image/format,png)
![5.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvSTJWa1VZbU1GS1B1ZEpvLnBuZw?x-oss-process=image/format,png)
##### 3.6下载项目

点击clone or download按钮

**注意**：Commits可以查看每次修改的相关信息，包括删除的文件的详细信息；编辑文件也算一次提交

##### 3.7对issue的操作

作用:发现代码BUG，需要讨论时用;或者使用开源项目出现问题时使用

情景:张三发现李四开源git库，则发提交了一个issue;李四隔天登录在github主页看到通知并和张三交流，最后关闭issue

![1.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvbzdzZTQ4TTNwell4YzJaLnBuZw?x-oss-process=image/format,png)
![2.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvWnVZQmlEbDMxakFyNGVVLnBuZw?x-oss-process=image/format,png)
![3.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvcjI5dExoUXhFRnZpVk5ELnBuZw?x-oss-process=image/format,png)
![4.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvbWV6UUNiUzlsYWZzdnBxLnBuZw?x-oss-process=image/format,png)
![5.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvRFYxZUpXMzhDS1RJNk93LnBuZw?x-oss-process=image/format,png)

##### 3.8Pull request
1)fork项目\
![1.png](https://imgconvert.csdnimg.cn/aHR0cDovL2NodWFudHUueHl6L3Q2LzczOC8xNTkyMzIwOTcxeDk3NzAxMzI2NC5wbmc?x-oss-process=image/format,png)
2)修改自己仓库的项目代\
3)新建pull request\
![2.png](https://imgconvert.csdnimg.cn/aHR0cDovL2NodWFudHUueHl6L3Q2LzczOC8xNTkyMzIxMDM0eDk5MjIzOTQwOC5wbmc?x-oss-process=image/format,png)
![Nkjf0g.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9zMS5heDF4LmNvbS8yMDIwLzA2LzE2L05ramYwZy5wbmc?x-oss-process=image/format,png)
4)等待作者操作（合并）\
![4.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDYvMTYvQkxONFluMVdRdXc3Y0VQLnBuZw?x-oss-process=image/format,png)![NkjWnS.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9zMS5heDF4LmNvbS8yMDIwLzA2LzE2L05ralduUy5wbmc?x-oss-process=image/format,png)
### Ⅱ  Git

**Git**是一个免费、开源的版本控制软件（记录文件的所有历史变化、随时可恢复到任何一个历史状态、多人协作开发或修改错误恢复）

#### 1.Git的安装

[官网](https://git-scm.com/download/win)下载安装\
检验是否安装成功：右击鼠标显示Git GUI Here和Git Bash Here

#### 2.一些基础设置

设置用户名
```
git config –-global user.name '这里填写自己的用户名'
```
设置用户名邮箱
```
git config –-global user.email '这里填写自己的用户名邮箱'
```
查看设置
```
git config --list
```

#### 3.本地仓库操作

##### 3.1初始化一个新的Git仓库
1)创建文件夹\
2)在文件夹内初始化Git（创建Git 仓库）\
命令行进入当前目录，使用
```
git init
```
成功会生成隐藏的.git文件\
3)向仓库中添加文件

##### 3.2本地操作区域
<img src="https://i.loli.net/2020/06/17/YOcxsPyIjnkeQqZ.png" width="400" height="250" align="center">

##### 3.3向仓库中添加文件
<img src="https://i.loli.net/2020/06/17/T8UueIlN3QotfjS.png" width="450" height="250" align="center">

git status：确定文件当前所处Git工作区域；

这里假设在工作区有文件 php文件\
1)工作区转入暂存区：
```
git status
git add hello.php
```
2)暂存区转入Git 仓库：
```
git status
git commit –m '提交描述'
```
3)确定文件是否已在Git仓库中：
```
git status
```
4)删除工作区文件：
```
git rm –f hello.php
```

#### 4.远程仓库操作

如何将本地仓库同步到远程仓库中：

1)将远程仓库（github对应的项目）复制到本地：
```
git clone 仓库地址
```
注意：仓库地址在clone or download按钮下取得

2)进行文件增删改查，并添加到Git仓库中

3)将本地仓库同步到远程仓库中 使用命令：
```
git push
```
