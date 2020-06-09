/*
 Navicat Premium Data Transfer

 Source Server         : 虚拟机数据库
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 192.168.10.131:3306
 Source Schema         : exercise

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 09/06/2020 22:18:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`cid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (1, '三年二班');
INSERT INTO `class` VALUES (2, '三年三班');
INSERT INTO `class` VALUES (3, '三年一班');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacher_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`cid`) USING BTREE,
  INDEX `teacher_id`(`teacher_id`) USING BTREE,
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`tid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, '生物', 1);
INSERT INTO `course` VALUES (2, '体育', 1);
INSERT INTO `course` VALUES (3, '物理', 2);

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NULL DEFAULT NULL,
  `course_id` int(11) NULL DEFAULT NULL,
  `number` int(3) NOT NULL,
  PRIMARY KEY (`sid`) USING BTREE,
  INDEX `student_id`(`student_id`) USING BTREE,
  INDEX `course_id`(`course_id`) USING BTREE,
  CONSTRAINT `score_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `score_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES (1, 1, 1, 60);
INSERT INTO `score` VALUES (2, 1, 2, 59);
INSERT INTO `score` VALUES (3, 2, 2, 100);
INSERT INTO `score` VALUES (4, 3, 2, 78);
INSERT INTO `score` VALUES (5, 4, 3, 66);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` enum('male','female','others') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'male',
  `class_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`sid`) USING BTREE,
  INDEX `class_id`(`class_id`) USING BTREE,
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '钢蛋', 'female', 1);
INSERT INTO `student` VALUES (2, '铁锤', 'female', 1);
INSERT INTO `student` VALUES (3, '山炮', 'male', 2);
INSERT INTO `student` VALUES (4, '彪哥', 'male', 3);

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`tid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES (1, '波多老师');
INSERT INTO `teacher` VALUES (2, '苍老师');
INSERT INTO `teacher` VALUES (3, '小泽老师');

-- ----------------------------
-- View structure for teacher_course_count
-- ----------------------------
DROP VIEW IF EXISTS `teacher_course_count`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `teacher_course_count` AS select `teacher`.`tname` AS `tname`,count(`course`.`cname`) AS `count(cname)` from (`teacher` left join `course` on((`teacher`.`tid` = `course`.`teacher_id`))) group by `teacher`.`tname`;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('小泽老师', 0);
INSERT INTO `teacher` VALUES ('波多老师', 2);
INSERT INTO `teacher` VALUES ('苍老师', 1);

-- ----------------------------
-- Function structure for search_by_id
-- ----------------------------
DROP FUNCTION IF EXISTS `search_by_id`;
delimiter ;;
CREATE FUNCTION `search_by_id`(id int)
 RETURNS varchar(32) CHARSET utf8
BEGIN

RETURN (SELECT cname from course WHERE cid=id);
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for test
-- ----------------------------
DROP PROCEDURE IF EXISTS `test`;
delimiter ;;
CREATE PROCEDURE `test`(out num int)
BEGIN
SELECT num;
set num=100;
SELECT num;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
