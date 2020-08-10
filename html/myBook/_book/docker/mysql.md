# Docker安装Mysql
1. 拉取官方mysql5.7镜像  
  `sudo docker pull mysql:5.7`
2. 在本地创建mysql的映射目录  
   `mkdir -p /root/mysql/data /root/mysql/logs /root/mysql/conf`
3. 运行mysql  
   `docker run -p 3306:3306 --name mysql -v /root/mysql/conf:/etc/mysql/conf.d -v /root/mysql/logs:/logs -v /root/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7`
   > -d: 后台运行容器 -p: 将容器的端口映射到本机的端口 -v: 将主机目录挂载到容器的目录 -e: 设置参数  
4. 启动mysql容器  
   `docker start mysql`
5. 使用连接工具测试

#### 拓：修改数据库密码
1. 进入mysql
   `sudo docker exec -it mysql bash`
   >docker exec 命令能帮助我们在正在运行的容器中运行指定命令 使用exit退出
2. 使用旧密码登录  
   `mysql -u root -p`
3. 修改密码  
   格式：`set password for 用户名@localhost = password('新密码');`  
   例子：`set password for root@localhost = password('123');`  
   远程连接密码：`set password for root@'%' = password('123');`
   > 补充：修改数据库远程登录密码，需要将localhost换为'%'，表示所有IP都有链接权限
4. 修改完成后，重启容器
   ```
      docker stop mysql 
      docker start mysql
   ```
参考链接：[docker安装mysql5.7](https://blog.csdn.net/weixin_40461281/article/details/92610876)