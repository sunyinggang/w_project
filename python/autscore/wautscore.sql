/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : wautscore

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-02-25 12:19:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(2) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'admin', '123456');

INSERT INTO `admin` VALUES ('2', 'b', '123456');
INSERT INTO `admin` VALUES ('3', 'c', '123456');
INSERT INTO `admin` VALUES ('4', 'd', '123456');
INSERT INTO `admin` VALUES ('5', 'e', '123456');
INSERT INTO `admin` VALUES ('6', 'f', '123456');
INSERT INTO `admin` VALUES ('7', 'g', '123456');
INSERT INTO `admin` VALUES ('8', 'h', '123456');
INSERT INTO `admin` VALUES ('9', 'i', '123456');
INSERT INTO `admin` VALUES ('10', 'g', '123456');


-- ----------------------------
-- Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('软件-1');

INSERT INTO `class` VALUES ('1', '软件-1');
INSERT INTO `class` VALUES ('2', '软件-2');
INSERT INTO `class` VALUES ('3', '软件-3');
INSERT INTO `class` VALUES ('4', '软件-4');
INSERT INTO `class` VALUES ('5', '软件-5');
INSERT INTO `class` VALUES ('6', '软件-6');
INSERT INTO `class` VALUES ('7', '软件-7');
INSERT INTO `class` VALUES ('8', '软件-8');
INSERT INTO `class` VALUES ('9', '软件-9');
INSERT INTO `class` VALUES ('10', '软件-10');


-- ----------------------------
-- Table structure for `experiment`
-- ----------------------------
DROP TABLE IF EXISTS `experiment`;
CREATE TABLE `experiment` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `model_url` varchar(250) NOT NULL,
  `keywords` text NOT NULL,
  `teacher_id` int(10) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of experiment
-- ----------------------------
INSERT INTO `experiment` VALUES ('4', '测试4', '1579603569.docx', '1', '5', '2020-01-01 00:00:00', '2020-01-01 00:00:00');
INSERT INTO `experiment` VALUES ('6', '测试实验二', '1581305383.docx', 'ddd', '4', '2020-01-01 00:00:00', '2020-01-01 00:00:00');
INSERT INTO `experiment` VALUES ('7', '测试实验', '1581496090.docx', '调试；进程；线程；程序；验证；查看 EOS 启动后的状态和行为，理解操作系统启动后的工作方式', '4', '2020-01-01 00:00:00', '2020-01-01 00:00:00');

INSERT INTO `experiment` VALUES ('1', '测试1', '1579603569.docx', '1', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('2', '测试2', '1579603569.docx', '2', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('3', '测试3', '1579603569.docx', '2', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('4', '测试4', '1579603569.docx', '4', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('5', '测试5', '1579603569.docx', '3', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('6', '测试6', '1579603569.docx', '6', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('7', '测试7', '1579603569.docx', '6', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('8', '测试8', '1579603569.docx', '7', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('9', '测试9', '1579603569.docx', '8', '2020-01-01 00:00:00', '2020-01-02 00:00:00');
INSERT INTO `experiment` VALUES ('10', '测试10', '1579603569.docx', '6', '2020-01-01 00:00:00', '2020-01-02 00:00:00');


-- ----------------------------
-- Table structure for `select`
-- ----------------------------
DROP TABLE IF EXISTS `select`;
CREATE TABLE `select` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `experiment_id` int(10) NOT NULL,
  `student_id` int(10) NOT NULL,
  `word_url` varchar(250) DEFAULT NULL,
  `select_time` datetime DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  `aut_score` int(3) DEFAULT NULL,
  `tea_score` int(3) DEFAULT NULL,
  `is_aut` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of select
-- ----------------------------
INSERT INTO `select` VALUES ('13', '4', '20', null, '2020-02-23 11:44:42', null, '0', '0', '0');
INSERT INTO `select` VALUES ('11', '7', '21', '1581499013.docx', '2020-02-12 17:13:53', null, '63', '0', '0');
INSERT INTO `select` VALUES ('12', '6', '21', null, '2020-02-12 17:14:06', null, '0', '0', '0');

INSERT INTO `select` VALUES ('1', '4', '5', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('2', '7', '8', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('3', '5', '8', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('4', '4', '9', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('5', '8', '2', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('6', '9', '1', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('7', '2', '3', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('8', '9', '4', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('9', '6', '7', null, '2020-02-12 17:14:06', null, null);
INSERT INTO `select` VALUES ('10', '4', '7', null, '2020-02-12 17:14:06', null, null);
-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `class_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('32', '18300113', 'pbkdf2:sha256:150000$dGRt7vcl$36c5f65678ed353c3578bee763123acb91e149fa697068fc08b927dec9552505', '王三', '4');
INSERT INTO `student` VALUES ('31', '18300112', 'pbkdf2:sha256:150000$lTob3XqW$0b5576592cf33a1daeb525a2c564b26dfe7edbba33ab1090d2e68610db77624b', '王二', '0');
INSERT INTO `student` VALUES ('30', '18300111', 'pbkdf2:sha256:150000$YblR2Cf6$7732a5fea985cfae7e96285d4e0f8b424b5eb91e721344b8e2a6b8e75de127cb', '王一', '0');
INSERT INTO `student` VALUES ('29', '18300110', 'pbkdf2:sha256:150000$tgsolfFS$c868ebe2750b08303e040f39c194c7ee0e26220574663bb3cf0a5e9dda19f92b', '张十', '0');
INSERT INTO `student` VALUES ('28', '18300109', 'pbkdf2:sha256:150000$Ds7I6G8v$90ea5fe43de78503c597a67099ac465698c4fcb612228869c0f0359da5ccb5bc', '张九', '0');
INSERT INTO `student` VALUES ('27', '18300108', 'pbkdf2:sha256:150000$8NF92gq6$8283469fae1fab63c7cce501e1b3a1dae0d0ae9fbb7eb612a8dcafb7b2443b8d', '张八', '0');
INSERT INTO `student` VALUES ('26', '18300107', 'pbkdf2:sha256:150000$3hF7JchA$7211f4f74cba8103eb410d05a8ba96ebd085e1d44ad627139841a802119a4fac', '张七', '0');
INSERT INTO `student` VALUES ('25', '18300106', 'pbkdf2:sha256:150000$RuEjbngx$0adbf3744278de388fe05918fb13d4e933ef60463bb65750b3e20c257b7cea3d', '张六', '0');
INSERT INTO `student` VALUES ('24', '18300105', 'pbkdf2:sha256:150000$BGrE6ew4$d7561782b0a8b37c223e30a786a499b43c0c3afd44588c6b777da28f41968785', '张五', '0');
INSERT INTO `student` VALUES ('23', '18300104', 'pbkdf2:sha256:150000$8iB1NEih$49ac248b13790717096ed9486cc261574d8e73ef3b7167f57351ab4a90802259', '张四', '0');
INSERT INTO `student` VALUES ('22', '18300103', 'pbkdf2:sha256:150000$N3FoC4M7$98a13592c8a721b9bec8a35f8ec37224ca7a43c275479b7eb7c320950f8bddea', '张三', '0');
INSERT INTO `student` VALUES ('21', '18300102', 'pbkdf2:sha256:150000$gAIePqgp$57e0054efeeda69909b1fcd289d1daf135d9c2e7778080958a9256ec77ff7e6c', '张二', '4');
INSERT INTO `student` VALUES ('20', '18300101', 'pbkdf2:sha256:150000$xcKH9kPy$c955f243f3975a1e4f3dc19683ee52f5da795445a4c52aab334ebe0cc3c0b01f', '张一', '4');
INSERT INTO `student` VALUES ('33', '18300114', 'pbkdf2:sha256:150000$5t80w8ju$66cda68584f2f11210b54a3224b31995d5b571eefe7243c093b9945a5c643f1b', '王四', '0');
INSERT INTO `student` VALUES ('34', '18300115', 'pbkdf2:sha256:150000$xV0JJ1di$b8c39c31013261611f7ef888dd8bf3718b6b832a2b4240c560264cf1fbab0de1', '王五', '0');
INSERT INTO `student` VALUES ('35', '18300116', 'pbkdf2:sha256:150000$vl1F4o02$63dacb1b931ef0280ca8a44d703b916192c16f6787ca1749d595602fe7ea2ea0', '王六', '0');

INSERT INTO `student` VALUES ('1', '18300112', '123456', '王二', '1');
INSERT INTO `student` VALUES ('2', '18300111', '123456', '王一', '2');
INSERT INTO `student` VALUES ('3', '18300110', '123456', '张十', '3');
INSERT INTO `student` VALUES ('4', '18300109', '123456', '张九', '3');
INSERT INTO `student` VALUES ('5', '18300108', '123456', '张八', '2');
INSERT INTO `student` VALUES ('6', '18300107', '123456', '张七', '6');
INSERT INTO `student` VALUES ('7', '18300106', '123456', '张六', '7');
INSERT INTO `student` VALUES ('8', '18300105', '123456', '张五', '1');
INSERT INTO `student` VALUES ('9', '18300104', '123456', '张四', '8');
INSERT INTO `student` VALUES ('10', '18300103', '123456', '张三', '5');


-- ----------------------------
-- Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('6', '18200903', 'pbkdf2:sha256:150000$3XOvdr6s$f8f23ff8e4a217c2de14d6c2713d89ee24ba565e5270e53226b42ae6ef9eb698', '李四');
INSERT INTO `teacher` VALUES ('4', '18200901', 'pbkdf2:sha256:150000$DbvW1bPz$e0aa5365ba66075c6b1ba0a8fd86fe5ff29d0f294979ce4f49090684e9692765', '王小明');
INSERT INTO `teacher` VALUES ('5', '18200902', 'pbkdf2:sha256:150000$z9nFoja8$77f9d24865fd75fa33d8b2f2ce9c278b05167f2d1df997a0050a09c7b4394868', '张晓红');


INSERT INTO `teacher` VALUES ('1', '18200901', '123456', '李二');
INSERT INTO `teacher` VALUES ('2', '18200902', '123456', '李一');
INSERT INTO `teacher` VALUES ('3', '18200903', '123456', '赵十');
INSERT INTO `teacher` VALUES ('4', '18200904', '123456', '赵九');
INSERT INTO `teacher` VALUES ('5', '18200905', '123456', '赵八');
INSERT INTO `teacher` VALUES ('6', '18200906', '123456', '赵七');
INSERT INTO `teacher` VALUES ('7', '18200907', '123456', '赵六');
INSERT INTO `teacher` VALUES ('8', '18200908', '123456', '赵五');
INSERT INTO `teacher` VALUES ('9', '18200909', '123456', '赵四');
INSERT INTO `teacher` VALUES ('10', '18200910', '123456', '赵三');

