# Maven

## Maven相关特性

### 传递依赖与排除依赖

传递依赖：如果我们的项目引用了一个jar包，而该jar包又引用了其他jar包。那么，在默认情况下编译项目时，Maven会把直接引用和间接引用的jar包都下载到本地（.../.m2/repository）

排除依赖：如果我们只想下载直接引用的jar包，那么需要在pom.xml中给出需要排除的jar包，在<exclusions> 标签下可以添加多个<exclusion>  用来添加需要排除的jar包，示例代码如下：

```xml
<dependency>    
    <groupId>org.apache.hbase</groupId>
    <artifactId>hbase</artifactId>
    <version>0.94.17</version> 
    <exclusions>  
         <exclusion>     
             <groupId>commons-logging</groupId>        
             <artifactId>commons-logging</artifactId>  
         </exclusion>  
    </exclusions>  
</dependency>
```

### 依赖冲突

**说明：若项目中多个jar同时引用了相同的jar时会产生依赖冲突，但Maven采用了两种避免冲突的策略，使得在Maven中是不存在依赖冲突的**

#### 短路优先

谁离得最近就使用谁的依赖jar包

例如：

A中的 commons-io的版本为2.4

B中的commons-io的版本为2.0

C中依赖于B,B依赖于A

即：C到达A为：C->B->A        C到达B为：C->B

则C的junit的包为2.0版本，因为C->b依赖的短路优先

#### 声明优先

若引用路径长度相同时，在pom.xml中谁先被声明，就使用谁

例如：C到达A为C->A ，C到达B为C->B，但是在C的pom.xml文件中先添加了A的依赖，所以这里使用A的版本

```xml
<dependency>
    <groupId>org.lonecloud.A</groupId>
    <artifactId>A</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</dependency>
<dependency>
    <groupId>org.lonecloud.B</groupId>
    <artifactId>B</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</dependency>
```

### 多模块项目聚合

```json

└─ SYG-Parent
    ├─SYG-Model
    │  ├─src
    │  │─pom.xml (JAR)
    │  
    │─SYG-Dao
    │  ├─src
    │  │─pom.xml (JAR)
    │  
    │─SYG-Service
    │  ├─src
    │  │─pom.xml (JAR)
    │
    └─ pom.xml           
```

父模块pom文件的配置

packaging类型必须是pom，聚合子模块使用modules标签

```xml
<groupId>com.syg</groupId>
<artifactId>SYG-Parent</artifactId>
<packaging>pom</packaging>
<version>0.0.1-SNAPSHOT</version>
<modules>
      <module>SYG-Model</module>
      <module>SYG-Dao</module>
      <module>SYG-Service</module>
</modules>
```

子模块需要在pom中声明父模块：使用 <parent>标签，这里以SYG-Model模块为例

```xml
    <parent>
			<groupId>com.syg</groupId>
			<artifactId>SYG-Model</artifactId>
			<version>1.0-SNAPSHOT</version>
	</parent>
```

父模块统一管理依赖包，使用<dependencyManagement>标签

```xml
<!-- 标识SpringCloud的版本 -->
<dependencyManagement>
      <dependencies>
          <dependency>
              <groupId>org.springframework.cloud</groupId>
			  <artifactId>spring-cloud-dependencies</artifactId>
			  <version>${spring-cloud.version}</version>
              <type>pom</type>
              <scopy>import</scopy>
		  </dependency>
       </dependencies>
</dependencyManagement>
```





Idea中配置Maven

![](http://images.simplesay.top/book/image-20200817175738830.png)



```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                          https://maven.apache.org/xsd/settings-1.0.0.xsd">
      <mirrors>
        <mirror>  
            <id>alimaven</id>  
            <name>aliyun maven</name>  
            <url>https://maven.aliyun.com/repository/public</url>
            <mirrorOf>central</mirrorOf>          
        </mirror>  
      </mirrors>
</settings>
```



