# 线上服务器Zookeeper集群环境搭建

## 一、集群规划

在hadoop101、hadoop102和hadoop103三个节点上部署Zookeeper

## 二、下载并解压安装

### 1.在hadoop01中下载

```bash
[hadoop@hadoop101 ~]$ cd /opt/software
[hadoop@hadoop101 software]$ wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz
```

### 2.解压安装

```bash
[hadoop@hadoop101 software]$ tar -zxvf hadoop-2.7.7.tar.gz -C /opt/module/
```

### 3.分发给hadoop102与hadoop103

```bash
[hadoop@hadoop101 software]$ cd /opt/module/
[hadoop@hadoop101 module]$ xsync zookeeper-3.4.14/
```

>如果分发速度较慢，在hadoop102与hadoop103中同样执行步骤1与步骤2

## 三、配置服务器编号

### 1.在/opt/module/zookeeper-3.4.14/这个目录下创建zkData

```bash
[hadoop@hadoop101 zookeeper-3.4.14]$ mkdir -p zkData
```

### 2.在/opt/module/zookeeper-3.4.14/zkData目录下创建一个myid的文件

```bash
[hadoop@hadoop101 zkData]$ touch myid
```

### 3.编辑myid文件

```bash
[hadoop@hadoop101 zkData]$ vi myid
```

### 4.在文件中添加与server对应的编号

```bash
# hadoop101编号为1，hadoop102编号为2，hadoop103编号为3
1
```

### 5.拷贝配置好的zookeeper到其他机器上

```bash
[hadoop@hadoop101 zkData]$ cd ..
[hadoop@hadoop101 zkData]$ xsync zkData/
```

### 6.并分别在hadoop102、hadoop103上修改myid文件中内容为2、3

## 四、配置zoo.cfg文件

### 1.重命名/opt/module/zookeeper-3.4.14/conf这个目录下的zoo_sample.cfg为zoo.cfg

```bash
[hadoop@hadoop101 zkData]$ cd /opt/module/zookeeper-3.4.14/conf
[hadoop@hadoop101 conf]$ mv zoo_sample.cfg zoo.cfg
```

### 2.打开zoo.cfg文件

```bash
[hadoop@hadoop101 conf]$ vim zoo.cfg
```

#### 修改数据存储路径配置

```bash
dataDir=/opt/module/zookeeper-3.4.14/zkData
```

#### 增加如下配置

```bash
#######################cluster##########################
server.1=hadoop101:2888:3888
server.2=hadoop102:2888:3888
server.3=hadoop103:2888:3888
```

>&emsp;&emsp;配置参数解读:  
>&emsp;&emsp;`server.A=B:C:D`  
>&emsp;&emsp;A是一个数字，表示这个是第几号服务器。集群模式下配置一个文件myid，这个文件在dataDir目录下，这个文件里面有一个数据就是A的值，Zookeeper启动时读取此文件，拿到里面的数据与zoo.cfg里面的配置信息比较从而判断到底是哪个server  
&emsp;&emsp;B是这个服务器的地址  
&emsp;&emsp;C是这个服务器Follower与集群中的Leader服务器交换信息的端口  
&emsp;&emsp;D是万一集群中的Leader服务器挂了，需要一个端口来重新进行选举，选出一个新的Leader，而这个端口就是用来执行选举时服务器相互通信的端口。

### 3.同步zoo.cfg配置文件

```bash
[hadoop@hadoop101 conf]$ xsync zoo.cfg
```

## 四、集群操作

### 1.分别启动Zookeeper

```bash
[hadoop@hadoop101 zookeeper-3.4.14]$ cd /opt/module/zookeeper-3.4.14/
[hadoop@hadoop101 zookeeper-3.4.14]$ bin/zkServer.sh start
[hadoop@hadoop102 zookeeper-3.4.14]$ bin/zkServer.sh start
[hadoop@hadoop103 zookeeper-3.4.14]$ bin/zkServer.sh start
```

>注意：阿里云服务器需要配置安全组，腾讯云不需要

### 2.查看状态

```bash
[atguigu@hadoop101 zookeeper-3.4.14]$ bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper-3.4.14/bin/../conf/zoo.cfg
Mode: follower
[atguigu@hadoop102 zookeeper-3.4.14]$ bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper-3.4.14/bin/../conf/zoo.cfg
Mode: follower
[atguigu@hadoop103 zookeeper-3.4.14]$ bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper-3.4.14/bin/../conf/zoo.cfg
Mode: leader
```
