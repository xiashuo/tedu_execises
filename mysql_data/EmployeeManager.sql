/*
 Navicat Premium Data Transfer

 Source Server         : 虚拟机mysql
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 192.168.17.132:3306
 Source Schema         : EmployeeManager

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 10/06/2020 20:34:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dept
-- ----------------------------
DROP TABLE IF EXISTS `dept`;
CREATE TABLE `dept`  (
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  `d_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`d_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dept
-- ----------------------------
INSERT INTO `dept` VALUES (1, '研发部');
INSERT INTO `dept` VALUES (2, '营销部');
INSERT INTO `dept` VALUES (3, '行政部');
INSERT INTO `dept` VALUES (4, '财务部');

-- ----------------------------
-- Table structure for emp_dept
-- ----------------------------
DROP TABLE IF EXISTS `emp_dept`;
CREATE TABLE `emp_dept`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `e_id` int(11) NOT NULL,
  `d_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `eid_fk`(`e_id`) USING BTREE,
  INDEX `did_fk`(`d_id`) USING BTREE,
  CONSTRAINT `did_fk` FOREIGN KEY (`d_id`) REFERENCES `dept` (`d_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `eid_fk` FOREIGN KEY (`e_id`) REFERENCES `employee` (`e_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of emp_dept
-- ----------------------------
INSERT INTO `emp_dept` VALUES (1, 1, 1);
INSERT INTO `emp_dept` VALUES (2, 2, 2);
INSERT INTO `emp_dept` VALUES (3, 3, 3);
INSERT INTO `emp_dept` VALUES (4, 4, 4);
INSERT INTO `emp_dept` VALUES (5, 5, 2);
INSERT INTO `emp_dept` VALUES (6, 6, 3);
INSERT INTO `emp_dept` VALUES (7, 7, 1);
INSERT INTO `emp_dept` VALUES (8, 8, 4);
INSERT INTO `emp_dept` VALUES (9, 9, 1);
INSERT INTO `emp_dept` VALUES (10, 10, 2);
INSERT INTO `emp_dept` VALUES (11, 11, 3);
INSERT INTO `emp_dept` VALUES (12, 1, 2);
INSERT INTO `emp_dept` VALUES (13, 3, 4);
INSERT INTO `emp_dept` VALUES (14, 6, 3);
INSERT INTO `emp_dept` VALUES (15, 9, 1);

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee`  (
  `e_id` int(11) NOT NULL AUTO_INCREMENT,
  `cn_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id_card` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `en_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `salary` int(11) NOT NULL,
  `dimission` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`e_id`) USING BTREE,
  UNIQUE INDEX `en_name_unique`(`en_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES (1, '张三', '42100219940714291X', 'jack', 12000, b'0');
INSERT INTO `employee` VALUES (2, '张三', '42100219940714291X', 'boll', 13000, b'0');
INSERT INTO `employee` VALUES (3, '李四', '42100219930714291X', 'lisi', 14000, b'0');
INSERT INTO `employee` VALUES (4, '王五', '42100219920714291X', 'wangwu', 13000, b'0');
INSERT INTO `employee` VALUES (5, '赵柳', '42100219910714291X', 'zhaoliu', 15000, b'0');
INSERT INTO `employee` VALUES (6, '孙起', '42100219940714292X', 'suanqi', 16000, b'0');
INSERT INTO `employee` VALUES (7, '王八', '42100219940714293X', 'wangba', 18000, b'0');
INSERT INTO `employee` VALUES (8, '周久', '42100219940714294X', 'zhoujiu', 17000, b'0');
INSERT INTO `employee` VALUES (9, '钱十', '42100219940714295X', 'qianshi', 11000, b'0');
INSERT INTO `employee` VALUES (10, '吴天', '42100219940714261X', 'wutian', 10000, b'0');
INSERT INTO `employee` VALUES (11, '郑板', '42100219940714271X', 'zhengban', 19000, b'0');

SET FOREIGN_KEY_CHECKS = 1;
