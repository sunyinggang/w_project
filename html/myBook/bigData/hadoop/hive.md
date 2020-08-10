# Hive安装部署

## 1.Hive安装及配置

### 下载Hive

```bash
[hadoop@hadoop101 ~]$ cd /opt/software/
[hadoop@hadoop101 software]$ wget http://mirror.bit.edu.cn/apache/hive/hive-2.3.7/apache-hive-2.3.7-bin.tar.gz
```

### 解压到/opt/module/目录下面

```bash
[hadoop@hadoop101 software]$ tar -zxvf apache-hive-2.3.7-bin.tar.gz -C /opt/module/
```

### 修改apache-hive-2.3.7-bin的名称为hive

```bash
[hadoop@hadoop101 module]$ mv apache-hive-2.3.7-bin/ hive
```

### 修改/opt/module/hive/conf目录下的hive-env.sh.template名称为hive-env.sh

```bash
[hadoop@hadoop101 module]$ cd hive/conf
[hadoop@hadoop101 conf]$ mv hive-env.sh.template hive-env.sh
```

### 配置hive-env.sh文件

```bash
[hadoop@hadoop101 conf]$ vim hive-env.sh
```

```bash
#配置HADOOP_HOME路径
export HADOOP_HOME=/opt/module/hadoop-2.7.7
#配置HIVE_CONF_DIR路径
export HIVE_CONF_DIR=/opt/module/hive/conf
```

## 2.Hadoop集群配置

### 必须启动hdfs和yarn

```bash
[hadoop@hadoop101 conf]$ cd /opt/module/hadoop-2.7.7
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/start-dfs.sh
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/start-yarn.sh
```

### 在HDFS上创建/tmp和/user/hive/warehouse两个目录并修改他们的同组权限可写

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hadoop fs -mkdir /tmp
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hadoop fs -mkdir -p /user/hive/warehouse
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hadoop fs -chmod g+w /tmp
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hadoop fs -chmod g+w /user/hive/warehouse
```

## 3.Hive基本操作

### 使用hive自带的内存数据库derby,应该先初始化

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ cd /opt/module/hive
[hadoop@hadoop101 hive]$ bin/schematool  -initSchema -dbType derby
```

### 启动hive

```bash
[hadoop@hadoop101 hive]$ bin/hive
```

### 查看数据库

```bash
hive> show databases;
OK
default
Time taken: 9.187 seconds, Fetched: 1 row(s)
```

### 打开默认数据库

```bash
hive> use default;
OK
Time taken: 0.062 seconds
```

### 显示default数据库中的表

```bash
hive> show tables;
OK
Time taken: 0.103 seconds
```

### 创建一张表

```bash
hive> create table student(id int, name string);
OK
Time taken: 1.914 seconds
```

### 显示数据库中有几张表

```bash
hive> show tables;
OK
student
Time taken: 0.033 seconds, Fetched: 1 row(s)
```

### 查看表的结构

```bash
hive> desc student;
OK
id            int
name          string
Time taken: 0.306 seconds, Fetched: 2 row(s)
```

### 向表中插入数据

```bash
hive> insert into student values(1000,"ss");
```

### 查询表中数据

```bash
hive> select * from student;
```

### 退出hive

```bash
hive> quit;
```