# SpringBoot边学边用（四）SpringBoot整合thymeleaf模板引擎

## 什么是模板引擎？

通过下图可以很容易理解，模板引擎就是将数据绑定到静态页面模板中，并输出绑定数据后的页面

![]( http://images.simplesay.top/book/image-20200818202655131.png)

相对于JSP、Velocity、Freemarker等模板引擎，SpringBoot推荐的Thymeleaf语法更简单，功能更强大

## 添加项目依赖

在项目pom.xml文件<dependencies></dependencies>标签内添加依赖：

```xml
        <!--thymeleaf-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
```

## 编写相关配置

打开resources目录下application.properties文件，添加如下配置：

```properties
#thymeleaf设置
#关闭缓存
spring.thymeleaf.cache=false
#指定thymeleaf模板路径
spring.thymeleaf.prefix=classpath:/templates/
#指定字符集编码
spring.thymeleaf.encoding=utf-8
# js ,css 等静态文件路径
spring.mvc.static-path-pattern=/static/**
```

## 创建静态页面

在resources/templates目录下新建静态页面

![]( http://images.simplesay.top/book/image-20200818200627116.png)

在html页面中 引入thymeleaf，使用th:text 在标签内设置文本内容，使用${}调用在控制器中绑定的数据，具体代码如下：

```html
<!DOCTYPE html>
<!--将默认的头 <html lang="en"> 引入thymeleaf-->
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table border="1">
    <tr>
        <td>编号</td>
        <td>姓名</td>
        <td>职业</td>
        <td>手机号</td>
    </tr>
    <tr>
        <td th:text="${customer.id}"></td>
        <td th:text="${customer.username}"></td>
        <td th:text="${customer.job}"></td>
        <td th:text="${customer.phone}"></td>
    </tr>
</table>
</body>
</html>
```

## 编写控制器代码

可以修改上节内容中的CustomerController控制器，需要将@RestController注解改为@Controller，这样才可以返回静态页面，对应的findCustomerById方法类型改为String，添加model参数，用于绑定查询到的customer数据，最后返回页面名称（不带.html后缀）

```java
package com.syg.demo.controller;

import com.syg.demo.po.Customer;
import com.syg.demo.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class CustomerController {

    @Autowired
    private CustomerService customerService;

    @GetMapping("/findCustomerById")
    public String findCustomerById(Integer id, Model model){
        Customer customer =  customerService.findCustomerById(id);
        model.addAttribute("customer",customer);
        return "Customer";
    }
}
```

## 访问测试

通过浏览器访问路由：http://localhost:8081/findCustomerById?id=1

此时返回的结果填充在表格中

![]( http://images.simplesay.top/book/image-20200818204035372.png)

**阅读更多技术文章，及时获取内容更新，请扫码关注微信公众号-大数据School！**

![](http://images.simplesay.top/book/wechat.png)
欢迎评论区留下你的精彩评论~
觉得文章不错可以分享到朋友圈让更多的小伙伴看到哦~

客官！在看一下呗