/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : wplane

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2019-08-14 11:54:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `airline`
-- ----------------------------
DROP TABLE IF EXISTS `airline`;
CREATE TABLE `airline` (
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of airline
-- ----------------------------
INSERT INTO `airline` VALUES ('China Eastern');

-- ----------------------------
-- Table structure for `airlinestaff`
-- ----------------------------
DROP TABLE IF EXISTS `airlinestaff`;
CREATE TABLE `airlinestaff` (
  `username` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` varchar(50) DEFAULT NULL,
  `airline_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `airline_name` (`airline_name`),
  CONSTRAINT `airlinestaff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of airlinestaff
-- ----------------------------
INSERT INTO `airlinestaff` VALUES ('sun', 'pbkdf2:sha256:50000$0bQgUAg2$3e0485e1f71c152295c80709b32d9e06761fa6620e64c18e125374c75bd6e4c8', 'Brown', 'Felix', '1900-01-01 00:00', 'China Eastern');

-- ----------------------------
-- Table structure for `airplane`
-- ----------------------------
DROP TABLE IF EXISTS `airplane`;
CREATE TABLE `airplane` (
  `id` varchar(50) NOT NULL,
  `seats` int(5) NOT NULL,
  `airline_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `airline_name` (`airline_name`),
  CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of airplane
-- ----------------------------
INSERT INTO `airplane` VALUES ('GBH231', '200', 'China Eastern');
INSERT INTO `airplane` VALUES ('LOP08', '265', 'China Eastern');

-- ----------------------------
-- Table structure for `airport`
-- ----------------------------
DROP TABLE IF EXISTS `airport`;
CREATE TABLE `airport` (
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of airport
-- ----------------------------
INSERT INTO `airport` VALUES ('FRT', 'Detroit');
INSERT INTO `airport` VALUES ('TFG', 'San Francisco');

-- ----------------------------
-- Table structure for `bookingagent`
-- ----------------------------
DROP TABLE IF EXISTS `bookingagent`;
CREATE TABLE `bookingagent` (
  `email` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `booking_agent_id` varchar(50) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bookingagent
-- ----------------------------
INSERT INTO `bookingagent` VALUES ('2334@qq.com', 'pbkdf2:sha256:50000$m9M6mlNS$a4358c1efec64037188df3436ccd8a01b7ebb5d2237cf59442a1b3ebb8dd6ddb', 'ew4GqbOU');
INSERT INTO `bookingagent` VALUES ('2345@qq.com', 'pbkdf2:sha256:50000$BRVumA89$9cd0665dc671b7a225b267c6321276ffa9ae39873109b0ebf0982e618d65ced3', 'Y0ION7PE');
INSERT INTO `bookingagent` VALUES ('2456@qq.com', 'pbkdf2:sha256:50000$uaoEqg3x$4fd7157e0801d5f208338ee2ad64d6f4e1d2bfe638941c743e8bed9360fe2a24', 'F5hZ2cwQ');
INSERT INTO `bookingagent` VALUES ('2567@qq.com', 'pbkdf2:sha256:50000$qCyUFaDe$8c23e12b629be07e4999126b9c99244933b30b59b0e9b520350e43ad35d2b2b8', 'n9XF3Ny7');
INSERT INTO `bookingagent` VALUES ('2678@qq.com', 'pbkdf2:sha256:50000$Br95Gyxc$fba04f4b82935ef2418b5df855b7f2cf5f9746b1d26383ee52ef29ee06897f4e', 'Xrj6PVFs');
INSERT INTO `bookingagent` VALUES ('2789@qq.com', 'pbkdf2:sha256:50000$JuVNV3Rv$21c85a08090138b1b62c025e3d78e1b05b2c809322f4f58191e63917e1d43091', 'SDT54nHe');

-- ----------------------------
-- Table structure for `customer`
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `password` varchar(200) NOT NULL,
  `building_number` varchar(50) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `passport_number` varchar(50) DEFAULT NULL,
  `passport_expiration` datetime DEFAULT NULL,
  `passport_country` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES ('1234@qq.com', 'Tom', 'pbkdf2:sha256:50000$Y5tJRK6q$2035604b984c589719635117f43b8f39f1c9a928b14ca6a8294b6e116445b4fa', '250', 'Hannah Administration Building', 'East Lansing', 'Michigan', '12345', 'DFGE321', '1900-12-14 00:30:00', 'United States', '1900-12-28');
INSERT INTO `customer` VALUES ('1345@qq.com', null, 'pbkdf2:sha256:50000$LjXGQ2oQ$5bd76d953bb2e1d2061cb8b40d09424be432fe08cce12a971bf2982b6b4d0546', null, null, null, null, null, null, null, null, null);
INSERT INTO `customer` VALUES ('1456@qq.com', null, 'pbkdf2:sha256:50000$f91NOo1W$96cc0ca6255df774dfc6f49174046f42a5312c5e9874d010365644958958372e', null, null, null, null, null, null, null, null, null);
INSERT INTO `customer` VALUES ('1567@qq.com', null, 'pbkdf2:sha256:50000$GQnag4Ku$77a7c638002c677136d911fdba192250b240e87b8b74262be9644189a71ba0fa', null, null, null, null, null, null, null, null, null);
INSERT INTO `customer` VALUES ('1678@qq.com', null, 'pbkdf2:sha256:50000$iz85TGIG$690b1949bf18e143717ef4302013ea358fa1618d950cb2c7b270424d1f3b8e75', null, null, null, null, null, null, null, null, null);
INSERT INTO `customer` VALUES ('1789@qq.com', null, 'pbkdf2:sha256:50000$I6KKQ0Sp$5a1b74b1c37f8fc2a0f2514280fd8ca9a5fdd31b1f8030aec983aedddfa437dd', null, null, null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for `flight`
-- ----------------------------
DROP TABLE IF EXISTS `flight`;
CREATE TABLE `flight` (
  `flight_num` varchar(50) NOT NULL,
  `departure_time` datetime NOT NULL,
  `arrival_time` datetime NOT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT '0.00',
  `rest_seat` int(5) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT '',
  `airline_name` varchar(50) NOT NULL,
  `departure_airport_name` varchar(50) NOT NULL,
  `arrival_airport_name` varchar(50) NOT NULL,
  `departure_city` varchar(50) NOT NULL,
  `arrival_city` varchar(50) NOT NULL,
  `airplane_id` varchar(50) NOT NULL,
  PRIMARY KEY (`flight_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of flight
-- ----------------------------
INSERT INTO `flight` VALUES ('CZ34', '2018-11-09 14:05:00', '2018-11-09 15:00:00', '560.00', '258', 'upcoming', 'China Eastern', 'TRL', 'TFG', 'Washington', 'San Francisco', 'LOP08');
INSERT INTO `flight` VALUES ('GTR', '2018-02-07 21:05:00', '2018-02-07 22:05:00', '343.00', '243', 'upcoming', 'China Eastern', 'FRT', 'JFK', 'Detroit', 'Chicago', 'ED005');
INSERT INTO `flight` VALUES ('VM54', '2012-05-15 21:05:00', '2012-05-15 21:05:00', '450.00', '196', 'upcoming', 'China Eastern', 'JFK', 'TFG', 'Chicago', 'San Francisco', 'GBH231');
INSERT INTO `flight` VALUES ('ZG54', '2018-11-09 19:00:00', '2018-11-09 20:00:00', '555.00', '231', 'upcoming', 'China Eastern', 'TFG', 'TRL', 'San Francisco', 'Washington', 'ZDR12');

-- ----------------------------
-- Table structure for `ticket`
-- ----------------------------
DROP TABLE IF EXISTS `ticket`;
CREATE TABLE `ticket` (
  `ticket_id` varchar(50) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `airline_name` varchar(50) NOT NULL,
  `flight_num` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT '0.00',
  `booking_agent_ID` varchar(50) DEFAULT NULL,
  `puechases_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ticket_id`),
  KEY `airline_name` (`airline_name`),
  KEY `flight_num` (`flight_num`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`),
  CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`flight_num`) REFERENCES `flight` (`flight_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ticket
-- ----------------------------
INSERT INTO `ticket` VALUES ('0CzdJk', '1234@qq.com', 'China Eastern', 'GTR', '343.00', 'Y0ION7PE', '2017-11-10 13:19:37');
INSERT INTO `ticket` VALUES ('0JP8om', '1789@qq.com', 'China Eastern', 'GTR', '343.00', 'n9XF3Ny7', '2018-10-10 17:49:05');
INSERT INTO `ticket` VALUES ('0ngkV1', '1234@qq.com', 'China Eastern', 'GTR', '343.00', 'Y0ION7PE', '2018-11-10 13:19:37');
INSERT INTO `ticket` VALUES ('0ngrPm', '1789@qq.com', 'China Eastern', 'GTR', '343.00', 'n9XF3Ny7', '2017-11-10 17:49:05');
INSERT INTO `ticket` VALUES ('0Nozdh', '1234@qq.com', 'China Eastern', 'GTR', '343.00', 'Y0ION7PE', '2017-10-10 13:19:37');
INSERT INTO `ticket` VALUES ('0NsdNo', '1234@qq.com', 'China Eastern', 'GTR', '343.00', 'Y0ION7PE', '2018-10-10 13:19:37');
INSERT INTO `ticket` VALUES ('2gCzdJ', '1567@qq.com', 'China Eastern', 'CZ34', '560.00', 'F5hZ2cwQ', '2017-11-10 17:48:25');
INSERT INTO `ticket` VALUES ('2gx6Gy', '1567@qq.com', 'China Eastern', 'CZ34', '560.00', 'F5hZ2cwQ', '2018-11-10 17:48:25');
INSERT INTO `ticket` VALUES ('2NoCzd', '1567@qq.com', 'China Eastern', 'CZ34', '560.00', 'F5hZ2cwQ', '2017-10-10 17:48:25');
INSERT INTO `ticket` VALUES ('4Cdvct', '1789@qq.com', 'China Eastern', 'ZG54', '555.00', 'Y0ION7PE', '2018-11-10 17:47:52');
INSERT INTO `ticket` VALUES ('4CzoJt', '1789@qq.com', 'China Eastern', 'ZG54', '555.00', 'Y0ION7PE', '2017-11-10 17:47:52');
INSERT INTO `ticket` VALUES ('4N8J8t', '1789@qq.com', 'China Eastern', 'ZG54', '555.00', 'Y0ION7PE', '2018-10-10 17:47:52');
INSERT INTO `ticket` VALUES ('4NoJ8t', '1789@qq.com', 'China Eastern', 'ZG54', '555.00', 'Y0ION7PE', '2017-10-10 17:47:52');
INSERT INTO `ticket` VALUES ('681heH', '1345@qq.com', 'China Eastern', 'GTR', '343.00', 'F5hZ2cwQ', '2018-11-10 14:12:35');
INSERT INTO `ticket` VALUES ('68ozoJ', '1345@qq.com', 'China Eastern', 'GTR', '343.00', 'F5hZ2cwQ', '2017-11-10 14:12:35');
INSERT INTO `ticket` VALUES ('6NaoPJ', '1345@qq.com', 'China Eastern', 'GTR', '343.00', 'F5hZ2cwQ', '2018-10-10 14:12:35');
INSERT INTO `ticket` VALUES ('6NJPoJ', '1345@qq.com', 'China Eastern', 'GTR', '343.00', 'F5hZ2cwQ', '2017-10-10 14:12:35');
INSERT INTO `ticket` VALUES ('8z0ngo', '1678@qq.com', 'China Eastern', 'ZG54', '555.00', 'ew4GqbOU', '2017-11-10 17:46:28');
INSERT INTO `ticket` VALUES ('8z0oNo', '1678@qq.com', 'China Eastern', 'ZG54', '555.00', 'ew4GqbOU', '2018-10-10 17:46:28');
INSERT INTO `ticket` VALUES ('8zkBoG', '1678@qq.com', 'China Eastern', 'ZG54', '555.00', 'ew4GqbOU', '2018-11-10 17:46:28');
INSERT INTO `ticket` VALUES ('cHrPmC', '1789@qq.com', 'China Eastern', 'GTR', '343.00', 'n9XF3Ny7', '2018-11-10 17:49:05');
INSERT INTO `ticket` VALUES ('CJdNgg', '1345@qq.com', 'China Eastern', 'CZ34', '560.00', 'F5hZ2cwQ', '2018-10-10 14:12:26');
INSERT INTO `ticket` VALUES ('CzPsoy', '1678@qq.com', 'China Eastern', 'GTR', '343.00', 'F5hZ2cwQ', '2018-10-10 17:48:34');
INSERT INTO `ticket` VALUES ('Dj8roM', '1567@qq.com', 'China Eastern', 'VM54', '450.00', 'Y0ION7PE', '2018-10-10 17:47:45');
INSERT INTO `ticket` VALUES ('DjMobk', '1567@qq.com', 'China Eastern', 'VM54', '450.00', 'Y0ION7PE', '2018-11-10 17:47:45');
INSERT INTO `ticket` VALUES ('dNaozd', '1567@qq.com', 'China Eastern', 'CZ34', '560.00', 'F5hZ2cwQ', '2018-10-10 17:48:25');
INSERT INTO `ticket` VALUES ('E7grDT', '1456@qq.com', 'China Eastern', 'CZ34', '560.00', 'Y0ION7PE', '2018-11-10 17:47:31');
INSERT INTO `ticket` VALUES ('EsdNrD', '1456@qq.com', 'China Eastern', 'CZ34', '560.00', 'Y0ION7PE', '2018-10-10 17:47:31');
INSERT INTO `ticket` VALUES ('H7FoRl', '1234@qq.com', 'China Eastern', 'VM54', '450.00', 'Y0ION7PE', '2018-11-10 13:28:56');
INSERT INTO `ticket` VALUES ('HoaPol', '1234@qq.com', 'China Eastern', 'VM54', '450.00', 'Y0ION7PE', '2018-10-10 13:28:56');
INSERT INTO `ticket` VALUES ('JPoNJr', '1456@qq.com', 'China Eastern', 'CZ34', '560.00', 'ew4GqbOU', '2018-10-10 17:46:46');
INSERT INTO `ticket` VALUES ('maJXyp', '1789@qq.com', 'China Eastern', 'CZ34', '560.00', 'n9XF3Ny7', '2018-11-10 17:48:54');
INSERT INTO `ticket` VALUES ('mJPNoo', '1789@qq.com', 'China Eastern', 'CZ34', '560.00', 'n9XF3Ny7', '2018-10-10 17:48:54');
INSERT INTO `ticket` VALUES ('S8rPoo', '1234@qq.com', 'China Eastern', 'ZG54', '555.00', 'Y0ION7PE', '2018-10-10 13:23:03');
INSERT INTO `ticket` VALUES ('sdNIam', '1234@qq.com', 'China Eastern', 'CZ34', '560.00', 'Y0ION7PE', '2018-11-10 13:20:25');
INSERT INTO `ticket` VALUES ('sdsdNm', '1234@qq.com', 'China Eastern', 'CZ34', '560.00', 'Y0ION7PE', '2018-10-10 13:20:25');
INSERT INTO `ticket` VALUES ('SkeEJ4', '1234@qq.com', 'China Eastern', 'ZG54', '555.00', 'Y0ION7PE', '2018-11-10 13:23:03');
INSERT INTO `ticket` VALUES ('tz3OUj', '1345@qq.com', 'China Eastern', 'CZ34', '560.00', 'F5hZ2cwQ', '2018-11-10 14:12:26');
INSERT INTO `ticket` VALUES ('UI5yQg', '1678@qq.com', 'China Eastern', 'GTR', '343.00', 'F5hZ2cwQ', '2018-11-10 17:48:34');
INSERT INTO `ticket` VALUES ('zAw8rp', '1456@qq.com', 'China Eastern', 'CZ34', '560.00', 'ew4GqbOU', '2018-11-10 17:46:46');
INSERT INTO `ticket` VALUES ('ZCPJ8C', '1678@qq.com', 'China Eastern', 'GTR', '343.00', 'Y0ION7PE', '2018-10-10 17:47:38');
INSERT INTO `ticket` VALUES ('ZCzdJP', '1678@qq.com', 'China Eastern', 'GTR', '343.00', 'Y0ION7PE', '2018-11-10 17:47:38');
