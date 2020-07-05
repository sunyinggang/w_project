/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50728
Source Host           : localhost:3306
Source Database       : webapp

Target Server Type    : MYSQL
Target Server Version : 50728
File Encoding         : 65001

Date: 2020-05-11 18:25:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tel` varchar(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('7', '15688708938', 'pbkdf2:sha256:50000$MTQQlP4D$4754f33466855c2d3114d8fdc0f1e146026d3f3710e5aae630780e0485f8b6e2');
INSERT INTO `user` VALUES ('8', '15662365002', 'pbkdf2:sha256:50000$pQvNyCoq$659fe3edd71781d7f71bf6f6e61ca72e75728427bff963b0d0fe4ef05df3b580');

- ----------------------------
-- Table structure for `commodity`
-- ----------------------------
DROP TABLE IF EXISTS `commodity`;
CREATE TABLE `commodity` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `os` varchar(50) NOT NULL,
  `number` varchar(50) NOT NULL,
  `area` varchar(50) NOT NULL,
  `server` varchar(50) NOT NULL,
  `rank` int(5) NOT NULL,
  `type` varchar(50) NOT NULL,
  `pet` int(5) NOT NULL,
  `sect` varchar(50) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `bargain` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `content` text,
  `see` int(2) NOT NULL DEFAULT '0',
  `tel` varchar(15) NOT NULL DEFAULT '',
  `wx` varchar(30) NOT NULL DEFAULT '',
  `role` int(1) NOT NULL DEFAULT '1',
  `user_id` int(5) DEFAULT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of commodity
-- ----------------------------
INSERT INTO `commodity` VALUES ('7', '测试一', '435.50', '苹果专区', 'sdf3', '测试一区', '测试服务器一', '66', '无账号绑定', '6', '大唐官府', '男', '可议价', '阿诗丹顿', '顶置图片.png', '1', '', '', '1', null, '2018-12-23 19:29:08');
INSERT INTO `commodity` VALUES ('8', '测试二', '342.50', '安卓专区', 'kf2', '测试一区', '测试服务器一', '67', '手机绑定', '67', '方寸山', '女', '不可议价', '啥风格和', 'buy.jpg,sell.jpg', '1', '', '', '1', null, '2018-12-23 19:29:10');
INSERT INTO `commodity` VALUES ('10', '测试四', '435.00', '安卓专区', 'kf45', '测试一区', '测试服务器二', '67', '无账号绑定', '6', '狮驼岭', '女', '不可议价', '多少分', '2019010921442256aa5c9fec944aeb9756f146509e89fd.png', '1', '', '', '1', null, '2019-01-09 21:44:24');
INSERT INTO `commodity` VALUES ('11', '测试八', '435.00', '苹果专区', '分', '测试一区', '测试服务器一', '34', '无账号绑定', '4', '大唐官府', '男', '可议价', 'd', 'buy.jpg,sell.jpg', '0', '', '', '1', null, '2018-12-23 19:39:37');
INSERT INTO `commodity` VALUES ('12', '测试六', '546.00', '苹果专区', 'DF4', '测试一区', '测试服务器一', '66', '无账号绑定', '66', '大唐官府', '男', '可议价', 's', 'buy.jpg,sell.jpg\r\nbuy.jpg,sell.jpg', '0', '', '', '1', null, '2018-12-23 18:52:21');
INSERT INTO `commodity` VALUES ('13', 'sad', '546.00', '苹果专区', 'kf2', '测试一区', '测试服务器一', '66', '手机绑定', '67', '大唐官府', '男', '可议价', 'sad', 'buy.jpg,sell.jpg', '0', '', '', '2', null, '2018-12-23 20:24:47');
INSERT INTO `commodity` VALUES ('14', '测试不置顶', '435.00', '安卓专区', 'DF4', '测试二区', '测试服务器一', '88', '签订合同账号', '8', '大唐官府', '女', '不可议价', '爱仕达', '顶置图片2.png,顶置图片3.png,顶置图片.png,顶置图片4.png', '0', '', '', '2', null, '2018-12-23 21:40:29');
INSERT INTO `commodity` VALUES ('15', 'ddd', '546.00', '安卓专区', '分', '测试二区', '爱仕达', '34', '有绑定账号', '4', '狮驼岭', '男', '不可议价', '打算', 'sell.jpg', '0', '', '', '1', null, '2018-12-23 20:48:26');
INSERT INTO `commodity` VALUES ('16', 'asc', '228.00', '双平台安卓登录', '分', '测试一区', '测试服务器二', '67', '无账号绑定', '8', '大唐官府', '男', '可议价', '打', '顶置图片.png', '0', '', '', '1', null, '2018-12-23 20:50:26');
INSERT INTO `commodity` VALUES ('17', 'asc', '546.00', '双平台苹果登入', 'i5PHpkBckj22qXrqOY2EjvKzO5', '测试一区', '测试服务器二', '566', '签订合同账号', '66', '普陀山', '女', '可议价', '大', '顶置图片2.png', '0', '', '', '1', null, '2018-12-23 20:55:22');
INSERT INTO `commodity` VALUES ('18', '测试前台商品', '567.00', '双平台苹果登入', 'QkD1Z2InD5zc02wVsuCksthPkn', '测试二区', '测试服务器一', '566', '手机绑定', '8', '普陀山', '男', '不可议价', '第三个', 'sell.jpg,顶置图片.png', '0', '15688708938', '1', '2', null, '2018-12-23 21:40:26');
INSERT INTO `commodity` VALUES ('19', 'asc', '228.00', '双平台苹果登入', 'olR4OffIn5C28U5b1JKSdrknR4', '的啊', '测试服务器一', '67', '签订合同账号', '66', '普陀山', '男', '可议价', '打分', 'buy.jpg,顶置图片2.png,sell.jpg,顶置图片.png', '0', '', '', '1', null, '2018-12-25 16:47:44');
INSERT INTO `commodity` VALUES ('20', 'ccacc', '338.00', '双平台安卓登录', 'xLXXmfh1tWx7R2oGwAVUJB850K', '测试二区', '测试服务器一', '88', '手机绑定', '67', '阴曹地府', '男', '可议价', '阿斯蒂芬', '顶置图片2.png,顶置图片3.png,sell.jpg,顶置图片4.png,顶置图片.png', '0', '', '', '1', null, '2018-12-25 16:50:28');
INSERT INTO `commodity` VALUES ('21', '测试一', '338.00', '苹果专区', '1ckS5zb2OEu5im1sbrJhwQiYpJ', '测试一区', '测试服务器一', '566', '手机绑定', '67', '大唐官府', '女', '不可议价', '暗示法', '顶置图片.png', '0', '15688708938', '1', '2', '7', '2020-01-11 17:24:14');
INSERT INTO `commodity` VALUES ('22', 'ddd', '123.00', '苹果专区', 'tjfOaMt5ZDLabUNYX1A5F27L2D', '的啊', '爱仕达', '566', '手机绑定', '67', '大唐官府', '男', '不可议价', '萨德', '20181225173345cabd36565ac34f34939ebe70b2fc749a.jpg', '0', '15688708938', '1', '2', '7', '2018-12-25 17:36:11');
INSERT INTO `commodity` VALUES ('23', 'asc', '435.00', '苹果专区', 'j1qnU5XL44', '测试一区', '测试服务器一', '66', '有绑定账号', '6', '大唐官府', '女', '可议价', 'tyju', '20181226165945d518299de56245e58e760cea8bf8d96e.png,2018122616594598254b8a02424980ab91cece1e72215b.png,201812261659455ac8d7da0c0049fbb94ae2fd0acbb353.png', '0', '', '', '1', null, '2018-12-26 16:59:48');

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(2) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'Admin', 'admin');

