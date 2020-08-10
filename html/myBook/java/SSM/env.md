# 使用Intellij IDEA搭建SSM项目

## 创建项目

打开Intellij IDEA，点击File -> New -> Project 

![]( http://images.simplesay.top/book/20200806171241.jpg)

左侧选择Maven，右侧勾选Create from archetype，选中webapp模板

![image-20200806171657348](C:\Users\sunyinggang\AppData\Roaming\Typora\typora-user-images\image-20200806171657348.png)

填写GroupId和ArtifactId后，点击next，最后finish完成

![]( http://images.simplesay.top/book/20200806171946.jpg)

## 使用Maven导入jar包

使用Maven加载需要的jar包，因此需要修改pom.xml文件。使用下面的代码将pom.xml文件中<properties>与<dependencies>的标签内容替换掉。

```xml
  <!-- 用来设置版本号 -->
  <properties>
    <srping.version>4.0.2.RELEASE</srping.version>
    <mybatis.version>3.2.8</mybatis.version>
    <slf4j.version>1.7.12</slf4j.version>
    <log4j.version>1.2.17</log4j.version>
    <druid.version>1.0.9</druid.version>
  </properties>
  <!-- 用到的jar包 -->
    <dependencies>
    <!-- 单元测试 -->
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <!-- 表示开发的时候引入，发布的时候不会加载此包 -->
      <scope>test</scope>
    </dependency>

    <!-- spring框架包 -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-test</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-oxm</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-tx</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-jdbc</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-aop</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context-support</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-expression</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-orm</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <!-- spring MVC框架包 -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-web</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>${srping.version}</version>
    </dependency>
    <!-- mybatis框架包 -->
    <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis</artifactId>
      <version>${mybatis.version}</version>
    </dependency>
    <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis-spring</artifactId>
      <version>1.2.2</version>
    </dependency>
    <!-- 数据库驱动 -->
    <dependency>
      <groupId>mysql</groupId>
      <artifactId>mysql-connector-java</artifactId>
      <version>5.1.35</version>
    </dependency>
    <!-- 导入dbcp的jar包，用来在applicationContext.xml中配置数据库 -->
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-dbcp2</artifactId>
      <version>2.1.1</version>
    </dependency>
    <!-- jstl标签类 -->
    <dependency>
      <groupId>jstl</groupId>
      <artifactId>jstl</artifactId>
      <version>1.2</version>
    </dependency>
    <!-- log -->
    <dependency>
      <groupId>log4j</groupId>
      <artifactId>log4j</artifactId>
      <version>${log4j.version}</version>
    </dependency>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>${slf4j.version}</version>
    </dependency>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-log4j12</artifactId>
      <version>${slf4j.version}</version>
    </dependency>
  </dependencies>
```

修改pom.xml文件后，右下角出现提示，选择Import Changes为项目导入jar包

![]( http://images.simplesay.top/book/20200806173059.jpg)

## 创建项目文件

### 创建Sources与Resources

在src/main目录下新建文件夹，创建java与resources文件夹

![]( http://images.simplesay.top/book/20200806173751.jpg)

创建后的目录结构

![]( http://images.simplesay.top/book/20200806173707.png)

点击左上角File -> Project Structure

![]( http://images.simplesay.top/book/20200806174036.jpg)

左侧选择Modules，右侧选中java文件夹，点击Sources；然后选中resources文件夹点击Resources

![]( http://images.simplesay.top/book/20200806174309.jpg)

### 创建项目包

在java目录下右键 -> New -> Package，输入包名

|    com.syg.controller    |     控制器层      |
| :----------------------: | :---------------: |
|     **com.syg.dao**      |     **Dao层**     |
|      **com.syg.po**      |   **持久化层**    |
|   **com.syg.service**    |   **service层**   |
| **com.syg.service.impl** | **service实现层** |

### 创建mapper文件夹

在resources目录下右键 -> New ->Directory，输入文件名mapper

创建后的目录结构如下：

![]( http://images.simplesay.top/book/20200807094649.jpg)

## 添加配置文件

### 配置文件说明

在resource目录下新建如下配置文件：

|       db.properties        |          数据库配置文件          |
| :------------------------: | :------------------------------: |
| **applicationContext.xml** |       **Spring的配置文件**       |
|   **mybatis-config.xml**   |      **MyBatis的配置文件**       |
|    **log4j.properties**    |         **日志配置文件**         |
|     **spring-mvc.xml**     |      **Spring MVC配置文件**      |
|        **web.xml**         | Spring MVC前端控制器配置文件（） |

> 注意：上述表格中web.xml无需创建，只需要对web.xml文件内容进行修改，文件位置：src/main/webapp/WEB-INF/web.xml

### db.properties

```properties
driver=com.mysql.jdbc.Driver
#连接路径，这里的test为创建的数据库名
url=jdbc:mysql://localhost:3306/test?characterEncoding=utf8
#数据库的用户名
username=root
#数据库的密码
password=123456
#定义初始连接数
initialSize=5
#定义最大空闲
maxIdle=30
#定义最小空闲
minIdle=10
```

### applicationContext.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:tx="http://www.springframework.org/schema/tx" xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
                        http://www.springframework.org/schema/beans/spring-beans-3.1.xsd
                        http://www.springframework.org/schema/tx
                        http://www.springframework.org/schema/tx/spring-tx.xsd http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

    <!-- 加载properties文件 -->
    <bean id="propertyConfigurer" class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">
        <property name="location" value="classpath:db.properties"/>
    </bean>

    <!-- 配置数据源 -->
    <bean id="dataSource" class="org.apache.commons.dbcp2.BasicDataSource">
        <property name="driverClassName" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
    </bean>

    <!-- 事务管理器，依赖于数据源 -->
    <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <!--数据库连接池-->
        <property name="dataSource" ref="dataSource"/>
    </bean>

    <!-- 开启事务注解 -->
    <tx:annotation-driven transaction-manager="transactionManager"/>

    <!-- 配置MyBatis工厂sqlSessionFactory -->
    <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
        <!-- 注入数据源 -->
        <property name="dataSource" ref="dataSource"/>
        <!-- 指定MyBatis核心配置文件 -->
        <property name="configLocation" value="classpath:mybatis-config.xml"/>
    </bean>

    <!-- 配置Mapper扫描器 -->
    <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
        <property name="basePackage" value="classpath:mapper/*.xml" />
    </bean>

    <!-- 扫描Service-->
    <context:component-scan base-package="com.syg.service" />
    
</beans>
```

### mybatis-config.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- 设置类的别名 -->
    <typeAliases>
        <package name="com.syg.po" />
    </typeAliases>
</configuration>
```

### log4j.properties

```properties
#日志输出级别
log4j.rootLogger=debug,stdout,D,E

#设置stdout的日志输出控制台
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
#输出日志到控制台的方式，默认为System.out
log4j.appender.stdout.Target = System.out
#设置使用灵活布局
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
#灵活定义输出格式
log4j.appender.stdout.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss,SSS} -[%p]  method:[%c (%rms)] - %m%n
```

### spring-mvc.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/mvc
       http://www.springframework.org/schema/mvc/spring-mvc-3.0.xsd">

    <!-- 配置包扫描器，扫描@Controller注解的类 -->
    <context:component-scan base-package="com.syg.controller"/>

    <!-- 加载SpringMVC注解驱动 -->
    <mvc:annotation-driven />

    <!-- 配置视图解析器 -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/jsp/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
</beans>
```

### web.xml

```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">

  <!--项目的欢迎页，项目运行起来后访问的页面-->
  <welcome-file-list>
    <welcome-file>index.jsp</welcome-file>
  </welcome-file-list>

  <!-- 注册ServletContext监听器，创建容器对象，并且将ApplicationContext对象放到Application域中 -->
  <listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>

  <!-- 指定spring核心配置文件 -->
  <context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>classpath:applicationContext.xml</param-value>
  </context-param>

  <!-- 解决乱码的过滤器 -->
  <filter>
    <filter-name>CharacterEncodingFilter</filter-name>
    <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
    <init-param>
      <param-name>encoding</param-name>
      <param-value>utf-8</param-value>
    </init-param>

    <init-param>
      <param-name>forceEncoding</param-name>
      <param-value>true</param-value>
    </init-param>
  </filter>
  <filter-mapping>
    <filter-name>CharacterEncodingFilter</filter-name>
    <url-pattern>/*</url-pattern>
  </filter-mapping>

  <!-- 配置Spring MVC前端控制器 -->
  <servlet>
    <servlet-name>springmvc</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>classpath:spring-mvc.xml</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
    <async-supported>true</async-supported>
  </servlet>

  <servlet-mapping>
    <servlet-name>springmvc</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping>

</web-app>
```

## 运行项目

运行项目需要配置Tomcat，首先点击IDEA右上角的 Edit Configurations... -> 进入到Run/Debug Configurations界面 -> 点击左上角加号 -> 选择Tomcat Server -> Local进入到Tomcat配置界面，可以在Server中看到基础配置，基本无需修改，若出现8080端口已被占用问题，可以修改HTTP port

然后，选中Deloyment -> 点击右边加号 -> 选中Artifact...

![]( http://images.simplesay.top/book/20200807095433.jpg)

选中第二项配置，点击右下角OK

![]( http://images.simplesay.top/book/20200807095445.jpg)

点击绿色三角启动项目，可以访问到默认页面index.jsp

![]( http://images.simplesay.top/book/20200807100210.jpg)

> 注意：我这里修改了端口号为1234，默认端口为8080

## 总结

学习内容源源不断，环境配置磕磕绊绊