# SpringBoot边学边用（一）使用Intellij IDEA搭建初始化SpringBoot项目

都已经2020年了，赶快放弃Eclipse拥抱Intellij IDEA吧！本文讲解如何使用Intellij IDEA快速搭建初始化SpringBoot项目

## 创建项目

打开Intellij IDEA，点击File -> New -> Project

![](http://images.simplesay.top/book/20200806171241.jpg)

左侧选择Spring Initializr -> 选择要使用的SDK（我这里升级到了jdk 11版本）-> 选择默认地址下载已经创建的初始化SpringBoot项目 -> 点击nex

![image-20200817172916195]( http://images.simplesay.top/book/image-20200817172916195.png)

填写GroupId和ArtifactId，默认使用Maven工具管理jar包，点击next

![image-20200818183831693]( http://images.simplesay.top/book/image-20200818183831693.png)

添加依赖，勾选Spring Web -> next -> finish，这样就构建了一个初始化SpringBoot项目

![image-20200817173632184]( http://images.simplesay.top/book/image-20200817173632184.png)

## 目录解析

初始化目录结构如下，对文件作用进行基本解释

```json

└─ .idea # idea创建的编译器配置文件
└─ .mvnw # 一个maven wrapper script,可以在没有安装maven或者maven版本不兼容的条件下运行maven的命令
└─ src
    ├─main
    │  ├─java  # 程序开发文件夹，在这里写程序代码
    │  │  └─com
    │  │     └─syg
    │  │        └─demo
    │  │           │  DemoApplication # 主程序入口启动类，运行该类启动SpringBoot应用   
    │  └─resources  # 配置目录，该目录用来存放应用的一些配置信息
    │      │  application.properties  # 用于存放程序的各种依赖模块的配置信息
    │      ├─static     # 静态资源目录,用于存放静态资源，如图片、CSS、JavaScript等
    │      └─templates  # 视图模板目录,存放Web页面的模板文件
    └─test  # 测试类，使用Junit对java中的源代码进行测试
│  HELP.md  # （无用，可直接删除）
│  mvnw     # （无用，可直接删除）
│  mvnw.cmd # （无用，可直接删除）
│  pom.xml  # maven配置文件，可以直接在此文件中添加项目依赖jar包                 
```

## 运行测试

创建的SpringBoot项目内置tomcat，打开主程序入口启动类，点击main方法前的绿色箭头选择Run

![image-20200818184217366]( http://images.simplesay.top/book/image-20200818184217366.png)

项目正确启动标志，没有任何报错信息

![image-20200817184509591]( http://images.simplesay.top/book/image-20200817184509591.png)

运行项目常见的一个问题就是默认8080端口被其他应用程序占用

![image-20200817184627073]( http://images.simplesay.top/book/image-20200817184627073.png)

可以通过application.properties修改服务端口号

![！]( http://images.simplesay.top/book/image-20200817184537760.png)

**阅读更多技术文章，及时获取内容更新，请扫码关注微信公众号-大数据School！**

