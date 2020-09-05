# Spring Cloud边学边用（三）服务发现框架Eureka

## 基本架构

Eureka由三个角色组成

- Eureka Server：提供服务注册与发现
- Service Provider：服务提供方，将自身服务注册到Eureka Server上，从而让Eureka Server持有服务的元信息，让其他的服务消费方能够找到当前服务
- Service Consumer：服务消费方，从Eureka Server上获取注册服务列表，从而能够消费服务

Eureka的基本架构图如下图所示：

![]( http://images.simplesay.top/book/image-20200902174700030.png)

​		其实很好理解，比如我们出门旅游，想要住当地民宿，可以使用某些预订民宿APP进行查找房源，在我们查找房源之前，所有的房源信息都是由房东提供给APP平台的，当我们获取到房源信息后，可以根据APP平台提供的联系方式与房东取得联系。在这个例子里房东就是Service Provider，提供了房源信息；我们租房的就是Service Consumer，从APP中获取房源信息，并且能够根据APP平台提供的联系方式与房东取得联系；APP平台就是Eureka Server，提供给房东发布房源信息的功能，而且可以让我们获取到房东发布的房源信息。

​		这里还需要补充一点，服务注册成功后，Eureka 客户会每隔30秒(默认情况下)发送一次心跳来**续约**。通过续约来告知Eureka Server 该 Eureka 客户仍然存在，没有出现问题。正常情况下，如果Eureka Server 在90秒没有收到 Eureka 客户的续约，它会将实例从其注册表中删除。

## Eureka Server高可用

存在问题：单节点的Eureka Server虽然能够实现基础功能，但是存在单点故障的问题，不能实现高可用。因为Eureka Server中存储了整个系统中所有的微服务的元数据信息，单节点一旦挂了，所有的服务信息都会丢失，造成整个系统的瘫痪

解决办法：搭建Eureka Server集群，让各个Sever节点之间相互注册，从而实现微服务元数据的复制/备份，即使单个节点失效，其他的Server节点仍可以继续提供服务

Eureka Server集群架构：

![]( http://images.simplesay.top/book/image-20200902192538505.png)

## 搭建Eureka Server模块

首先在父模块（根目录）下新建Module

![]( http://images.simplesay.top/book/image-20200902182227986.png)

选择继承父模块，填写ArtifactId，即为shop-eureka模块

![]( http://images.simplesay.top/book/image-20200902201204071.png)

将shop-eureka模块的pom.xml配置内容替换为以下配置：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>shop</artifactId>
        <groupId>com.syg.demo</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>shop-eureka</artifactId>
    <version>1.0-SNAPSHOT</version>
    <!-- 项目的打包类型,子模块使用默认的jar -->
    <packaging>jar</packaging>

    <!-- 模块名及描述信息 -->
    <name>shop-eureka</name>
    <description>Spring Cloud Eureka For shop</description>

    <!-- eureka server: 提供服务发现与服务注册 -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
        </dependency>
    </dependencies>

    <!--
        SpringBoot的Maven插件, 能够以Maven的方式为应用提供SpringBoot的支持，可以将
        SpringBoot应用打包为可执行的jar或war文件, 然后以通常的方式运行SpringBoot应用
     -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

在shop-eureka模块的java目录下新建包com.syg.demo，创建启动类EurekaApplication

```java
package com.syg.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@EnableEurekaServer
@SpringBootApplication
public class EurekaApplication {

    public static void main(String[] args) {
        SpringApplication.run(EurekaApplication.class, args);
    }
}
```

在shop-eureka模块的resources目录下新建application.yml，编写相关配置

```yaml
spring:
  application:
    name: shop-eureka

server:
  port: 8000

eureka:
  instance:
    hostname: localhost
  client:
    # 标识是否从 Eureka Server 获取注册信息, 默认是 true. 如果这是一个单节点的 Eureka Server
    # 不需要同步其他节点的数据, 设置为 false
    fetch-registry: false
    # 是否将自己注册到 Eureka Server, 默认是 true. 由于当前应用是单节点的 Eureka Server
    # 需要设置为 false
    register-with-eureka: false
    # 设置 Eureka Server 所在的地址, 查询服务和注册服务都需要依赖这个地址
    service-url:
      defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
```

运行启动类EurekaApplication，在浏览器中访问此地址：http://localhost:8000/，可以看到Eureka Server模块搭建成功

![]( http://images.simplesay.top/book/image-20200902203532499.png)

## 升华

