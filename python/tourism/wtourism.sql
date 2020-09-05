SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `people`
-- ----------------------------
DROP TABLE IF EXISTS `people`;
CREATE TABLE `people` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `content` varchar(100) NOT NULL,
  `create_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of people
-- ----------------------------
INSERT INTO `people` VALUES ('1', '凤凰城', '2019010309123728c88873d7764ce9be4de0bb5ee59526.png', '你们可知道凤凰鸟吗？凤凰鸟是幸福鸟，哪里有凤凰，哪里就有幸福。凤凰姐妹一共七个，住在长江南边的一架高山上，凤凰常常为人们造福，所以江南很美丽，山是青山，水是绿水，鲜花遍地香，树木都成行，人长得清秀健壮', '2019-01-03 09:12:37');
INSERT INTO `people` VALUES ('4', '宁夏沙湖生态旅游区', '20190103092944855bf0ca56dd4f869ba26fca0bdc1664.png', '国家5A级景区。沙湖地处贺兰山下、黄河金岸，距宁夏回族自治区首府银川市42公里。景区总面积80.10平方公里，20余平方公里沙漠与40余平方公里水域毗邻而居，既有大漠戈壁之雄浑，又有江南水乡之秀美，被', '2019-01-03 09:29:44');
INSERT INTO `people` VALUES ('5', '镇北堡西部影城', '20190103093022170b1cd7d5834cbe91e0af682bec3e37.png', '国家AAAAA级旅游景区。位于银川市西夏区镇北堡镇。距银川市中心区35公里，火车站25公里，河东机场48公里，110国道穿行其间，交通方便，是贺兰山东麓旅游区的亮点。镇北堡西部影城在中国众多的影视城中', '2019-01-03 09:30:22');


SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `natural`
-- ----------------------------
DROP TABLE IF EXISTS `natural`;
CREATE TABLE `natural` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `content` varchar(100) NOT NULL,
  `create_time` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of natural
-- ----------------------------
INSERT INTO `natural` VALUES ('2', '火山寨', '20190103090832fa738188342549978c6103a22194ce19.png', '火石寨国家地质（森林）公园位于宁夏西吉县城以北15公里，属六盘山西部余脉。火石寨，是镶嵌在中国西部黄土高原上的一颗璀璨的明珠，以大西北垄断性旅游资源丹霞地貌著称，自然风光、人文景观、回族风情相互交织构', '2019-01-01 21:55:33.766565');
INSERT INTO `natural` VALUES ('4', '沙坡头', '201901030926537e33ce84ef924d09a7bb8f3eeba7af00.png', '国家AAAAA级旅游景区，国家级沙漠生态自然保护区，全球环保500佳单位，全民健身二十个著名景观，科技进步特别奖。', '2019-01-03 09:26:53.541481');
INSERT INTO `natural` VALUES ('5', '水洞沟', '2019010309273261efbf6f983946eeb36d9332b9319088.png', '宁夏水洞沟旅游景区是中国最早发掘的旧石器时代文化遗址，被誉为“中国史前考古的发祥地”、“中西方文化交流的历史见证”，被国家列为“最具中华文明意义的百项考古发现”之一。是全国重点文物保护单位，国家AAA', '2019-01-03 09:27:32.846550');


SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `history`
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `content` varchar(100) NOT NULL,
  `create_time` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of history
-- ----------------------------
INSERT INTO `history` VALUES ('1', '历史文物----鎏金铜牛', '2019010309095150c6a558bb0f485790263f8859e89faa.png', '1977年宁夏银川西夏陵区出土的之间青铜牛长120厘米、宽38厘米、高45厘米、重188公斤。屈肢而卧，体态健壮，比例匀称，造型逼真，个体硕大，是西夏艺术品中的珍品。', '2019-01-01 21:56:53.839673');
INSERT INTO `history` VALUES ('3', '雕龙石栏柱', '20190103092341a54b0943e99a45fd8fde2be11a5707db.png', '1974年出土于宁夏银川西夏陵区。系一件西夏建筑构件中十分珍贵的石雕艺术品。', '2019-01-03 09:23:41.495764');
INSERT INTO `history` VALUES ('4', '西夏文佛经《吉祥遍至口和本续》', '2019010309241656e3975926ca4b6083deff338e593a87.png', '1991年出土于宁夏贺兰县拜寺沟方塔。 这是一部保存较好\"木刻本西夏文佛经,白麻纸精印,蝴蝶装,共9册,约10万字。这部1991年出土的西夏文佛经是迄今世界上发现的最早的木活字扳印本。', '2019-01-03 09:24:16.454604');
INSERT INTO `history` VALUES ('5', '石螭首', '20190103092534b8aa47ef80874228baa85ad992c51311.png', '1974年出土于宁夏银川西夏陵区6号陵。螭口衔珠，眉骨突出，双目圆睁，颈部有一圈鬃毛，两角用浮雕手法刻出，神态威猛，气势非凡，后端为楔形榫头，可套嵌在建筑物上。', '2019-01-03 09:25:34.442412');
INSERT INTO `history` VALUES ('6', '西夏文残碑', '2019010309261019637bfb9c324cc48dd2d58aaadfe557.png', '1974年出土于宁夏银川市西夏陵区。此块残碑为西夏陵出土的形体较大，字数较多的一块西夏文碑。砂岩雕凿，阴刻楷书，所刻碑文笔画匀称，笔力遒劲厚重，是不可多得的西夏书法珍品。西夏文字多为比较工整的楷书。', '2019-01-03 09:26:10.857486');


SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', '银川美食');
INSERT INTO `category` VALUES ('2', '中卫美食');
INSERT INTO `category` VALUES ('3', '固原美食');



SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'admin', '123456');


SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `img` varchar(100) NOT NULL,
  `category_id` int(10) NOT NULL,
  `content` text NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('1', '盖碗茶', '2018111810412306aec9542dec4ab7b2e2024ae601a023.jpg', '1', '最主要的当然是茶叶和冰糖两样，其他的配料有枸杞子、沙枣、红枣、核桃仁、葡萄干、桂圆、话梅等滋补佳品，称之为八宝茶。沏茶的水要沸腾的水，称之为“牡丹花水”。', '2018-11-18 10:41:23');
INSERT INTO `product` VALUES ('2', '清蒸羊羔肉', '20181118104249d6302f71b06244bbb61dc58dc92e170c.jpg', '2', '宁夏羊羔肉细嫩鲜美，没有膻味。羊羔肉最好选用胸叉、上脊骨部位，剁成长方形条，用清凉水洗净，摆在碗内，放上生姜、大葱、大蒜；再放上几粒生花椒，上笼蒸30分钟左右；然后扣至汤盘内上桌，配以醋、蒜汁、盐等调料佐食。', '2018-11-18 10:42:50');
INSERT INTO `product` VALUES ('3', '烩羊杂碎', '20190103085339ab8a9774340d40cbb58c6ad8b6f7262b.png', '1', '风味独特。其制作方法是：用羊的内脏、头蹄肉，经仔细冲洗后，入开水锅煮熟后捞出，切成丝。以原汤下入切好的杂碎丝，加葱、姜、蒜末、红辣油、味精、香菜，即成烩羊杂碎。那红色的便是辣椒油，绿色的是青葱香菜末，油色下面是乳白色的鲜汤，喝一口鲜汤吃一口杂碎，不膻不腻，味道香醇浓郁。', '2018-11-18 10:43:10');
