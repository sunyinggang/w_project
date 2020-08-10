# Docker部署Flask项目

若在linux服务器中

打包
`docker build -f Dockerfile.dockerfile -t traffic .`

运行
`docker run --name traffic -p 5555:5555 --link mysql:mysql -d traffic`

进入docker  
`docker exec -it flask /bin/bash`

其他命令

`apt-get update`

`apt-get install vim`


`docker restart 容器ID或容器名`

删除某个镜像

docker stop

删除docker中的镜像
docker images
docker rmi IMAGE ID

删除docker中的容器
docker ps -a
docker rm CONTAINER ID

查看当前正在运行的容器
docker ps

查看所有的容器
docker ps -a

mysql跟应用不在同一个网络中
应用中连接mysql用如下两种方式：
1.如果你是docker-compose 直接关联方式
2.如果你是普通docker，就要写当前IP