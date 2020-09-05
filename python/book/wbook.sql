/*
 Navicat Premium Data Transfer

 Source Server         : 172.81.212.215
 Source Server Type    : MySQL
 Source Server Version : 50730
 Source Host           : 172.81.212.215:3306
 Source Schema         : wbook

 Target Server Type    : MySQL
 Target Server Version : 50730
 File Encoding         : 65001

 Date: 07/07/2020 16:07:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NULL DEFAULT NULL,
  `title` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `day` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (10, 5, '论语 ', '2018-10-15', '已还书');
INSERT INTO `book` VALUES (11, 5, '沉思录', '2018-10-20', '5');
INSERT INTO `book` VALUES (12, 5, '不抱怨的世界', '2018-9-26', '10');
INSERT INTO `book` VALUES (13, 5, '谁动了我的奶酪?', '2018-10-26', '已还书');
INSERT INTO `book` VALUES (14, 6, '红楼梦', '2018-9-10', '5');
INSERT INTO `book` VALUES (15, 6, '孩子你慢慢来', '2018-10-1', '7');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `usertype` int(5) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (5, 'Tom', 'tom', 1);
INSERT INTO `user` VALUES (6, 'Sam', 'sam', 1);
INSERT INTO `user` VALUES (7, 'admin', 'admin', 2);

SET FOREIGN_KEY_CHECKS = 1;
