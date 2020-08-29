# SpringBoot边学边用（六）使用Mybatis Generator 自动生成 Mapper 文件

>  Mybatis generator主要的功能就是方便，快捷的创建好Dao、entry、xml，加快了开发速度 

## 添加依赖

在项目pom.xml文件<dependencies></dependencies>标签内添加如下代码

```xml
        <!-- MyBatis 生成器 -->
        <dependency>
            <groupId>org.mybatis.generator</groupId>
            <artifactId>mybatis-generator-core</artifactId>
            <version>1.3.7</version>
        </dependency>
```

## 数据库配置

在resources目录下新建generator-config.properties 文件，填写数据库连接信息，用于自动生成Mapper时连接数据库

```properties
jdbc.driverClass=com.mysql.cj.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/test?useUnicode=true&characterEncoding=utf-8&useSSL=true&serverTimezone=UTC
jdbc.username=root
jdbc.password=123456
```

## Mybatis Generator 配置

### generator-config.xml 文件

在resources目录下新建generator-config.xml 文件，编写自动生成mapper、dao、po配置文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
        PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">

<generatorConfiguration>
    <properties resource="generator-config.properties"/>
    <context id="MySqlContext" targetRuntime="MyBatis3" defaultModelType="flat">
        <property name="beginningDelimiter" value="`"/>
        <property name="endingDelimiter" value="`"/>
        <property name="javaFileEncoding" value="UTF-8"/>
        <!-- 实现序列化方法并生成序列化id-->
        <plugin type="org.mybatis.generator.plugins.SerializablePlugin"/>
        <!-- 生成重写的toString()方法 -->
        <plugin type="org.mybatis.generator.plugins.ToStringPlugin"/>
        <!--生成mapper.xml时覆盖原文件-->
        <plugin type="org.mybatis.generator.plugins.UnmergeableXmlMappersPlugin"/>
        <commentGenerator type="org.mybatis.generator.internal.DefaultCommentGenerator">
            <!-- 是否去除自动生成的注释 true：是 ： false:否 -->
            <property name="suppressAllComments" value="true"/>
            <property name="suppressDate" value="true"/>
            <property name="addRemarkComments" value="true"/>
        </commentGenerator>

        <jdbcConnection driverClass="${jdbc.driverClass}"
                        connectionURL="${jdbc.url}"
                        userId="${jdbc.username}"
                        password="${jdbc.password}">

            <property name="nullCatalogMeansCurrent" value="true" />
        </jdbcConnection>

        <!--实体类生成路径 targetPackage -->
        <javaModelGenerator targetPackage="com.syg.demo.po"
                            targetProject="src/main/java"/>

        <!--mapper.xml 生成路径 targetPackage -->
        <sqlMapGenerator targetPackage="Mapper" targetProject="src/main/resources"/>

        <!--dao层接口 生成路径 targetPackage -->
        <javaClientGenerator type="XMLMAPPER" targetPackage="com.syg.demo.dao"
                             targetProject="src/main/java"/>
        <!--生成全部表tableName设为%-->
        <table tableName="%" enableCountByExample="false" selectByExampleQueryId="false"
               enableDeleteByExample="false" enableSelectByExample="false" enableUpdateByExample="false">
            <generatedKey column="id" sqlStatement="MySql" identity="true"/>
        </table>
    </context>
</generatorConfiguration>
```

### 启动类代码

在包com.syg.demo下新建一个类：GeneratorMapper，编写启动Mybatis Generator的程序代码

```java
package com.syg.demo;

import org.mybatis.generator.api.MyBatisGenerator;
import org.mybatis.generator.config.Configuration;
import org.mybatis.generator.config.xml.ConfigurationParser;
import org.mybatis.generator.internal.DefaultShellCallback;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class GeneratorMapper {
    public static void main(String[] args) throws Exception {
        //MBG 执行过程中的警告信息
        List<String> warnings = new ArrayList<>();

        //读取配置文件
        InputStream is = GeneratorMapper.class.getResourceAsStream("/generator-config.xml");
        ConfigurationParser cp = new ConfigurationParser(warnings);
        Configuration config = cp.parseConfiguration(is);
        is.close();

        //当生成的代码重复时，覆盖原代码
        DefaultShellCallback callback = new DefaultShellCallback(Boolean.TRUE);

        MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config, callback, warnings);
        //执行生成代码
        myBatisGenerator.generate(null);
        //输出警告信息
        for (String warning : warnings) {
            System.out.println(warning);
        }
    }
}
```

## 运行程序，生成mapper文件、dao接口、po实体类

打开GeneratorMapper文件，点击运行，控制台没有输出报错信息即代表成功运行，生成了mapper、dao、po

![]( http://images.simplesay.top/book/image-20200819210648422.png)

> 提示：由于前几节内容自己创建过po与mapper文件，所以这里控制台最后信息为重写文件（单纯只阅读本节内容的自动忽略这个提示）

这里需要注意一点，通过Mybatis Generator生成的dao层默认类名为*Mapper，所以这里删除我们之前自己创建的CustomerDao接口文件（单纯只阅读本节内容的自动忽略这个删除）

![]( http://images.simplesay.top/book/image-20200819210450124.png)

## 添加MyBatis的Java配置

我们打开生成的CustomerMapper接口，发现接口上没有使用@Mapper注解，这样在SpringBoot启动时就无法实现自动注入，就不可能将这个dao交给Spring管理

![]( http://images.simplesay.top/book/image-20200819211458062.png)



在com.syg.demo下新建包config，在包内创建MyBatis的配置类：MyBatisConfig.java

通过添加@Configuration定义为配置类，然后使用@MapperScan注解并将要自动扫描的dao层路径作为参数，这样SpringBoot在启动时就会将dao层交由Spring管理，具体代码如下：

```java
package com.syg.demo.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;

/**
 * MyBatis配置类
 */
@Configuration
@MapperScan("com.syg.demo.dao")
public class MyBatisConfig {
}
```

## 修改Service层

在com.syg.demo.service.impl包下找到CustomerServiceImpl.java，我们要将之前的customerDao对象换成自动生成的customerMapper对象，并调用自动生成的通过主键查询数据的方法

![]( http://images.simplesay.top/book/image-20200819212645897.png)

> 提示：只查看本节内容的读者忽略这个修改

## 总结

自动生成mapper在开发中是一种非常省时的方式，本节内容讲解了自动生成整个过程，特别是书写的generator-config.xml 文件查阅了很多博客，才能达到一次运行，没有报错的效果。在文章内容中出现的几个提示是给阅读整个专栏内容的读者看的，但是不影响单独学习这节内容的其他读者，如果感兴趣也可以阅读此专栏其他文章

**阅读更多技术文章，及时获取内容更新，请扫码关注微信公众号-大数据School！**

![](http://images.simplesay.top/book/wechat.png)
欢迎评论区留下你的精彩评论~
觉得文章不错可以分享到朋友圈让更多的小伙伴看到哦~

同学！在看一下呗