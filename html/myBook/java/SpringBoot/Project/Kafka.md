# 环境搭建

## Kafka

### 安装Kafka

访问[Kafka官网](http://kafka.apache.org/downloads)，下载已经编译好的Kafka压缩包

![]( http://images.simplesay.top/book/image-20200823155555294.png)

这里给出在centos下的安装过程，这里使用xshell远程连接我的centos服务器（mac下操作命令相同），windows下直接下载解压即可

```json
# 创建软件安装目录
cd /opt
mkdir soft
# 下载kafka
wget https://mirror.bit.edu.cn/apache/kafka/2.6.0/kafka_2.12-2.6.0.tgz
# 解压
tar -zxvf kafka_2.12-2.6.0.tgz
# 进入到解压的软件目录
cd kafka_2.12-2.6.0/
```

查看文件目录

![]( http://images.simplesay.top/book/image-20200823160055808.png)

### 修改配置
```json
# 进入到kafka的软件目录
cd /opt/soft/kafka_2.12-2.6.0/
# 创建日志存放目录
mkdir logs
# 修改配置文件中的broker.id与log.dirs
cd config/
vim server.properties
# 修改kafka唯一标识broker.id
broker.id=1
# 日志文件存放目录：log.dirs
log.dirs=/opt/soft/kafka_2.12-2.6.0/logs
```

### 运行测试

```json
# 进入到kafka目录下
cd /opt/soft/kafka_2.12-2.6.0
# kafka依赖于Zookeeper，先启动Zookeeper
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties 
# 启动kafka服务器
bin/kafka-server-start.sh config/server.properties
```

可以看到成功运行

![image-20200823163934528]( http://images.simplesay.top/book/image-20200823163934528.png)

再打开一个服务器连接窗口，使用jps命令可以看到启动的kafka与zookeeper

**提示：jps命令跟jdk有关，如果不可使用jps命令则需要自行安装jdk**

![image-20200823164609903]( http://images.simplesay.top/book/image-20200823164609903.png)

### Kafka相关命令

```json
# 创建Topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
# 查看已创建的Topic列表
bin/kafka-topics.sh --list --zookeeper localhost:2181
# 启动Consumer消费	
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

再打开一个服务器连接窗口，启动Producer

```json
# 启动Producer发送消息
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

在Producer中输入发送的信息

![image-20200823170749067]( http://images.simplesay.top/book/image-20200823170749067.png)

则在Consumer中可以接收到Producer发送的信息

![image-20200823170721613]( http://images.simplesay.top/book/image-20200823170721613.png)

