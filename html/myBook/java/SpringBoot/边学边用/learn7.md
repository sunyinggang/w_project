# SpringBoot边学边用（七）SpringBoot单元测试

> 编写单元测试可以帮助开发人员编写高质量的代码，减少Bug，便于重构；Spring Boot提供了一些注解和工具去帮助开发者测试他们的应用，在Spring Boot中开启单元测试只需要引入spring-boot-starter-test即可，其包含了一些主流的测试库

## 添加项目依赖

在项目pom.xml文件<dependencies></dependencies>标签内添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
</dependency>
```

## 创建单元测试类

在项目src/test目录下，存在新建项目时自动创建的入口类的测试类，接下来我们测试CustomerServiceImpl中的函数方法，所以在demo下新建包service/impl，然后创建对应的CustomerServiceImplTests测试类

![]( http://images.simplesay.top/book/image-20200826214634480.png)



## 添加注解

一个标准的SpringBoot测试用例应该包含两个注解：

- @SpringBootTest：意思是带有SpringBoot支持的引导程序
- @RunWith(SpringRunner.class)：告诉JUnit运行使用Spring的测试支持

```java
package com.syg.demo.service.impl;

import com.syg.demo.dao.CustomerMapper;
import com.syg.demo.po.Customer;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest
@RunWith(SpringRunner.class)
public class CustomerServiceImplTests {
    
    @Autowired
    private CustomerMapper customerMapper;
    //查询客户
    //要测试的方法上添加@Test注解
    @Test
    public void findCustomerById(){
        Customer custom = this.customerMapper.selectByPrimaryKey(1);
        System.out.println(custom);
    }
}
```

**注意：单元测试方法为void类型，这里将查询结果在控制台输出**

## 运行单元测试方法

在带有@Test注解的左侧可以直接点击运行

![]( http://images.simplesay.top/book/image-20200826215106637.png)

可以在控制台中查看到输出结果，即通过主键查询数据方法成功

![]( http://images.simplesay.top/book/image-20200826215223703.png)



**阅读更多技术文章，及时获取内容更新，请扫码关注微信公众号-大数据School！**

![](http://images.simplesay.top/book/wechat.png)
欢迎评论区留下你的精彩评论~
觉得文章不错可以分享到朋友圈让更多的小伙伴看到哦~

同学！在看一下呗