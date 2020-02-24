/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : wcar

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-02-24 16:03:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', '管理员1', '男', '136080@qq.com', '1', 'e10adc3949ba59abbe56e057f20f883e');

-- ----------------------------
-- Table structure for `car`
-- ----------------------------
DROP TABLE IF EXISTS `car`;
CREATE TABLE `car` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of car
-- ----------------------------
INSERT INTO `car` VALUES ('2', '车辆页', 'http://localhost/wcar/public/upload/2020/02-03/524c0c8e4ecd0b06e75517275c192eb4.jpg', '3', '测试建议', '2', '2020-02-03 19:10:39', '2020-02-14 15:53:49');

-- ----------------------------
-- Table structure for `carer_info`
-- ----------------------------
DROP TABLE IF EXISTS `carer_info`;
CREATE TABLE `carer_info` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `logo` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of carer_info
-- ----------------------------
INSERT INTO `carer_info` VALUES ('5', 'A1234', '北京', '宝马', '3');

-- ----------------------------
-- Table structure for `car_show`
-- ----------------------------
DROP TABLE IF EXISTS `car_show`;
CREATE TABLE `car_show` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of car_show
-- ----------------------------
INSERT INTO `car_show` VALUES ('2', '车辆外观', 'http://localhost/wcar/public/upload/2020/02-03/2603bebf0169ae883a19cfc63ff91393.jpg', '3', '测试2', '2', '2020-02-03 19:10:56', '2020-02-14 16:23:35');

-- ----------------------------
-- Table structure for `drive_card`
-- ----------------------------
DROP TABLE IF EXISTS `drive_card`;
CREATE TABLE `drive_card` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `nation` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `born_date` varchar(255) NOT NULL,
  `get_date` varchar(255) NOT NULL,
  `car_type` varchar(255) NOT NULL,
  `limit_date` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of drive_card
-- ----------------------------
INSERT INTO `drive_card` VALUES ('2', '驾驶证基本信息', 'A1234', 'a', 'ad', '中国', '山东省威海市荣成市', '2020-02-22', '2020-02-22', 'sad', '10', 'http://localhost/wcar/public/upload/2020/02-03/4c9cb81638b95f4fa4cd0facc3ed41aa.jpg', '3', null, '0', '2020-02-03 19:02:37', '2020-02-03 19:02:37');

-- ----------------------------
-- Table structure for `drive_subpage`
-- ----------------------------
DROP TABLE IF EXISTS `drive_subpage`;
CREATE TABLE `drive_subpage` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of drive_subpage
-- ----------------------------

-- ----------------------------
-- Table structure for `id_card`
-- ----------------------------
DROP TABLE IF EXISTS `id_card`;
CREATE TABLE `id_card` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `limit_date` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of id_card
-- ----------------------------
INSERT INTO `id_card` VALUES ('2', '身份证基本信息（正页）', '2025-01-20', '山东省威海市荣成市', 'http://localhost/wcar/public/upload/2020/02-03/aab7b212d37b4899b57b3e4b541d4d00.jpg', '3', null, '1', '2020-02-03 19:03:37', '2020-02-14 16:36:45');

-- ----------------------------
-- Table structure for `id_subpage`
-- ----------------------------
DROP TABLE IF EXISTS `id_subpage`;
CREATE TABLE `id_subpage` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `nation` varchar(255) NOT NULL,
  `born_date` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of id_subpage
-- ----------------------------
INSERT INTO `id_subpage` VALUES ('2', '身份证基本信息（副页）', '张三', '男', '汉', '2007-10-1', '山东省威海市荣成市', '370826200710014638', 'http://localhost/wcar/public/upload/2020/02-15/29eb0a26b564de658ef27d05ec34f9b3.png', '6', null, '0', '2020-02-15 12:36:47', '2020-02-15 12:36:47');
INSERT INTO `id_subpage` VALUES ('3', '身份证基本信息（副页）', '李四', '男', '汉', '1997-05-10', '山东省威海市荣成市', '370826199705104638', '15/29eb0a26b564de658ef27d05ec34f9b3.png', '7', null, '1', '2020-02-15 12:38:53', '2020-02-15 14:30:13');

-- ----------------------------
-- Table structure for `review_process`
-- ----------------------------
DROP TABLE IF EXISTS `review_process`;
CREATE TABLE `review_process` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content_id` int(10) NOT NULL,
  `type` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of review_process
-- ----------------------------

-- ----------------------------
-- Table structure for `travel_card`
-- ----------------------------
DROP TABLE IF EXISTS `travel_card`;
CREATE TABLE `travel_card` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL,
  `car_type` varchar(255) NOT NULL,
  `car_user` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `user_nature` varchar(255) NOT NULL,
  `logo` varchar(255) NOT NULL,
  `identify_code` varchar(255) NOT NULL,
  `engine_num` varchar(255) NOT NULL,
  `register_date` date NOT NULL,
  `send_date` date NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of travel_card
-- ----------------------------
INSERT INTO `travel_card` VALUES ('2', '行驶证基本信息', 'A1234', 'sad', 'das', '山东省威海市荣成市', 'a', '宝马', 'wqe', 'd', '2020-01-10', '2020-02-10', 'http://localhost/wcar/public/upload/2020/02-03/4f6177471ef2f58499b3451d316ca006.jpg', '3', null, '1', '2020-02-03 16:49:02', '2020-02-03 18:58:17');
INSERT INTO `travel_card` VALUES ('3', '行驶证基本信息', 'A1234', '轿车', '李四', '山东省威海市荣成市', 'a', '宝马', 'wqed', 'ggf', '2010-06-17', '2011-01-05', 'http://localhost/wcar/public/upload/2020/02-15/a66386f0334322992fc05d2ce1d11148.png', '7', null, '0', '2020-02-15 12:43:18', '2020-02-15 12:43:18');
INSERT INTO `travel_card` VALUES ('4', '行驶证基本信息', 'A123', '轿车', '张三', '山东省威海市荣成市', 'a', '宝马', 'ffvv', 'awaae', '2008-11-10', '2009-02-10', 'http://localhost/wcar/public/upload/2020/02-15/9691aface14f2510fa5a27f3bf38da02.png', '6', null, '0', '2020-02-15 12:44:36', '2020-02-15 12:44:36');

-- ----------------------------
-- Table structure for `travel_subpage`
-- ----------------------------
DROP TABLE IF EXISTS `travel_subpage`;
CREATE TABLE `travel_subpage` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL,
  `people` varchar(255) NOT NULL,
  `picture_url` varchar(255) NOT NULL,
  `user_id` int(10) NOT NULL,
  `suggest` text,
  `status` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of travel_subpage
-- ----------------------------
INSERT INTO `travel_subpage` VALUES ('3', '行驶证副业基本信息', 'A1234', '4', 'http://localhost/wcar/public/upload/2020/02-03/f92fb4c4cbdd4ed62999005e7eb07734.jpg', '3', 'sad测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试', '2', '2020-02-03 19:00:56', '2020-02-03 19:00:56');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('5', '1', '男', 'admin', '1', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `user` VALUES ('2', '1', '男', 'admin', '2', '123456');
INSERT INTO `user` VALUES ('3', 'd', '男', 'admin', '15688708938', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `user` VALUES ('6', '张三', '男', '135@qq.com', '123', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `user` VALUES ('7', '李四', '男', '145@qq.com', '1234', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `user` VALUES ('11', '王五', '男', '136080416@qq.com', '12345', 'e10adc3949ba59abbe56e057f20f883e');
