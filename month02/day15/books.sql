/*
 Navicat Premium Data Transfer

 Source Server         : 虚拟机数据库
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 192.168.10.131:3306
 Source Schema         : books

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 09/06/2020 22:17:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `birthplace` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of author
-- ----------------------------
INSERT INTO `author` VALUES (1, '鲁迅', '浙江');
INSERT INTO `author` VALUES (2, '老舍', '浙江');
INSERT INTO `author` VALUES (3, '金庸', '浙江');
INSERT INTO `author` VALUES (4, '巴金', '浙江');

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `publish_date` year NOT NULL,
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `author_fk`(`author_id`) USING BTREE,
  INDEX `publisher_fk`(`publisher_id`) USING BTREE,
  CONSTRAINT `author_fk` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `publisher_fk` FOREIGN KEY (`publisher_id`) REFERENCES `publisher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (2, '狂人日记', 30.00, 2001, NULL, 1, 1);
INSERT INTO `book` VALUES (3, '朝花夕拾', 28.00, 2002, NULL, 1, 2);
INSERT INTO `book` VALUES (4, '射雕英雄传', 33.00, 1995, NULL, 3, 3);
INSERT INTO `book` VALUES (5, '鹿鼎记', 22.00, 2003, NULL, 3, 3);
INSERT INTO `book` VALUES (6, '骆驼祥子', 33.00, 2002, NULL, 2, 4);
INSERT INTO `book` VALUES (7, '茶馆', 25.00, 2003, NULL, 2, 4);
INSERT INTO `book` VALUES (8, '家', 33.00, 1999, NULL, 4, 5);
INSERT INTO `book` VALUES (9, '寒夜', 24.00, 2002, NULL, 4, 5);

-- ----------------------------
-- Table structure for publisher
-- ----------------------------
DROP TABLE IF EXISTS `publisher`;
CREATE TABLE `publisher`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of publisher
-- ----------------------------
INSERT INTO `publisher` VALUES (1, '中国教育出版社');
INSERT INTO `publisher` VALUES (2, '中国人民出版社');
INSERT INTO `publisher` VALUES (3, '人民文学出版社');
INSERT INTO `publisher` VALUES (4, '商务印书馆');
INSERT INTO `publisher` VALUES (5, '长江文艺出版社');

SET FOREIGN_KEY_CHECKS = 1;
