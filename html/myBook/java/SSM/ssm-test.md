# SSM整合测试

完成了SSM框架整合环境的搭建工作，就已经完成了这三个框架大部分的整合工作。接下来，以查询客户信息为例，来讲解SSM框架的整合开发，其具体实现步骤如下。

## 创建数据表

在test数据库（依据db.properties配置文件的数据库）中创建customer数据表，并导入测试数据

```mysql
CREATE TABLE `customer` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `job` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES ('1', '小明', '医生','13567344567');
INSERT INTO `customer` VALUES ('2', '小红', '教师','18756576778');
```

## 在com.syg.po包中

创建持久化类Customer：

```java
package com.syg.po;

public class Customer {
    private Integer id;
    private String username;
    private String job;
    private String phone;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}
```

## 在com.syg.dao包中

在包中创建接口CustomerDao：

```java
package com.syg.dao;

import com.syg.po.Customer;

public interface CustomerDao {
    public Customer findCustomerById(Integer id);
}
```

并在resources/mapper下创建对应的映射文件CustomerDao.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.syg.dao.CustomerDao">
    <select id="findCustomerById" parameterType="Integer" resultType="Customer">
        select * from customer where id = #{id}
    </select>
</mapper>
```

## 在com.syg.service包中

创建接口CustomerService，并在CustomerService中定义通过id查询客户的方法:

```java
package com.syg.service;

import com.syg.po.Customer;

public interface CustomerService {
    public Customer findCustomerById(Integer id);
}
```

## 在com.syg.service.impl包中

在包中创建CustomerService接口的实现类CustomerServiceImpl

```java
package com.syg.service.impl;

import com.syg.dao.CustomerDao;
import com.syg.po.Customer;
import com.syg.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class CustomerServiceImpl implements CustomerService {

    @Autowired
    private CustomerDao customerDao;
    //查询客户
    public Customer findCustomerById(Integer id){
        return this.customerDao.findCustomerById(id);
    }
}
```

## 在com.syg.controller包中

创建用于处理页面请求的控制器类CustomerController

```java
package com.syg.controller;

import com.syg.po.Customer;
import com.syg.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class CustomerController {
    @Autowired
    private CustomerService customerService;

    @RequestMapping("/findCustomerById")
    public String findCustomerById(Integer id, Model model){
        Customer customer = customerService.findCustomerById(id);
        model.addAttribute("customer",customer);
        return "customer";
    }
}
```

## 创建展示页面

在WEB-INF目录下，创建一个jsp文件夹，在该文件夹下创建一个用于展示客户详情的页面文件customer.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>客户信息</title>
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
        <td>${customer.id}</td>
        <td>${customer.username}</td>
        <td>${customer.job}</td>
        <td>${customer.phone}</td>
    </tr>
</table>
</body>
</html>
```

点击运行，在浏览器中访问地址http://localhost:1234/findCustomerById?id=1

![]( http://images.simplesay.top/book/20200807154107.jpg)

## 总结

理清每个包下存放的文件是什么作用