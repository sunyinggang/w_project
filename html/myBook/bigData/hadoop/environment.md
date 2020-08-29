# 线上服务器Hadoop集群环境搭建

## 一 、前期准备（公共配置）

> 说明：需要三台线上服务器（1核2G的基础配置即可）  
> 这里假设此三台服务器别名为hadoop101、hadoop102、hadoop103  
> 公共配置要在三台服务器中都要进行配置

### 1. 配置network

#### 打开network配置文件

  `vim /etc/sysconfig/network`

#### 书写配置，然后保存退出

  ```bash
    PEERNTP=no
    #同理在hadoop102服务器中配置为HOSTNAME=hadoop102，hadoop103同理
    HOSTNAME=hadoop101
  ```

### 2.配置hosts

#### 打开hosts配置文件

`vim /etc/hosts`

#### 配置hosts，然后保存退出

```bash
  #在hadoop101上，配置hosts文件时使用的是hadoop101的私网ip
  # 使用命令ifconfig -a查看内网ip
  xxx.xx.xx.xx hadoop101

  #配置hadoop102的公网ip
  xxx.xx.xx.xx hadoop102

  #配置hadoop103的公网ip
  xxx.xx.xx.xx hadoop103
  
  #同理在hadoop102中配置hosts时使用hadoop102的私有ip，hadoop101与hadoop103的公有ip；hadoop103同理
```

### 3.验证配置

在三台服务器上依次执行一下步骤，验证是否配置成功

```bash
[root@hadoop101 ~]$ ping hadoop101
[root@hadoop101 ~]$ ping hadoop102
[root@hadoop101 ~]$ ping hadoop103
```

### 4.创建一个普通用户

#### 新建用户

```bash
[root@hadoop101 ~]$ useradd hadoop #新建一个用户hadoop
[root@hadoop101 ~]$ passwd hadoop #为hadoop用户创建密码
```

#### 将该用户写入sudoers文件中

>为什么写入到sudoers文件中？  
>方便执行sudo命令。sudo命令的执行流程是: 当前用户转换到root, 然后以root身份执行命令, 执行完成后, 直接退回到当前用户

``` bash
vim /etc/sudoers
```

```bash
#在root ALL=(ALL)  ALL添加
#代表每次使用sudo命令的时候不提示你输入根密码
hadoop  ALL=(ALL) NOPASSWD:ALL

# 保存时wq!强制保存
```

### 5.创建用户工作目录

```bash
#在/opt目录下创建两个文件夹module和software，并把所有权赋给hadoop
#software用与存放软件安装包文件，module则是软件安装目录
[root@hadoop101 ~]$ mkdir /opt/module /opt/software
[root@hadoop101 ~]$ chown hadoop:hadoop /opt/module /opt/software
```

### 6.永久修改主机名

```bash
[root@localhost ~]$ hostnamectl --static set-hostname hadoop101 #hadoop101服务器中
[root@localhost ~]$ hostnamectl --static set-hostname hadoop102 #hadoop102服务器中
[root@localhost ~]$ hostnamectl --static set-hostname hadoop103 #hadoop103服务器中

[root@localhost ~]$ reboot -f #每个主机都要重启才能生效
[root@hadoop101 ~]$ hostnamectl #查看是否生效
```

## 二 、JDK与Hadoop的安装

>注意：以下操作只需在hadoop101主机中进行

### 1.下载软件包

下载jdk1.8，进入[下载地址](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)，复制下载目录后，下载到hadoop101主机中

```bash
[root@hadoop101 ~]$ cd /opt/software
[hadoop@hadoop101 software]$ wget https://download.oracle.com/otn/java/jdk/8u251-b08/3d5a2bb8f8d4428bbe94aed7ec7ae784/jdk-8u251-linux-x64.tar.gz?AuthParam=1592397487_784064cf4a36bbbe87ea8eace28d38d2 #下载jdk

[hadoop@hadoop101 software]$ wget https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz #下载hadoop
```

### 2.解压安装JDK

#### 解压JDK到/opt/module目录下

```bash
[hadoop@hadoop101 software]$ tar -zxvf jdk-8u251-linux-x64.tar.gz -C /opt/module/
```

#### 配置JDK环境变量

##### 进入到jdk文件目录，获取JDK路径

```bash
[hadoop@hadoop101 jdk1.8.0_251]$ pwd
/opt/module/jdk1.8.0_251
```

##### 打开/etc/profile文件

```bash
[hadoop@hadoop101 software]$ sudo vi /etc/profile
```

##### 在profile文件末尾添加JDK路径，并保存退出

```bash
#JAVA_HOME
export JAVA_HOME=/opt/module/jdk1.8.0_251
export PATH=$PATH:$JAVA_HOME/bin
```

##### 让修改后的文件生效

```bash
[hadoop@hadoop101 jdk1.8.0_251]$ source /etc/profile
```

#### 测试JDK是否安装成功

```bash
[hadoop@hadoop101 jdk1.8.0_251]$ java -version
java version "1.8.0_251"
```

>注意：重启（如果java -version可以用就不用重启）

```bash
[hadoop@hadoop101 jdk1.8.0_251]$ sync
[hadoop@hadoop101 jdk1.8.0_251]$ sudo reboot
```

### 3.安装Hadoop

#### 进入到Hadoop安装包路径下,解压安装文件到/opt/module下面

```bash
[hadoop@hadoop101 software]$ tar -zxvf hadoop-2.7.7.tar.gz -C /opt/module/
```

#### 将Hadoop添加到环境变量

##### 获取Hadoop安装路径

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ pwd
/opt/module/hadoop-2.7.7
```

##### 再次打开打开/etc/profile文件

[hadoop@hadoop101 hadoop-2.7.7]$ sudo vi /etc/profile

##### 在profile文件末尾添加环境变量，并保存退出

```bash
##HADOOP_HOME
export HADOOP_HOME=/opt/module/hadoop-2.7.7
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
```

##### 让修改后的文件生效

```bash
[hadoop@ hadoop101 hadoop-2.7.7]$ source /etc/profile
```

#### 测试是否安装成功

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ hadoop version
Hadoop 2.7.7
```

>注意：重启（如果Hadoop命令不能用再重启）

```bash
[hadoop@hadoop101 jdk1.8.0_251]$ sync
[hadoop@hadoop101 jdk1.8.0_251]$ sudo reboot
```

## 三、编写集群分发脚本

### 1.安装rsync

```bash
[hadoop@hadoop101 jdk1.8.0_251]$ sudo yum -y install rsync
```

### 2.在/home/atguigu目录下创建bin目录，并在bin目录下xsync创建文件

```bash
[hadoop@hadoop101 ~]$ mkdir bin
[hadoop@hadoop101 ~]$ cd bin/
[hadoop@hadoop101 bin]$ touch xsync
[hadoop@hadoop101 bin]$ vi xsync
```

### 3.在该文件中编写如下代码

```bash
#!/bin/bash
#1 获取输入参数个数，如果没有参数，直接退出
pcount=$#
if ((pcount==0)); then
echo no args;
exit;
fi

#2 获取文件名称
p1=$1
fname=`basename $p1`
echo fname=$fname

#3 获取上级目录到绝对路径
# cd –P是当存在软连接时，调转到软连接所指定的源文件目录
pdir=`cd -P $(dirname $p1); pwd`
echo pdir=$pdir

#4 获取当前用户名称
user=`whoami`

#5 循环
for((host=102; host<104; host++)); do
        echo ------------------- hadoop$host --------------
        rsync -av $pdir/$fname $user@hadoop$host:$pdir
done
```

### 4.修改脚本 xsync 具有执行权限

```bash
[hadoop@hadoop101 bin]$ chmod 777 xsync
```

### 5.调用脚本，形式：xsync 文件名称

```bash
[hadoop@hadoop101 bin]$ xsync /home/atguigu/bin
#遇到提示直接yes，然后输入其他主机的密码
```

>注意：如果将xsync放到/home/atguigu/bin目录下仅在hadoop用户下才能使用，想要所有用户都可以使用xsync命令，就将xsync移动到/usr/local/bin目录下

### 6.将xsync复制到/bin目录下，并进行分发

>因为后期会传输某些系统配置文件，所以讲xsync放到root用户的bin下，方便使用`sudo xsync`命令

```bash
[hadoop@hadoop101 bin]$ sudo cp xsync /bin
[hadoop@hadoop101 bin]$ cd /bin
[hadoop@hadoop101 bin]$ sudo xsync xsync
```

## 四、集群配置

### 1.集群部署规划

|  | hadoop101 | hadoop102 | hadoop103 |
| :----: | :----: | :----: | :----: |
| HDFS | NameNode  DataNode | DataNode | SecondaryNameNode  DataNode|
|YARN | NodeManager | ResourceManager  NodeManager | NodeManager |

### 2.文件拷贝

```bash
[atguigu@hadoop101 module]$ cd /opt/module #进入到安装目录
[atguigu@hadoop101 module]$ xsync hadoop-2.7.7 #拷贝hadoop
[atguigu@hadoop101 module]$ xsync jdk1.8.0_251/ #拷贝jdk
[atguigu@hadoop101 module]$ sudo xsync /etc/profile  #拷贝环境配置文件,注意要使用sudo，输入的密码是root用户密码
# 在hadoop102与hadoop103中更新配置文件
[hadoop@hadoop101 module]$  source /etc/profile #使更新后的环境配置文件生效
# 完成后可输入hadoop、java测试是否生效
```

> 注意：过程会比较慢，也可以按照：二、JDK与Hadoop的安装中第一步直接在hadoop102与hadoop103中下载hadoop与jdk

### 2.配置集群

#### 核心配置文件

##### 进入到hadoop配置文件目录中

```bash
[atguigu@hadoop101 hadoop]$ cd /opt/module/hadoop-2.7.7/etc/hadoop
```

##### 配置core-site.xml

```bash
[hadoop@hadoop101 hadoop]$ vi core-site.xml
```

##### 在该文件中编写如下配置

```bash
<configuration>
<!-- 指定HDFS中NameNode的地址 -->
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://hadoop101:9000</value>
</property>

<!-- 指定Hadoop运行时产生文件的存储目录 -->
<property>
  <name>hadoop.tmp.dir</name>
  <value>/opt/module/hadoop-2.7.7/data/tmp</value>
</property>
</configuration>
```

#### HDFS配置文件

##### 配置hadoop-env.sh

```bash
[hadoop@hadoop101 hadoop]$ vi hadoop-env.sh
# 文件内添加如下配置
export JAVA_HOME=/opt/module/jdk1.8.0_251
```

##### 配置hdfs-site.xml

```bash
[hadoop@hadoop101 hadoop]$ vi hdfs-site.xml
```

##### 在该文件中编写如下配置

```bash
<property>
  <name>dfs.replication</name>
  <value>3</value>
</property>

<!-- 指定Hadoop辅助名称节点主机配置 -->
<property>
  <name>dfs.namenode.secondary.http-address</name>
  <value>hadoop103:50090</value>
</property>
```

#### YARN配置文件

##### 配置yarn-env.sh

```bash
[hadoop@hadoop101 hadoop]$ vi yarn-env.sh
export JAVA_HOME=/opt/module/jdk1.8.0_251
```

##### 配置yarn-site.xml

```bash
[hadoop@hadoop101 hadoop]$ vi yarn-site.xml
```

##### 在该文件中增加如下配置

```bash
<!-- Reducer获取数据的方式 -->
<property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
</property>

<!-- 指定YARN的ResourceManager的地址 -->
<property>
  <name>yarn.resourcemanager.hostname</name>
  <value>hadoop102</value>
</property>
```

#### MapReduce配置文件

##### 配置mapred-env.sh

```bash
[hadoop@hadoop101 hadoop]$ vi mapred-env.sh
export JAVA_HOME=/opt/module/jdk1.8.0_251
```

##### 配置mapred-site.xml

```bash
[hadoop@hadoop101 hadoop]$ cp mapred-site.xml.template mapred-site.xml
[hadoop@hadoop101 hadoop]$ vi mapred-site.xml
```

##### 在该文件中增加如下配置

```bash
<!-- 指定MR运行在Yarn上 -->
<property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
</property>
```

### 3.在集群上分发配置好的Hadoop配置文件

```bash
[hadoop@hadoop101 hadoop]$ xsync /opt/module/hadoop-2.7.7/
```

### 4.查看文件分发情况

```bash
# 在hadoop102与hadoop103中查看是否分发成功
[atguigu@hadoop103 hadoop]$ cat /opt/module/hadoop-2.7.7/etc/hadoop/core-site.xml
```

## 五、集群单点启动

### 1.如果集群是第一次启动，需要格式化NameNode

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ hdfs namenode -format
```

### 2.在hadoop101上启动NameNode

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ hadoop-daemon.sh start namenode
[hadoop@hadoop101 hadoop-2.7.7]$ jps
5504 Jps
5435 NameNode
```

### 3.在hadoop101、hadoop102以及hadoop103上分别启动DataNode

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ hadoop-daemon.sh start datanode
[hadoop@hadoop101 hadoop-2.7.7]$ jps
5604 Jps
5435 NameNode
5532 DataNode
[hadoop@hadoop102 hadoop-2.7.7]$ hadoop-daemon.sh start datanode[hadoop@hadoop102 hadoop-2.7.7]$ jps
7127 Jps
7021 DataNode
[hadoop@hadoop103 hadoop-2.7.7]$ hadoop-daemon.sh start datanode
[hadoop@hadoop103 hadoop-2.7.7]$ jps
30146 DataNode
30298 Jps
```

#### 4.运行效果

## 六、群起集群

### 1.SSH无密登录配置（在hadoop101中进行配置）

#### 生成公钥和私钥

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ ssh-keygen -t rsa
```

#### 将公钥拷贝到要免密登录的目标机器上

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ cd /home/atguigu/.ssh
[hadoop@hadoop101 hadoop-2.7.7]$ ssh-copy-id hadoop101
[hadoop@hadoop101 hadoop-2.7.7]$ ssh-copy-id hadoop102
[hadoop@hadoop101 hadoop-2.7.7]$ ssh-copy-id hadoop103
```

>注意：还需要在hadoop101上采用root账号，配置一下无密登录到hadoop101、hadoop102、hadoop103  
还需要在hadoop102上采用atguigu账号配置一下无密登录到hadoop101、hadoop102、hadoop103服务器上

### 2.群起配置

#### 配置slaves

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ cd /opt/module/hadoop-2.7.7/etc/hadoop
[hadoop@hadoop101 hadoop]$ vi slaves
```

#### 修改文件内容

```bash
#该文件中添加的内容结尾不允许有空格，文件中不允许有空行
hadoop101
hadoop102
hadoop103
```

#### 同步所有节点配置文件

```bash
[hadoop@hadoop101 hadoop]$ xsync slaves
```

### 3.停止之前启动的namenode与datanode

#### hadoop101中

```bash
[hadoop@hadoop101 hadoop]$ hadoop-daemon.sh stop namenode
[hadoop@hadoop101 hadoop]$ hadoop-daemon.sh stop datanode
```

#### hadoop102中

```bash
[hadoop@hadoop102 hadoop]$ hadoop-daemon.sh stop datanode
```

#### hadoop103中

```bash
[hadoop@hadoop103 hadoop]$ hadoop-daemon.sh stop datanode
```

### 4.整体启动/停止HDFS

#### 在hadoop101中执行启动

```bash
[hadoop@hadoop101 hadoop]$ start-dfs.sh
```

#### 如果想要关闭HDFS，执行如下命令

```bash
[hadoop@hadoop101 hadoop]$ stop-dfs.sh
```

### 5.整体启动/停止YARN

#### 在hadoop102中执行启动

```bash
[hadoop@hadoop102 hadoop]$ start-yarn.sh
```

#### 如果想要关闭YARN，执行如下命令

```bash
[hadoop@hadoop102 hadoop]$ stop-yarn.sh
```

>在这里回答两个问题：  
>1.为什么要配置ssh免密登陆？  
>方便在hadoop101中执行群起HDFS的时候，不需要再次输入hadoop102与hadoop103主机用户密码  
>2.为什么也要在hadoop102中主动配置无密登录？为什么在hadoop102中群起YARN？  
>因为我们之前部署集群配置时由YARN启动的ResourceManager要部署在hadoop102中，所以在hadoop102中启动YARN，并无需在集群部署过程中输入hadoop101与hadoop103的用户密码

### 6.查看YARN是否启动成功

访问：`http://hadoop102:8088/`

界面：

## 七、配置历史服务器与日志聚集


### 1.配置历史服务器

>为了查看程序的历史运行情况，需要配置一下历史服务器

```bash
[hadoop@hadoop101 hadoop]$ cd /opt/module/hadoop-2.7.7/etc/hadoop
[hadoop@hadoop101 hadoop]$ vi mapred-site.xml
```

#### 在文件中增加如下配置，将hadoop103配置为历史服务器

```bash
<!-- 历史服务器端地址 -->
<property>
<name>mapreduce.jobhistory.address</name>
<value>hadoop103:10020</value>
</property>
<!-- 历史服务器web端地址 -->
<property>
    <name>mapreduce.jobhistory.webapp.address</name>
    <value>hadoop103:19888</value>
</property>
```

### 2.配置日志的聚集

>日志聚集概念：应用运行完成以后，将程序运行日志信息上传到HDFS系统上。  
日志聚集功能好处：可以方便的查看到程序运行详情，方便开发调试。

```bash
[hadoop@hadoop101 hadoop]$ cd /opt/module/hadoop-2.7.7/etc/hadoop
[hadoop@hadoop101 hadoop]$ vi mapred-site.xml
```

#### 在文件中增加如下配置

```bash
<!-- 日志聚集功能使能 -->
<property>
<name>yarn.log-aggregation-enable</name>
<value>true</value>
</property>

<!-- 日志保留时间设置7天 -->
<property>
<name>yarn.log-aggregation.retain-seconds</name>
<value>604800</value>
</property>
```

### 3.配置文件同步

```bash
[hadoop@hadoop101 hadoop]$ cd /opt/module/hadoop-2.7.7
[hadoop@hadoop101 hadoop-2.7.7]$ xsync etc/
```

### 4.重新启动HDFS与YARN，使配置文件生效

```bash
[hadoop@hadoop101 hadoop-2.7.7]$ stop-dfs.sh
[hadoop@hadoop101 hadoop-2.7.7]$ start-dfs.sh
```

```bash
[hadoop@hadoop102 hadoop-2.7.7]$ stop-yarn.sh
[hadoop@hadoop102 hadoop-2.7.7]$ start-yarn.sh
```

```bash
[hadoop@hadoop103 hadoop-2.7.7]$ mr-jobhistory-daemon.sh start historyserver
```
