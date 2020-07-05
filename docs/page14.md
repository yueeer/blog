<center><img src="https://i.loli.net/2020/06/08/gcwel5R3MbtTxUh.png" width="20%"></center>

## Github & Git基础操作总结

学习教程来自b站：[【教程】学会Git玩转Github【全】](https://www.bilibili.com/video/BV1Xx411m7kn?p=10)\
参考CSDN总结：[Git和Github详细入门教程（别再跟我说你不会Git和Github)](https://blog.csdn.net/jiahuan_/article/details/105933423)\
参考GitHub总结：[Git笔记](https://github.com/yezhaodan/-Git/blob/master/GitLearning.md)
参考廖雪峰老师网站：[Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)

### Ⅰ Github

**Github**是全球最大的社交编程及代码托管网站(https://github.com/),借助git来管理项目代码

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
<img src="https://i.loli.net/2020/07/04/uapkc5blyUGmhBE.png" width="350" height="150" align="center">

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
commit的版本会存储，可以进行还原\
3)确定文件是否已在Git仓库中：
```
git status
```
att:每次修改本地文件（vim）后都要重新add和commit\
4)删除工作区文件：
```
git rm –f hello.php
```
5)比对本地文件和暂存区文件，回顾修改步骤
```
git diff hello.php
```
6)查看commit历史
```
git log
```
会按提交时间列出所有的更新,最近的更新排在最上面,HEAD指针指向最后状态\
7)返回历史版本
```
git reset --hard HEAD^ #返回上个状态
git reset --hard HEAD^^ #返回上上个状态
git reset --hard HEAD~100 #返回上100个状态
git reset --hard commit指令序号 #返回特定的状态
```
本地同步修改，git仓库指针修改

8）把文件在本地的修改全部撤销
```
git checkout -- hello.php
```
一种是文件自修改后还没有被放到暂存区，现在，撤销修改就回到和git仓库一模一样的状态；\
一种是文件已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

#### 4.远程仓库操作

如何将本地仓库同步到远程仓库中：

##### 4.1将远程仓库（github对应的项目）复制到本地：
```
git clone 仓库地址
```
注意：仓库地址在clone or download按钮下取得

##### 4.2进行文件增删改查，并添加到Git仓库中

1）建立GitHub和git仓库的连接

- 创建公钥

进入~/.ssh/
```
ssh-keygen -t rsa -b 2048 -C "github账号"
```
查看 id_rsa.pub，将里面的内容复制到github/settings/SSH and GPG keys/SSH keys/new SSH key/key

- 查看是否接通

```
ssh -T git@github.com
```

- git仓库与要传入的github仓库建立连接

```
git remote add origin git@github.com:...
```
如果更换位置
```
git rempte rm origin
git remote add origin git@github.com:...
```

2) 将本地仓库同步到远程仓库中

```
git push (-f) origin master
```
#### 5.分支管理

分支管理可以使版本库的演进保持简洁，主干清晰，各个分支各司其职、井井有条。

主分支**Master**只有一个，它是自动建立的，默认就是在主分支在进行开发。所有提供给用户使用的正式版本，都在这个主分支上发布。\
开发分支**Develop**，这个分支可以用来生成代码的最新隔夜版本（nightly）。如果想正式对外发布，就在Master分支上，对Develop分支进行"合并"（merge）。
团队成员都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并。
<img src="https://i.loli.net/2020/07/04/b1wvD4puCsyirYQ.png" width="450" height="150" align="center">

##### 5.1创建和合并分支
Git用master指向最新的提交，每次提交，master分支都会向前移动一步。
<img src="https://i.loli.net/2020/07/04/qZjY4NOsatXCzen.png" width="250" height="100" align="center">

1）创建新的分支dev\
Git新建了一个指针指向master相同的提交，再把HEAD指向dev，就表示当前分支在dev上
<img src="https://i.loli.net/2020/07/04/SyTcRtiAKdq6kvg.png" width="280" height="120" align="center">
```
git checkout -b dev 或 git switch -c dev#创建并切换到dev分支
```
相当于
```
git branch dev #创建新的分支
git checkout dev  #切换到新分支
```
查看当前分支
```
git branch
* dev
  master
```
2)在dev分支进行修改和提交(vim + add + commit)
<img src="https://i.loli.net/2020/07/04/qFm15cClJNMw7ty.png" width="300" height="150" align="center">

此时如果回到master分支查看文件，文件还是修改前的状态

3）merge master and dev
<img src="https://i.loli.net/2020/07/04/GxlPWLAaptzcY4J.png" width="300" height="150" align="center">
```
git switch master #切换到master分支
git merge dev #合并指定分支到当前分支
```
此时master分支中文件的内容和dev分支的最新提交是完全一样的。

4)删除dev分支
<img src="https://i.loli.net/2020/07/04/zBrbfKk5s1DIeRq.png" width="280" height="120" align="center">
```
git branch -d dev
```
##### 5.2解决冲突

master分支和feature1分支各自都分别有新的提交，变成了这样
<img src="https://i.loli.net/2020/07/04/nChEqwVI8p52vSl.png" width="300" height="180" align="center">

此时进行合并会有冲突，必须手动解决冲突。可以直接查看文件中的内容
```
没问题的部分+
<<<<<<< HEAD
Creating a new branch is quick & simple.
=======
Creating a new branch is quick AND simple.
>>>>>>> feature1
```
手动修改master中的部分再add,commit,merge,如图所示
<img src="https://i.loli.net/2020/07/04/dr24QltNZ8eHzE9.png" width="320" height="200" align="center">

用git log --graph可以看到分支的合并情况
```
$ git log --graph --pretty=oneline --abbrev-commit
*   cf810e4 (HEAD -> master) conflict fixed
|\
| * 14096d0 (feature1) AND simple
* | 5dc6824 & simple
|/
* b17d20e branch test
...
```
最后，删除feature1分支

##### 5.3--no-ff方式的git merge
1)合并方式\
合并要创建一个新的commit，所以加上-m参数，把commit描述写进去。
```
git merge --no-ff -m "merge with no-ff" dev
```
用git log看看分支历史：
```
*   e1e9c68 (HEAD -> master) merge with no-ff
|\
| * f52c633 (dev) add merge
|/
*   cf810e4 conflict fixed
...
```
<img src="https://i.loli.net/2020/07/04/sSLxHdg3UcCPwZW.png" width="320" height="200" align="center">

2)Fast-forward与no-ff的区别\
参考fangchao3652博客[git Fast-forward与no-ff的区别](https://blog.csdn.net/fangchao3652/article/details/53540874)

使用no-ff后，会多生成一个commit 记录，强制保留dev分支的开发记录\
而fast-forward的话则是直接合并，看不出之前Branch的任何记录

![1.png](https://i.loli.net/2020/07/04/CnDirGzj8vcwNMm.png)
![2.png](https://i.loli.net/2020/07/04/bIF7QE18jWlr6Pv.png)

##### 5.4Bug分支

当你接到一个修复一个代号101的bug的任务时，你想创建一个分支issue-101来修复它，但是，当前正在dev上进行的工作还没法提交，Git stash功能可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作。
```
$git stash
Saved working directory and index state WIP on dev: f52c633 add merge
```
用git status查看工作区，就是干净的,可以放心地创建分支来修复bug。

假定需要在master分支上修复，就从master创建临时分支,修复bug，add,commit,merge,删除issue-101分支，回到dev分支干活。此时查看工作区
```
$git status
On branch dev
nothing to commit, working tree clean
```
用git stash list命令看看：
```
$ git stash list
stash@{0}: WIP on dev: f52c633 add merge
```
进行恢复同时把stash内容也删了
```
git stash pop
git stash apply stash@{0} #恢复指定的stash
```
在dev分支上修复同样的bug，我们只需要把commit时显示的4c805e2 fix bug 101这个提交所做的修改“复制”到dev分支。
```
$ git branch
* dev
  master
$ git cherry-pick 4c805e2
[master 1d4b803] fix bug 101
 1 file changed, 1 insertion(+), 1 deletion(-)
```

##### 5.5Feature分支
开发一个新feature，最好新建一个分支；\
如果要丢弃一个没有被合并过的分支，可以强行删除
```
git branch -D <分支名>
```

##### 5.6多人协作

1）查看远程库的信息\
远程仓库的默认名称是origin
```
git remote (-v) #-v显示更详细信息
```

2)抓取分支

clone下远程仓库
```
git clone git@github.com:
```
默认情况下，只能看到本地的master分支，可以用git branch查看。

要在dev分支上开发，就必须创建远程origin的dev分支到本地
```
git checkout -b dev(本地分支名) origin/dev（远程分支名）
```
在本地dev上修改，add,commit

3)推送分支

把本地分支上的所有本地提交推送到远程库
```
git push origin master/dev/...(本地分支名) 
```

4)解决冲突

如果同事的最新提交和你试图推送的提交有冲突导致push失败，先抓取最新提交在本地合并解决冲突
```
git pull
```
如果没有指定本地dev分支与远程origin/dev分支的链接导致git pull失败,提示“no tracking information”
```
git branch --set-upstream branch-name origin/branch-name
```
