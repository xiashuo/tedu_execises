/*
 Navicat Premium Data Transfer

 Source Server         : 虚拟机数据库
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 192.168.10.131:3306
 Source Schema         : stu

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 09/06/2020 22:19:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cls
-- ----------------------------
DROP TABLE IF EXISTS `cls`;
CREATE TABLE `cls`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` tinyint(3) UNSIGNED NOT NULL,
  `sex` enum('w','m') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` float NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cls
-- ----------------------------
INSERT INTO `cls` VALUES (2, 'Baron', 10, 'm', 91);
INSERT INTO `cls` VALUES (3, 'Jame', 9, 'm', 90);
INSERT INTO `cls` VALUES (4, 'Lucy', 17, 'w', 81);

-- ----------------------------
-- Table structure for dept
-- ----------------------------
DROP TABLE IF EXISTS `dept`;
CREATE TABLE `dept`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dept
-- ----------------------------
INSERT INTO `dept` VALUES (1, '技术部');
INSERT INTO `dept` VALUES (2, '销售部');
INSERT INTO `dept` VALUES (3, '市场部');
INSERT INTO `dept` VALUES (4, '行政部');

-- ----------------------------
-- Table structure for interest
-- ----------------------------
DROP TABLE IF EXISTS `interest`;
CREATE TABLE `interest`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hobby` set('sing','dance','draw') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` decimal(6, 2) NULL DEFAULT NULL,
  `remark` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of interest
-- ----------------------------

-- ----------------------------
-- Table structure for marathon
-- ----------------------------
DROP TABLE IF EXISTS `marathon`;
CREATE TABLE `marathon`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `athlete` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` date NULL DEFAULT NULL,
  `registration_time` datetime(0) NULL DEFAULT NULL,
  `performance` time(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of marathon
-- ----------------------------
INSERT INTO `marathon` VALUES (1, '麦克', '1994-07-14', '2020-03-28 00:00:00', '02:30:20');
INSERT INTO `marathon` VALUES (2, '托里', '1993-03-14', '2020-03-28 00:00:00', '02:20:20');

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS `person`;
CREATE TABLE `person`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` tinyint(4) NULL DEFAULT 0,
  `sex` enum('m','w','o') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT 'o',
  `salary` decimal(8, 2) NULL DEFAULT 250.00,
  `hire_date` date NOT NULL,
  `dept_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `dept_fk`(`dept_id`) USING BTREE,
  CONSTRAINT `dept_fk` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of person
-- ----------------------------
INSERT INTO `person` VALUES (1, 'Lily', 29, 'w', 20000.00, '2017-04-03', 2);
INSERT INTO `person` VALUES (2, 'Tom', 27, 'm', 16000.00, '2019-10-03', 1);
INSERT INTO `person` VALUES (3, 'Joy', 30, 'm', 28000.00, '2016-04-03', 1);
INSERT INTO `person` VALUES (4, 'Emma', 24, 'w', 8000.00, '2019-05-08', 4);
INSERT INTO `person` VALUES (5, 'Abby', 28, 'w', 17000.00, '2018-11-03', 3);
INSERT INTO `person` VALUES (6, 'Jame', 32, 'm', 22000.00, '2017-04-07', 4);

-- ----------------------------
-- Table structure for sanguo
-- ----------------------------
DROP TABLE IF EXISTS `sanguo`;
CREATE TABLE `sanguo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` enum('男','女') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `country` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `attack` int(11) NOT NULL,
  `defense` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sanguo
-- ----------------------------
INSERT INTO `sanguo` VALUES (1, '曹操', '男', '魏', 256, 63);
INSERT INTO `sanguo` VALUES (2, '张辽', '男', '魏', 300, 69);
INSERT INTO `sanguo` VALUES (3, '甄姬', '女', '魏', 168, 34);
INSERT INTO `sanguo` VALUES (4, '夏侯渊', '男', '魏', 300, 83);
INSERT INTO `sanguo` VALUES (5, '刘备', '男', '蜀', 220, 59);
INSERT INTO `sanguo` VALUES (6, '诸葛亮', '男', '蜀', 170, 54);
INSERT INTO `sanguo` VALUES (7, '赵云', '男', '蜀', 360, 70);
INSERT INTO `sanguo` VALUES (8, '张飞', '男', '蜀', 370, 80);
INSERT INTO `sanguo` VALUES (9, '孙尚香', '女', '蜀', 249, 62);
INSERT INTO `sanguo` VALUES (10, '大乔', '女', '吴', 190, 44);
INSERT INTO `sanguo` VALUES (11, '小乔', '女', '吴', 188, 39);
INSERT INTO `sanguo` VALUES (12, '周瑜', '男', '吴', 300, 60);
INSERT INTO `sanguo` VALUES (13, '吕蒙', '男', '吴', 300, 71);

-- ----------------------------
-- Procedure structure for get_score_by_name
-- ----------------------------
DROP PROCEDURE IF EXISTS `get_score_by_name`;
delimiter ;;
CREATE PROCEDURE `get_score_by_name`(INOUT `uname` varchar(32))
BEGIN
SELECT score from cls WHERE name=uname;

END
;;
delimiter ;

-- ----------------------------
-- Function structure for score_cha
-- ----------------------------
DROP FUNCTION IF EXISTS `score_cha`;
delimiter ;;
CREATE FUNCTION `score_cha`(id1 int,id2 int)
 RETURNS int(11)
BEGIN
DECLARE a int;
DECLARE b int;
set a=(SELECT score from cls WHERE id=id1);
set b=(SELECT score from cls WHERE id=id2);
return a-b;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
