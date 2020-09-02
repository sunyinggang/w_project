# Spring Cloud边学边用（一）为什么要使用Spring Cloud？

在学习SpringCloud之前，我们都会去了解SpringCloud到底是用来做什么的？需要在哪些场景使用？那么接下来通过简单的案例来设定一个SpringCloud使用场景，方便读者理解SpringCloud到底是用来做什么的

## 案例引入

当我们在网上购买商品时，点击购买需要完成在线支付，支付成功后即完成商品购买

由于我们之前学习了SpringBoot，我们可以把这整个购买流程放在一个SpringBoot应用中，但现在我们打算将商品购买与支付分成两个小的应用，即分成两个**微服务**：

![]( http://images.simplesay.top/book/image-20200902105616848.png)

## 创建项目

如果我们继续使用SpringBoot，那么首先我们需要创建两个SpringBoot项目，这里我创建的两个SpringBoot项目的Artifact为buy和pay

在项目pay中，新建控制器PayController，简单的创建一个返回字符串信息的方法，同时修改了application.properties配置文件中端口号为8090

```java
package com.example.pay.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PayController {
    @RequestMapping("/pay")
    public String pay() {
        return "支付成功";
    }
}
```

运行项目，通过浏览器访问

![]( http://images.simplesay.top/book/image-20200902123129880.png)

在项目buy中，新建控制器BuyController，创建一个方法，在方法内调用pay项目中支付测试方法，同时修改了application.properties配置文件中端口号为8088

```java
package com.example.buy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class BuyController {
    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/buy")
    public String buyGoods() {
        ResponseEntity<String> forEntity =
                restTemplate.getForEntity("http://localhost:8090/pay", String.class);
        return forEntity.getBody();
    }
}
```

运行项目，通过浏览器访问

![]( http://images.simplesay.top/book/image-20200902123429151.png)

可以观察到，此时我们调用buy项目中的购买测试方法，方法中成功去调用了pay项目中的支付测试方法，即我们通过SpringBoot实现项目购物功能分为两个微服务，但这是真正的微服务么？

## 存在的问题

上述我们实现了一个简单的分布式应用示例，应用之间通过HTTP进行通信，但是如果我们的支付微服务模块pay改变了项目ip或端口号，那么我们还需要去购买微服务模块buy中做对应的修改，这是比较麻烦的一个过程。当然这只是面临的很小的一个问题，当我们面临访问人数增多时，我们就要考虑如何做负载均衡；当我们的微服务模块增多时，就要考虑有些模块间数据如何进行同步等问题。所以单纯的使用Spring Boot来做微服务开发，面临着许多的问题，所以开发出基于Spring Boo的一系列框架的集合----Spring Cloud框架，专门应用于微服务场景