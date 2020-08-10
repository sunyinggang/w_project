# 线上服务器HDFS-HA集群环境搭建

## 一、配置HDFS-HA集群

### 1.关闭之前的hadoop集群环境

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ stop-dfs.sh
[hadoop@hadoop102 hadoop-2.7.7]$ stop-yarn.sh
[hadoop@hadoop103 hadoop-2.7.7]$ mr-jobhistory-daemon.sh stop historyserver
```

### 2.在/opt/module/目录下创建一个ha文件夹

```bash
[hadoop@hadoop101 ~]$ cd /opt/module/
[hadoop@hadoop101 module]$ mkdir ha
```

### 3.将/opt/module/下的hadoop-2.7.7拷贝到/opt/module/ha目录下

```bash
[hadoop@hadoop101 module]$ cp -r hadoop-2.7.7/ /opt/module/ha/
[hadoop@hadoop101 hadoop-2.7.7]$ cd /opt/module/ha/hadoop-2.7.7
[hadoop@hadoop101 hadoop-2.7.7]$ rm -rf data logs #删除之前运行时创建的数据节点
```

### 4.配置hadoop-env.sh

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ cd etc/hadoop
[hadoop@hadoop101 hadoop]$ vim hadoop-env.sh
```

#### 配置JAVA_HOME

```bash
export JAVA_HOME=/opt/module/jdk1.8.0_251
```

### 5.配置core-site.xml

```bash
[hadoop@hadoop101 hadoop]$ vim core-site.xml
```

#### core-site.xml配置如下内容

```bash
#删除旧配置，换成下面新的
<configuration>
<!-- 把两个NameNode）的地址组装成一个集群mycluster -->
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://mycluster</value>
  </property>

  <!-- 指定hadoop运行时产生文件的存储目录 -->
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/opt/module/ha/hadoop-2.7.7/data/tmp</value>
  </property>
</configuration>
```

### 6.配置hdfs-site.xml

```bash
[hadoop@hadoop101 hadoop]$ vim hdfs-site.xml
```

#### hdfs-site.xml配置如下内容

```bash
<configuration>
  <!-- 完全分布式集群名称 -->
  <property>
    <name>dfs.nameservices</name>
    <value>mycluster</value>
  </property>

  <!-- 集群中NameNode节点都有哪些 -->
  <property>
    <name>dfs.ha.namenodes.mycluster</name>
    <value>nn1,nn2</value>
  </property>

  <!-- nn1的RPC通信地址 -->
  <property>
    <name>dfs.namenode.rpc-address.mycluster.nn1</name>
    <value>hadoop101:9000</value>
  </property>

  <!-- nn2的RPC通信地址 -->
  <property>
    <name>dfs.namenode.rpc-address.mycluster.nn2</name>
    <value>hadoop102:9000</value>
  </property>

  <!-- nn1的http通信地址 -->
  <property>
    <name>dfs.namenode.http-address.mycluster.nn1</name>
    <value>hadoop101:50070</value>
  </property>

  <!-- nn2的http通信地址 -->
  <property>
    <name>dfs.namenode.http-address.mycluster.nn2</name>
    <value>hadoop102:50070</value>
  </property>

  <!-- 指定NameNode元数据在JournalNode上的存放位置 -->
  <property>
    <name>dfs.namenode.shared.edits.dir</name>
  <value>qjournal://hadoop101:8485;hadoop102:8485;hadoop103:8485/mycluster</value>
  </property>

  <!-- 配置隔离机制，即同一时刻只能有一台服务器对外响应 -->
  <property>
    <name>dfs.ha.fencing.methods</name>
    <value>sshfence</value>
  </property>

  <!-- 使用隔离机制时需要ssh无秘钥登录-->
  <property>
    <name>dfs.ha.fencing.ssh.private-key-files</name>
    <value>/home/atguigu/.ssh/id_rsa</value>
  </property>

  <!-- 声明journalnode服务器存储目录-->
  <property>
    <name>dfs.journalnode.edits.dir</name>
    <value>/opt/module/ha/hadoop-2.7.7/data/jn</value>
  </property>

  <!-- 关闭权限检查-->
  <property>
    <name>dfs.permissions.enable</name>
    <value>false</value>
  </property>

  <!-- 访问代理类：client，mycluster，active配置失败自动切换实现方式-->
  <property>
    <name>dfs.client.failover.proxy.provider.mycluster</name>
    <value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
  </property>
</configuration>
```

### 7.拷贝配置好的hadoop环境到其他节点

```bash
[hadoop@hadoop101 hadoop]$ cd /opt/module/
[hadoop@hadoop101 module]$ xsync ha
```

>注意：如果过程很慢可以在hadoop102、hadoop103中执行上述步骤1、2、3，然后仅同步配置文件：

```bash
xsync /opt/module/ha/hadoop-2.7.7/etc/hadoop/
```

## 二、启动HDFS-HA集群

### 1.群起journalnode服务

```bash
[hadoop@hadoop101 hadoop]$ cd /opt/module/ha/hadoop-2.7.7
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/hadoop-daemons.sh start journalnode
```

### 2.在[nn1]上，对其进行格式化，并启动

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hdfs namenode -format
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/hadoop-daemon.sh start namenode
```

### 3.在[nn2]上同目录，同步nn1的元数据信息

```bash
[hadoop@hadoop102 hadoop-2.7.7]$ bin/hdfs namenode -bootstrapStandby
```

### 4.启动[nn2]

```bash
[hadoop@hadoop102 hadoop-2.7.7]$ sbin/hadoop-daemon.sh start namenode
```

### 5.查看web页面显示

### 6.在[nn1]上，启动所有datanode

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/hadoop-daemons.sh start datanode
```

### 7.将[nn1]切换为Active

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hdfs haadmin -transitionToActive nn1
```

### 8.查看是否Active

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hdfs haadmin -getServiceState nn1
```

## 三、配置HDFS-HA自动故障转移

### 1.在hdfs-site.xml中增加如下配置

```bash
<property>
  <name>dfs.ha.automatic-failover.enabled</name>
  <value>true</value>
</property>
```

### 2.在core-site.xml文件中增加如下配置

```bash
<property>
  <name>ha.zookeeper.quorum</name>
  <value>hadoop101:2181,hadoop102:2181,hadoop103:2181</value>
</property>
```

### 3.同步配置

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ xsync /opt/module/ha/hadoop-2.7.7/etc
```

### 4.关闭所有HDFS服务

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/stop-dfs.sh
[hadoop@hadoop101 hadoop-2.7.7]$ rm -rf data logs #三台机器都要执行删除操作
```

### 5.再次群起journalnode服务

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/hadoop-daemons.sh start journalnode
```

### 6.格式化namenode

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hdfs namenode -format
```

### 7.启动Zookeeper集群(如果已启动不需要再次启动）

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ /opt/module/zookeeper-3.4.14/bin/zkServer.sh start
```

### 7.初始化HA在Zookeeper中状态

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/hdfs zkfc -formatZK
[hadoop@hadoop102 hadoop-2.7.7]$ bin/hdfs namenode –bootstrapStandby#同步初始化，在hadoop102同目录执行
```

### 8.启动HDFS服务

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/start-dfs.sh
```

## 四、配置YARN-HA集群

### 1.配置yarn-site.xml

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ cd /opt/module/ha/hadoop-2.7.7
[hadoop@hadoop101 hadoop-2.7.7]$ vim etc/hadoop/yarn-site.xml
```

#### 重写配置内容

```bash
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
    </property>

  <!--启用resourcemanager ha-->
  <property>
    <name>yarn.resourcemanager.ha.enabled</name>
    <value>true</value>
  </property>

  <!--声明两台resourcemanager的地址-->
  <property>
    <name>yarn.resourcemanager.cluster-id</name>
    <value>cluster-yarn1</value>
  </property>

  <property>
    <name>yarn.resourcemanager.ha.rm-ids</name>
    <value>rm1,rm2</value>
  </property>

  <property>
    <name>yarn.resourcemanager.hostname.rm1</name>
    <value>hadoop101</value>
  </property>

  <property>
    <name>yarn.resourcemanager.hostname.rm2</name>
    <value>hadoop102</value>
  </property>

  <!--指定zookeeper集群的地址-->
  <property>
    <name>yarn.resourcemanager.zk-address</name>
    <value>hadoop101:2181,hadoop102:2181,hadoop103:2181</value>
  </property>

  <!--启用自动恢复-->
  <property>
    <name>yarn.resourcemanager.recovery.enabled</name>
    <value>true</value>
  </property>

  <!--指定resourcemanager的状态信息存储在zookeeper集群-->
  <property>
    <name>yarn.resourcemanager.store.class</name>
    <value>org.apache.hadoop.yarn.server.resourcemanager.recovery.ZKRMStateStore</value>
  </property>
</configuration>
```

#### 同步更新其他节点的配置信息

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ xsync etc
```

### 3.启动YARN

#### 在hadoop101中执行

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/start-yarn.sh
```

#### 在hadoop102中执行

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ sbin/yarn-daemon.sh start resourcemanager
```

#### 查看服务状态

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ bin/yarn rmadmin -getServiceState rm1
[hadoop@hadoop101 hadoop-2.7.7]$ bin/yarn rmadmin -getServiceState rm2
```
