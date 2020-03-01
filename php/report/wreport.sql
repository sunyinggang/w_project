/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : wreport

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-03-01 14:28:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', '张三', '136080416@qq.com', 'e10adc3949ba59abbe56e057f20f883e');

-- ----------------------------
-- Table structure for `clue`
-- ----------------------------
DROP TABLE IF EXISTS `clue`;
CREATE TABLE `clue` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `object` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of clue
-- ----------------------------

-- ----------------------------
-- Table structure for `exposure`
-- ----------------------------
DROP TABLE IF EXISTS `exposure`;
CREATE TABLE `exposure` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of exposure
-- ----------------------------
INSERT INTO `exposure` VALUES ('7', '测试一', '<p>爱仕达sad</p>', '2020-02-17 21:12:36', '2020-02-17 21:12:36');
INSERT INTO `exposure` VALUES ('4', '测试二', '<p>					</p><p style=\"text-align: center;\">萨德</p><p>&nbsp; &nbsp; 萨德撒多士大夫发</p><p><img src=\"/report/public/upload/image/20200217/1581939426.jpg\" title=\"1581939426.jpg\" alt=\"22.jpg\"/></p><p>				</p>', '2020-02-17 19:14:00', '2020-02-17 19:37:09');
INSERT INTO `exposure` VALUES ('6', '测试四', '<p>sadsa</p><p><img src=\"/report/public/upload/image/20200217/1581940194.jpg\" title=\"1581940194.jpg\" alt=\"22.jpg\"/><img src=\"/report/public/upload/image/20200217/1581940199.jpg\" title=\"1581940199.jpg\" alt=\"22.jpg\"/></p>', '2020-02-17 19:50:01', '2020-02-17 19:50:01');
INSERT INTO `exposure` VALUES ('5', '测试三', '<p>车费萨达顺风车<br/></p><p style=\"white-space: normal;\">萨达顺风车</p><p style=\"white-space: normal;\">沙发但是第四个</p><p>沙发但是第四个</p><p><img src=\"/report/public/upload/image/20200217/1581939386.jpg\" title=\"1581939386.jpg\" alt=\"22.jpg\"/></p>', '2020-02-17 19:36:29', '2020-02-17 19:36:29');

-- ----------------------------
-- Table structure for `harass`
-- ----------------------------
DROP TABLE IF EXISTS `harass`;
CREATE TABLE `harass` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `web_address` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of harass
-- ----------------------------

-- ----------------------------
-- Table structure for `illegal`
-- ----------------------------
DROP TABLE IF EXISTS `illegal`;
CREATE TABLE `illegal` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `object` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of illegal
-- ----------------------------

-- ----------------------------
-- Table structure for `illwebsite`
-- ----------------------------
DROP TABLE IF EXISTS `illwebsite`;
CREATE TABLE `illwebsite` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `web_address` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of illwebsite
-- ----------------------------

-- ----------------------------
-- Table structure for `infringement`
-- ----------------------------
DROP TABLE IF EXISTS `infringement`;
CREATE TABLE `infringement` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `web_address` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of infringement
-- ----------------------------

-- ----------------------------
-- Table structure for `leakage`
-- ----------------------------
DROP TABLE IF EXISTS `leakage`;
CREATE TABLE `leakage` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `object` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `web_address` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of leakage
-- ----------------------------

-- ----------------------------
-- Table structure for `other`
-- ----------------------------
DROP TABLE IF EXISTS `other`;
CREATE TABLE `other` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of other
-- ----------------------------

-- ----------------------------
-- Table structure for `reward`
-- ----------------------------
DROP TABLE IF EXISTS `reward`;
CREATE TABLE `reward` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reward
-- ----------------------------
INSERT INTO `reward` VALUES ('1', '测试悬赏公告', '<p>测试</p><p><img src=\"/ueditor/php/upload/image/20200217/1581934052.jpg\" title=\"1581934052.jpg\" alt=\"22.jpg\"/></p>', '2020-02-17 18:07:34', '2020-02-17 18:07:34');

-- ----------------------------
-- Table structure for `rumor`
-- ----------------------------
DROP TABLE IF EXISTS `rumor`;
CREATE TABLE `rumor` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `web_address` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rumor
-- ----------------------------
INSERT INTO `rumor` VALUES ('4', '测试34', '<p>cekgfhaa</p>', null, '1', '5', '1', 'www.abc.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');

-- ----------------------------
-- Table structure for `safety`
-- ----------------------------
DROP TABLE IF EXISTS `safety`;
CREATE TABLE `safety` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of safety
-- ----------------------------
INSERT INTO `safety` VALUES ('1', '测试安全警示', '<p>					</p><p>sad<img src=\"/ueditor/php/upload/image/20200217/1581934172.jpg\" title=\"1581934172.jpg\" alt=\"22.jpg\"/></p><p>				</p>', '2020-02-17 18:09:34', '2020-02-17 18:09:51');

-- ----------------------------
-- Table structure for `scam`
-- ----------------------------
DROP TABLE IF EXISTS `scam`;
CREATE TABLE `scam` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `web_address` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of scam
-- ----------------------------
INSERT INTO `scam` VALUES ('3', '中奖信息', '测试2', '<p>asd</p>', null, '1', '1', '1', 'www.abc.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');
INSERT INTO `scam` VALUES ('4', '中奖信息', '测试', '<p>哒哒哒哒哒哒多多多多</p>', null, '0', '1', '1', 'www.abc.com', '2020-02-23 18:46:53', '2020-02-23 18:46:53');
INSERT INTO `scam` VALUES ('5', '代刷信用', '代刷信用测试', '<p>代刷信用测试</p>', null, '0', '1', '1', 'www.abc.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');
INSERT INTO `scam` VALUES ('6', '其他诈骗', '快乐赞卡单不退款', '<p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\">&nbsp; &nbsp; &nbsp; &nbsp;客服态度非常不好不给予正面回答问题打太极拖延时间导致我每天都在损失金钱入账&nbsp;快乐赞平台只有一个仲裁却仲裁了近一周还未解决现要求全额退款并解释说明道歉。</span></p><p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\"><img src=\"/report/public/upload/image/20200229/1582954249.jpg\" title=\"1582954249.jpg\" alt=\"1bf5dc61faaa91a361a1d476fea83f6e.jpg\"/></span></p>', null, '1', '1', '1', 'www.abc.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');
INSERT INTO `scam` VALUES ('7', '虚拟财产交易', '辽宁汇铂网络科技有限公司理财app非法集资', '<p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\">&nbsp; &nbsp; &nbsp; &nbsp;汇鼎理财app于2020年1月份左右突然无法正常提现，后于2月10日发布了因疫情防控延迟复工公告，后又于2月20日发布了暂停公司运营的公告。此app原由浙江汇铂资产管理有限公司负责，现转移为辽宁汇铂网络科技有限公司，此app法定代表人邵建国非法集资，恶意关闭旗下理财是app数据，未受本地金融部门监管，运营不善还持续收纳出借款，恶意吸收公众储蓄，请警方介入调查，还我们受害人一个公道！</span></p><p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\"><img src=\"/report/public/upload/image/20200229/1582954470.jpg\" title=\"1582954470.jpg\" alt=\"12.jpg\"/></span></p>', null, '1', '1', '1', 'www.abc.com', '0000-00-00 00:00:00', '2020-02-29 17:12:43');
INSERT INTO `scam` VALUES ('8', '虚拟财产交易', '百消丹云麒不发货不退款，恶意销售，客服电话为空号！', '<p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\">&nbsp; &nbsp; &nbsp; 百消丹云麒&nbsp;微信商城下单，不发货，不退款，申请退款后给我自动取消，变更为发货中，但是物流信息查询不到，客服不回消息，客服电话四个号码三个为空号，明显欺骗。</span></p><p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\"><img src=\"/report/public/upload/image/20200229/1582954717.jpg\" title=\"1582954717.jpg\" alt=\"123.jpg\"/></span></p>', null, '0', '1', '1', 'www.abc.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');
INSERT INTO `scam` VALUES ('9', '虚拟财产交易', '百消丹云麒不发货不退款，恶意销售，客服电话为空号！', '<p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\">&nbsp; &nbsp; &nbsp; 百消丹云麒&nbsp;微信商城下单，不发货，不退款，申请退款后给我自动取消，变更为发货中，但是物流信息查询不到，客服不回消息，客服电话四个号码三个为空号，明显欺骗。</span></p><p><span style=\"color: rgb(102, 102, 102); font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-size: 15px; background-color: rgb(255, 255, 255);\"><img src=\"/report/public/upload/image/20200229/1582954717.jpg\" title=\"1582954717.jpg\" alt=\"123.jpg\"/></span></p>', null, '0', '1', '1', 'www.abc.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');
INSERT INTO `scam` VALUES ('10', '虚拟财产交易', '咸鱼交易骗单', '<h1 style=\"box-sizing: border-box; margin: 0px; font-size: 20px; font-family: &quot;Helvetica Neue&quot;, STHeiti, 微软雅黑, &quot;Microsoft YaHei&quot;, Helvetica, Arial, sans-serif; font-weight: 500; line-height: 30px; color: rgb(51, 51, 51); max-width: 500px; white-space: normal; background-color: rgb(255, 255, 255);\">&nbsp; &nbsp; &nbsp; 闲鱼交易骗单 假物流 发起退货申请 不给退款 发起投诉后 卖家威胁帮他解封后退款 但迟迟未退 订单已经到自动确认收货了</h1><p><br/></p>', 'sad', '2', '1', '1', 'www.abc.com', '2020-02-29 13:54:06', '2020-02-29 17:22:51');

-- ----------------------------
-- Table structure for `sort`
-- ----------------------------
DROP TABLE IF EXISTS `sort`;
CREATE TABLE `sort` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `ano_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sort
-- ----------------------------
INSERT INTO `sort` VALUES ('1', '诈骗类有害信息举报', 'scam');
INSERT INTO `sort` VALUES ('5', '谣言类有害信息举报', 'rumor');
INSERT INTO `sort` VALUES ('2', '侵权类有害信息举报', 'infringement');
INSERT INTO `sort` VALUES ('3', '骚扰类有害信息举报', 'harass');
INSERT INTO `sort` VALUES ('4', '违法网站举报', 'illwebsite');
INSERT INTO `sort` VALUES ('6', '恶意手机应用举报', 'spite');
INSERT INTO `sort` VALUES ('7', '个人信息泄露举报', 'leakage');
INSERT INTO `sort` VALUES ('8', '违法犯罪线索举报', 'clue');
INSERT INTO `sort` VALUES ('9', '违法违纪举报', 'illegal');
INSERT INTO `sort` VALUES ('10', '其它违法举报', 'other');

-- ----------------------------
-- Table structure for `spite`
-- ----------------------------
DROP TABLE IF EXISTS `spite`;
CREATE TABLE `spite` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `download` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `commit` text,
  `status` int(10) NOT NULL,
  `sort_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spite
-- ----------------------------

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `area` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '张三', '男', '370826194533459876', '136080416@qq.com', '15688708938', '山东威海', 'e10adc3949ba59abbe56e057f20f883e');
