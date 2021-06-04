# Student_homework
学员代码作业仓库，使用 GitHub，Gitee 主要是为了方便阅读。

Gitee：[https://gitee.com/huangjiabaoaiyc/Student_homework](https://gitee.com/huangjiabaoaiyc/Student_homework)

Github：[https://github.com/AndersonHJB/Student_homework](https://github.com/AndersonHJB/Student_homework)



# 1. 首先 Fork 他人的 repository（代码仓库）

Fork 的名词是  **叉子**  的意思，不过这里取的是动词 **分叉，建一个分支** 的意思。进入你想参与合作开发的仓库界面，点击右上角的 **Fork** 图标，此时你已经复制了一个副本在你的 GitHub 仓库中了，或者是说一个新的代码仓库被创建了，可以打开你的 GitHub 主页看一看。

**注意，这个远程仓库是属于你自己的。这里 Fork 不同于 Clone，Clone 是发生在你的本地机器中，相当于你复制了一个完全相同的副本在你的终端上，但该副本的远程仓库连接的仍然是原作者的仓库，所以你并不是这个项目仓库的拥有者，没有更新它的权限。**

因此，Fork 正是我们所需要的。

![image-20210604105105691](README.assets/image-20210604105105691.png)

点击之后可以看到，自己帐号内有一个新的代码仓库被创建了。

![image-20210604110759936](README.assets/image-20210604110759936.png)

**然后将这个代码仓库 Clone（克隆）到你的本地机器中，**可以使用命令行或者 IDE（比如 Intellij IDEA）的 **VCS** 功能来实现。**Clone** 成功之后你就可以自主修改里面的内容，然后 **Push** 到远程仓库中，注意，这是你自己的远程仓库。**但是不使用 Fork，而是直接 Clone（克隆）原作者的仓库的话，你会得到一个 fatal: unable to access 的提示，无法访问。**



**在这一环节，所有的修改只发生在你的远程仓库中，原作者的代码仓库内容是不会发生任何改变的。这里最需要理解的是，Clone 下来的本地仓库连接的是你 GitHub 上的远程仓库。**



# 2. 开始参与开发前的一些准备

（1）在你做任何开发前，最好先详细阅读该项目的 **CONTRIBUTING.md 文件**。

（2）浏览该项目的 **Issues（问题）**公告，甚至可以自己创建一个 **Issue**。

（3）一般不要将自己做的修改提交到 **master branch（主分支）**上，而是应该提交到某个明确的 **topic branch（主题分支，解决某个 bug  或者添加某一功能的分支）**上。**注意，我们应该自己建一个 topic branch，然后在上面作修改，而不在 master 分支直接修改，因为这样更具有直观性。**

（4）最好每次只提交较小的修改，并写好清晰明确的 **Commit Messages（提交说明）**.

（5）如果有需要，请更新 **README 文件**。



# 3. 创建一个 Pull Request

按自己的需要去修改项目内容，然后将所做的修改提交（Add+Commit）到自己的代码仓库，接着到仓库页面，点击 **New pull request** 按钮。

![image-20210604111406963](README.assets/image-20210604111406963.png)

![image-20210604111506923](README.assets/image-20210604111506923.png)

![image-20210604111550256](README.assets/image-20210604111550256.png)

![image-20210604111636953](README.assets/image-20210604111636953.png)

点击去之后可以看到，左边红框是你 Fork 的原项目仓库和分支，右边红框是你当前选择的项目仓库和分支。



**其实这里就是将两个红框内的内容作对比，并把不相同的地方显示出来。** 因为此时两个仓库和分支的内容是不一样的，所有显示出了一些修改区别。接下来点击如下：

![image-20210604112250766](README.assets/image-20210604112250766.png)

填写你的请求信息，说明你做了些什么之类的。这个请求是发给该项目的维护者（拥有者）的，完成之后点击 **Create pull request** 按钮即可。

![image-20210604112334610](README.assets/image-20210604112334610.png)

![image-20210604112435774](README.assets/image-20210604112435774.png)

**之后项目的维护者会受到你的请求，只要他/她通过了你的请求，你所做的修改就会被整合到原项目的仓库里了。**

接下来，我就用我的主体账号来看看。

![image-20210604112529496](README.assets/image-20210604112529496.png)

![image-20210604113415993](README.assets/image-20210604113415993.png)


![image-20210604113440201](README.assets/image-20210604113440201.png)

![image-20210604113455878](README.assets/image-20210604113455878.png)



# 4. 与原仓库保持同步更新

**说到合作开发就会有一个问题，如何与他人的代码保持同步？**



在自己做开发的过程中，难免会遇到你 Fork 的项目已经有了新的更新，这时当然是希望自己仓库中的代码也能同步进行更新。可是，你本地仓库所连接的远程仓库的是你自己的 GitHub 仓库，而不是原作者的仓库。**解决方法其实很简单，为你的本地仓库再添加一个远程仓库源。**

> **查看当前项目所连接的远程仓库**
>
> 打开终端，进入到项目的 Git 仓库所在目录，一般就是项目目录，输入：
>
> **git remote -v**

```git
git remote -v
```

![image-20210604114142622](README.assets/image-20210604114142622.png)

> 这里，因为账号的原因，我就用主账号来给大家演示。

可以看到目前只连接了我自己的远程仓库。

> **添加原作者的远程仓库连接**
>
> **git remote add upstream https://github.com/AndersonHJB/Student_homework**
>
> **（注意替换原仓库的 http 链接）**

然后你可以继续使用：

```git
git remote -v
```

查看有无成功添加。

我用别的仓库演示：

![image-20210604142916960](README.assets/image-20210604142916960.png)

> 还差一点就大功告成了
>
> **（1）从原仓库获取最新版本到本地**
>
> **git fetch upstream master**
>
> **（2）保证当前位于 master 分支上**
>
> **git checkout master**
>
> **（3）将最新版本整合到本地 master 分支上**
>
> **git merge upstream/master**
>
> **（4）将更新发送到自己的 GitHub 仓库里**
>
> **git push origin master**

> （1）（2）（3）步可以用
>
> **git pull upstream master**
>
> 这条命令替代，可以这样不太安全，因为你 **fetch（获取）**之后可以通过
>
> **gitlog--oneline --graph --decorate --all**
>
> 来查看更新的情况，再决定是否 **merge（整合）**到一起。



# 5. 交作业方法

接下来，我拿朋友的 GitHub 账号来完整操作一遍。

![image-20210604145405287](README.assets/image-20210604145405287.png)

![image-20210604145430484](README.assets/image-20210604145430484.png)

![image-20210604145504677](README.assets/image-20210604145504677.png)

![image-20210604150252660](README.assets/image-20210604150252660.png)

我们桌面就有了这个文件夹了：

![image-20210604150438808](README.assets/image-20210604150438808.png)

接下来，我把我的一张照片放到仓库里面：

![image-20210604150542772](README.assets/image-20210604150542772.png)

![image-20210604150619229](README.assets/image-20210604150619229.png)

