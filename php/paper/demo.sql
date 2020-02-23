/*
 Navicat Premium Data Transfer

 Source Server         : demo
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : localhost:3306
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 28/11/2019 20:45:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for paper_system
-- ----------------------------
DROP TABLE IF EXISTS `paper_system`;
CREATE TABLE `paper_system`  (
  `id` char(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '系部名称',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id`(`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci COMMENT = '系部表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for paper_admin
-- ----------------------------
DROP TABLE IF EXISTS `paper_admin`;
CREATE TABLE `paper_admin`  (
  `id` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci COMMENT = '教务表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for paper_leader
-- ----------------------------
DROP TABLE IF EXISTS `paper_leader`;
CREATE TABLE `paper_leader`  (
  `id` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` char(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '123456',
  `sid` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for paper_name
-- ----------------------------
DROP TABLE IF EXISTS `paper_name`;
CREATE TABLE `paper_name`  (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '论文题目',
  `sid` char(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '所属系部',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `paper_name_sid`(`sid`) USING BTREE,
  CONSTRAINT `paper_name_sid` FOREIGN KEY (`sid`) REFERENCES `paper_system` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci COMMENT = '论文题目表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for paper_student
-- ----------------------------
DROP TABLE IF EXISTS `paper_student`;
CREATE TABLE `paper_student`  (
  `id` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `keyid` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'openid',
  `sid` char(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '所属系部',
  `topic` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '论文题目',
  `ppt1` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '开题PPT',
  `report` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '开题报告',
  `ppt2` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '答辩PPT',
  `paper` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '论文',
  `score1` int(4) NOT NULL COMMENT '开题指导教师成绩',
  `score2` int(4) NOT NULL COMMENT '开题答辩委员会成绩',
  `score3` int(4) NOT NULL COMMENT '论文指导教师成绩',
  `score4` int(4) NOT NULL COMMENT '论文答辩委员会成绩',
  `finally` int(4) NOT NULL COMMENT '最终成绩',
  `topic_state1` int(2) NOT NULL COMMENT '指导教师是否批准题目',
  `topic_state2` int(2) NOT NULL COMMENT '系主任是否批准题目',
  `state` int(2) NOT NULL COMMENT '学生状态',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `paper_student_sid`(`sid`) USING BTREE,
  CONSTRAINT `paper_student_sid` FOREIGN KEY (`sid`) REFERENCES `paper_system` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci COMMENT = '学生表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for paper_teacher
-- ----------------------------
DROP TABLE IF EXISTS `paper_teacher`;
CREATE TABLE `paper_teacher`  (
  `id` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `sid` char(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '所属系部',
  `member` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '被指导学生',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `paper_teacher_sid`(`sid`) USING BTREE,
  CONSTRAINT `paper_teacher_sid` FOREIGN KEY (`sid`) REFERENCES `paper_system` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci COMMENT = '指导教师表' ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
