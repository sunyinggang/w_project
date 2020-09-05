# Spring Cloud边学边用（二）Spring Cloud简介

Spring Cloud是由Spring官方开发维护，基于Spring Boot开发，提供了一套完整的**微服务**解决方案。所以提起Spring Cloud就不得不说一下微服务

## 什么是微服务

早些年的服务实现和实施思路是将很多功能从开发到交付都打包成一个很大的服务单元。而微服务实现和实施思路则更强调功能趋向单一，服务单元小型化和微型化。这里用汽车生产车间举例，原来我们是在一个车间里完成汽车的装配、喷漆、焊装与检测工作

![]( http://images.simplesay.top/book/image-20200902163054730.png)

现在（微服务化之后）则建立四个车间，将这四项工作分别放入到不同的车间中，这四项工作就是服务的功能，而车间则是将这些服务功能打包交付的服务单元

![]( http://images.simplesay.top/book/image-20200902163113137.png)

所以，从思路和理念上来讲，微服务就是要倡导大家尽量将功能进行拆分，将服务粒度做小，使之可以独立承担对外服务的职责，沿着这个思路开发和交付的软件服务实体就叫作“微服务”

## SpringBoot与SpringCloud的关系

Spring Cloud是完全基于Spring Boot 而开发，Spring Cloud 利用 Spring Boot 特性整合了开源行业中优秀的组件，整体对外提供了一套在微服务架构中服务治理的解决方案。

## SpringCloud的常用组件

- 服务发现——Netflix Eureka
- 客服端负载均衡——Netflix Ribbon
- 断路器——Netflix Hystrix
- 服务网关——Netflix Zuul
- 分布式配置——Spring Cloud Config

我将在后续文章中对常用组件进行详细讲解，并说明如何使用

## 使用IDEA创建Spring Cloud项目

接下来几节内容我们会把第一篇文章中使用Spring Boot创建的微服务改用Spring Cloud重新构建一个真正的微服务

### 创建父工程

打开Intellij IDEA，点击File -> New -> Project

![](http://images.simplesay.top/book/20200806171241.jpg)

在左侧选中Maven，创建一个maven项目，点击next，输入自己的包名和项目名，父工程和子工程的包名需要保持一致

![]( http://images.simplesay.top/book/image-20200902175603037.png)

### 修改父工程pom文件

删除根目录下的src目录，因为根目录相当于父模块，只需要对pom.xml进行配置，打开根目录下pom.xml文件，将以下配置覆盖原文件内容

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.syg.demo</groupId>
    <artifactId>shop</artifactId>
    <version>1.0-SNAPSHOT</version>

    <name>shop</name>
    <description>SpringCloud Project For shop</description>

    <!-- 项目的打包类型, 即项目的发布形式, 默认为 jar. 对于聚合项目的父模块来说, 必须指定为 pom -->
    <packaging>pom</packaging>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.4.RELEASE</version>
    </parent>

    <properties>
        <spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
    </properties>

    <dependencies>
        <!-- 引入单元测试 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <!-- 标识 SpringCloud 的版本 -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- 配置远程仓库 -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
    
</project>
```