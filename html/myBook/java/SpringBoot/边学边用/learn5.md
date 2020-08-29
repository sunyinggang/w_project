# SpringBoot边学边用（五）SpringBoot使用YAML语法编写配置文件

​         springboot支持两种格式的配置文件，分别是 application.properties 和 application.yml。在之前几节内容中使用的是application.properties，SpringBoot会默认自动读取这个全局的配置文件；而application.yml 是一种YAML格式的文件，yaml是一种简洁的非标记语言，yaml数据为中心，使用空格、缩进、分行来组织数据，使得内容更加简洁易读，并且有利于运维人员后期的维护，有点类似于json格式，因此我们可以将配置文件修改成更简洁的YAML格式。

> 注意：springboot配置文件默认名称为application，不要使用其他名称，否则不会被springboot自动读取

## YAML语法

### 基本语法

k:(空格)v：表示一对键值对（**空格必须有**）；属性和值是大小写敏感的；

以**空格**的缩进来控制层级关系；只要是左对齐的一列数据，都是同一个层级的

```yaml
server:
    port: 8081 #注意这里8081前面有一个空格
```

### 值的写法

k: v：字面直接来写；

​		字符串默认不用加上单引号或者双引号；

​		""：双引号；不会转义字符串里面的特殊字符；特殊字符会作为本身想表示的意思

​				name:   "zhangsan \n lisi"：输出；zhangsan 换行  lisi

​		''：单引号；会转义特殊字符，特殊字符最终只是一个普通的字符串数据

​				name:   ‘zhangsan \n lisi’：输出；zhangsan \n  lisi

### 对象（键值对）：

​	k: v：在下一行来写对象的属性和值的关系；注意缩进。其中对象也是k: v的方式

```yaml
friends:
	lastName: zhangsan
	age: 20
```

行内写法：

```yaml
friends: {lastName: zhangsan,age: 18}
```

### 数组（List、Set）：

用 `- 值` 表示数组中的一个元素

```yaml
pets:
 - cat
 - dog
 - pig
```

行内写法

```yaml
pets: [cat,dog,pig]
```

## Profile

### 什么是Profile？

Profile 可以让 Spring 对不同的环境提供不同配置的功能，可以通过激活、指定参数等方式快速切换环境

### 多Profile文件形式

在进行实际开发的时候，分为本地环境、测试环境和生产环境，这就需要配置多个配置文件，如端口号等等，我们当然可以每更换一个环境就改一次配置，但是十分繁琐

这个时候就可以多设置几个配置文件，文件名格式可以是 `application-{profile}.properties/yml`，但默认使用的主配置文件 `application.properties/yml`

### 举例说明

以新学习的YAML语法格式配置文件为例，创建了三个配置文件：

- `application.yml`：主配置文件
- `application-dev.yml`：开发环境配置文件
- `application-prop.yml`：生产环境配置文件

我们可以在主配置文件中随时切换成其他配置文件，配置内容如下：

`application-prop.yml`配置文件内容：

```yml
server:
  port: 8081 # 生产环境端口
spring:
  profiles: prod #指定属于生产环境
```

`application-dev.yml`配置文件内容：

```yaml
server:
  port: 8083 # 开发环境端口
spring:
  profiles: dev #指定属于开发环境
```

`application.yml`配置文件内容：

```yaml
server:
  port: 8081 # 本地环境端口
spring:
  profiles:
    active: prod # 切换到生产环境
```

## 修改项目中的配置文件

了解了YAML语法后，我们可以将项目中的application.properties修改为application.yml

在resources目录下刪除application.properties，新建application.yml，添加如下代码：

```yaml
server:
  port: 8081

spring:
  datasource:
    # 指定数据库驱动
    driver-class-name: com.mysql.jdbc.Driver
    # 数据库jdbc连接url地址
    url: jdbc:mysql://127.0.0.1:3306/test?useUnicode=true&characterEncoding=utf-8&useSSL=true&serverTimezone=UTC
    # 数据库账号密码
    username: root
    password: 123456

  # thymeleaf设置
  thymeleaf:
    # 关闭缓存
    cache: false
    # 指定thymeleaf模板路径
    prefix: classpath:/templates/
    # 指定字符集编码
    encoding: utf-8

  # js ,css 等静态文件路径
  mvc:
    static-path-pattern: /static/**

# mybatis相关
mybatis:
  # 实体类包路径
  type-aliases-package: com.syg.demo.po
  # 扫描mapper映射文件
  mapper-locations: classpath:Mapper/*.xml
```

**阅读更多技术文章，及时获取内容更新，请扫码关注微信公众号-大数据School！**

![](http://images.simplesay.top/book/wechat.png)
欢迎评论区留下你的精彩评论~
觉得文章不错可以分享到朋友圈让更多的小伙伴看到哦~

同学！在看一下呗