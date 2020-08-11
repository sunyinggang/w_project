# Typora+PicGo 实现图片快速上传





[七牛云](https://www.qiniu.com/)



[免费额度须知](https://developer.qiniu.com/af/kb/1574/free-credit-information)



## 1.下载PicGO

没有安装PicGO或者已安装PicGO版本在2.2以下，先安装或更新一下PicGO

由于github上下载非常慢，这里提供两个下载地址：

[地址一（极力推荐，直接下载，速度非常快）](http://erkye.lanzous.com/ic230zc)

[地址二（为了防止地址一失效，提供百度网盘下载，提取码：jdjg）](https://pan.baidu.com/s/1sAhMbzPBA5fIh7IcdiN2mw )

## 2.设置Server

打开PicGO设置，点击Server设置

![image-20200810201741948]( http://images.simplesay.top/book/image-20200810201741948.png)

填写设置内容，主要是设置端口号

![image-20200810201706967]( http://images.simplesay.top/book/image-20200810201706967.png)

## 3.Typora偏好设置

打开软件Typora -> 点击文件 ->点击偏好设置，进行如下配置：

1.左侧选择图像

2.设置配置图片时... 下拉选择上传图片，并勾选前两个复选框

3.选定你的PicGO安装路径中PicGO的exe程序

4.点击验证是否成功

![image-20200810203505912]( http://images.simplesay.top/book/image-20200810203505912.png)

验证成功结果如下，注意这里的测试上传图片路径端口就是上边在PicGO中设置的36677端口

![image-20200810201557661]( http://images.simplesay.top/book/image-20200810201557661.png)

## 4.开始使用

设置成功后，我们可以直接使用截图软件或者复制图片后粘贴到Typora文档中，提示上传成功！同样可以在PicGO点击左侧相册可以查看到刚才粘贴到Typora文档中的图片

![image-20200810204230143]( http://images.simplesay.top/book/image-20200810204230143.png)

