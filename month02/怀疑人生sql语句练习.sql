-- 创建表
-- 学生表
CREATE TABLE `Student`(
  `s_id` VARCHAR(20),
  `s_name` VARCHAR(20) NOT NULL DEFAULT '',
  `s_birth` VARCHAR(20) NOT NULL DEFAULT '',
  `s_sex` VARCHAR(10) NOT NULL DEFAULT '',
  PRIMARY KEY(`s_id`)
);

-- 课程表
CREATE TABLE `Course`(
  `c_id`  VARCHAR(20),
  `c_name` VARCHAR(20) NOT NULL DEFAULT '',
  `t_id` VARCHAR(20) NOT NULL,
  PRIMARY KEY(`c_id`)
);

-- 教师表
CREATE TABLE `Teacher`(
  `t_id` VARCHAR(20),
  `t_name` VARCHAR(20) NOT NULL DEFAULT '',
  PRIMARY KEY(`t_id`)
);

-- 成绩表
CREATE TABLE `Score`(
  `s_id` VARCHAR(20),
  `c_id`  VARCHAR(20),
  `s_score` INT(3),
  PRIMARY KEY(`s_id`,`c_id`)
);

-- 插入学生表测试数据
insert into Student values('01' , '赵雷' , '1990-01-01' , '男');
insert into Student values('02' , '钱电' , '1990-12-21' , '男');
insert into Student values('03' , '孙风' , '1990-05-20' , '男');
insert into Student values('04' , '李云' , '1990-08-06' , '男');
insert into Student values('05' , '周梅' , '1991-12-01' , '女');
insert into Student values('06' , '吴兰' , '1992-03-01' , '女');
insert into Student values('07' , '郑竹' , '1989-07-01' , '女');
insert into Student values('08' , '王菊' , '1990-01-20' , '女');

-- 课程表测试数据
insert into Course values('01' , '语文' , '02');
insert into Course values('02' , '数学' , '01');
insert into Course values('03' , '英语' , '03');
insert into Course values('04' , '物理' , '01');

-- 教师表测试数据
insert into Teacher values('01' , '张三');
insert into Teacher values('02' , '李四');
insert into Teacher values('03' , '王五');
insert into Teacher values('04' , 'Lina');
insert into Teacher values('05' , 'PeterZhang');


#成绩表测试数据
insert into Score values('01' , '01' , 80);
insert into Score values('01' , '02' , 90);
insert into Score values('01' , '03' , 99);
insert into Score values('01' , '04' , 67);
insert into Score values('02' , '01' , 70);
insert into Score values('02' , '02' , 60);
insert into Score values('02' , '03' , 80);
insert into Score values('02' , '04' , 98);
insert into Score values('03' , '01' , 80);
insert into Score values('03' , '02' , 80);
insert into Score values('03' , '03' , 80);
insert into Score values('04' , '01' , 50);
insert into Score values('04' , '02' , 30);
insert into Score values('04' , '03' , 20);
insert into Score values('04' , '04' , 40);
insert into Score values('05' , '01' , 76);
insert into Score values('05' , '02' , 87);
insert into Score values('06' , '01' , 31);
insert into Score values('06' , '03' , 34);
insert into Score values('07' , '02' , 89);
insert into Score values('07' , '03' , 98);
insert into Score values('08' , '01' , 89);
insert into Score values('08' , '02' , 98);


# 1.查询"01"课程比"02"课程成绩高的学生的信息及课程分数
select a.* , b.s_score 课程01的分数,c.s_score 课程02的分数 from Student a , Score b , Score c
where a.s_id = b.s_id and a.s_id = c.s_id and b.c_id = '01' and c.c_id = '02' and b.s_score > c.s_score;

# 2.查询"01"课程比"02"课程成绩低的学生的信息及课程分数
select a.* , b.s_score 课程01的分数,c.s_score 课程02的分数 from Student a , Score b , Score c
where a.s_id = b.s_id and a.s_id = c.s_id and b.c_id = '01' and c.c_id = '02' and b.s_score < c.s_score;

# 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩 保留小数点
SELECT Student.s_id,Student.s_name,avg(Score.s_score) FROM Student LEFT JOIN Score on Student.s_id=Score.s_id GROUP BY Student.s_id HAVING AVG(Score.s_score)>=60;

# 4.查询平均成绩小于60分的同学的学生编号和学生姓名和平均成绩 (包括有成绩的和无成绩的)
SELECT Student.s_id,Student.s_name,avg(Score.s_score) FROM Student LEFT JOIN Score on Student.s_id=Score.s_id GROUP BY Student.s_id HAVING AVG(Score.s_score)<60;

# 5.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
SELECT Student.s_id,Student.s_name,count(Score.s_score) 选课总数,SUM(Score.s_score) 总成绩 FROM Student LEFT JOIN Score on Student.s_id=Score.s_id GROUP BY Student.s_id;

# 6.查询不姓"李"姓老师的数量
SELECT count(*) 不姓‘李’姓老师的数量 FROM Teacher WHERE t_name not LIKE '李%';

# 7.查询学过"张三"老师授课的同学的信息
SELECT DISTINCT Student.* FROM Student,Teacher,Course,Score WHERE Student.s_id=Score.s_id and Score.c_id=Course.c_id and Course.t_id=Teacher.t_id and Teacher.t_name='张三';

# 8、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
SELECT Student.* FROM Student,Score a,Score b WHERE a.s_id=Student.s_id and b.s_id=Student.s_id and a.c_id='01' and b.c_id='02';

# 9、查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息
SELECT Student.* from Student LEFT JOIN Score a on Student.s_id=a.s_id WHERE a.c_id='01' and Student.s_id not in (SELECT Student.s_id FROM Student LEFT JOIN Score b on Student.s_id=b.s_id WHERE b.c_id='02');

# 10.查询没有学全所有课程的同学的信息
SELECT Score.s_id,any_value(Student.s_name) 姓名,any_value(Student.s_birth) 生日,any_value(Student.s_sex) 性别 FROM Student LEFT JOIN Score on Student.s_id=Score.s_id GROUP BY Score.s_id HAVING count(Score.c_id)<(SELECT count(*) FROM Course);

# 11.查询至少有一门课与学号为"03"的同学所学相同的同学的信息
SELECT DISTINCT Student.* FROM Student,(SELECT c_id from Score where s_id='03') as a,Score WHERE a.c_id=Score.c_id and Student.s_id=Score.s_id;

# 12. 查询和"05"号的同学学习的课程完全相同的其他同学的信息
SELECT DISTINCT Student.* FROM Student,Score WHERE Student.s_id=Score.s_id and Score.s_id<>'05' and Score.s_id not in (SELECT s_id FROM Score WHERE c_id not in (SELECT c_id FROM Score WHERE s_id='05'));

# 13. 查询没学过"张三"老师讲授的任一门课程的学生姓名
SELECT DISTINCT Student.s_name FROM Student LEFT JOIN Score on Student.s_id=Score.s_id WHERE Score.s_id not in (SELECT s_id FROM Score WHERE c_id in (SELECT Course.c_id FROM Teacher LEFT JOIN Course on Teacher.t_id=Course.t_id WHERE t_name='张三'));

# 14. 查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT Student.s_id,Student.s_name,AVG(Score.s_score) FROM Student LEFT JOIN Score on Student.s_id=Score.s_id WHERE Score.s_id in (SELECT Score.s_id FROM Score WHERE Score.s_score<60 GROUP BY Score.s_id HAVING count(*)>=2) GROUP BY Student.s_id,Student.s_name;

-- 15、检索"01"课程分数小于60，按分数降序排列的学生信息(asc升序 desc降序)
SELECT student.*,score.c_id,score.s_score FROM student LEFT JOIN score on student.s_id=score.s_id WHERE score.c_id='01' and score.s_score<60 ORDER BY score.s_score;
