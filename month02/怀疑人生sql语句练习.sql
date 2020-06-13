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


-- # 1.查询"01"课程比"02"课程成绩高的学生的信息及课程分数
select a.* , b.s_score 课程01的分数,c.s_score 课程02的分数
from Student a , Score b , Score c
where a.s_id = b.s_id and a.s_id = c.s_id and b.c_id = '01' and c.c_id = '02' and b.s_score > c.s_score;

-- # 2.查询"01"课程比"02"课程成绩低的学生的信息及课程分数
select a.* , b.s_score 课程01的分数,c.s_score 课程02的分数
from Student a , Score b , Score c
where a.s_id = b.s_id and a.s_id = c.s_id and b.c_id = '01' and c.c_id = '02' and b.s_score < c.s_score;

-- # 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩 保留小数点
SELECT Student.s_id,Student.s_name,avg(Score.s_score)
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
GROUP BY Student.s_id
HAVING AVG(Score.s_score)>=60;

-- # 4.查询平均成绩小于60分的同学的学生编号和学生姓名和平均成绩 (包括有成绩的和无成绩的)
SELECT Student.s_id,Student.s_name,avg(Score.s_score)
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
GROUP BY Student.s_id
HAVING AVG(Score.s_score)<60;

-- # 5.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
SELECT Student.s_id,Student.s_name,count(Score.s_score) 选课总数,SUM(Score.s_score) 总成绩
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
GROUP BY Student.s_id;

-- # 6.查询不姓"李"姓老师的数量
SELECT count(*) 不姓李姓老师的数量
FROM Teacher
WHERE t_name not LIKE '李%';

-- # 7.查询学过"张三"老师授课的同学的信息
SELECT DISTINCT Student.*
FROM Student,Teacher,Course,Score
WHERE Student.s_id=Score.s_id and Score.c_id=Course.c_id and Course.t_id=Teacher.t_id and Teacher.t_name='张三';

-- # 8、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
SELECT Student.*
FROM Student,Score a,Score b
WHERE a.s_id=Student.s_id and b.s_id=Student.s_id and a.c_id='01' and b.c_id='02';

-- # 9、查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息
SELECT Student.*
from Student LEFT JOIN Score a on Student.s_id=a.s_id
WHERE a.c_id='01' and Student.s_id not in (
    SELECT Student.s_id
    FROM Student LEFT JOIN Score b on Student.s_id=b.s_id
    WHERE b.c_id='02'
);

-- # 10.查询没有学全所有课程的同学的信息
SELECT Score.s_id,any_value(Student.s_name) 姓名,any_value(Student.s_birth) 生日,any_value(Student.s_sex) 性别
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
GROUP BY Score.s_id
HAVING count(Score.c_id)<(
    SELECT count(*)
    FROM Course
);

-- # 11.查询至少有一门课与学号为"03"的同学所学相同的同学的信息
SELECT DISTINCT Student.*
FROM Student,(
    SELECT c_id
    from Score
    where s_id='03'
) as a,Score
WHERE a.c_id=Score.c_id and Student.s_id=Score.s_id;

-- # 12. 查询和"05"号的同学学习的课程完全相同的其他同学的信息
SELECT DISTINCT Student.*
FROM Student,Score
WHERE Student.s_id=Score.s_id and Score.s_id<>'05' and Score.s_id not in (
    SELECT s_id
    FROM Score
    WHERE c_id not in (
        SELECT c_id
        FROM Score
        WHERE s_id='05'
    )
);

-- # 13. 查询没学过"张三"老师讲授的任一门课程的学生姓名
SELECT DISTINCT Student.s_name
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
WHERE Score.s_id not in (
    SELECT s_id
    FROM Score
    WHERE c_id in (
        SELECT Course.c_id
        FROM Teacher LEFT JOIN Course on Teacher.t_id=Course.t_id
        WHERE t_name='张三'
    )
);

-- # 14. 查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT Student.s_id,Student.s_name,AVG(Score.s_score)
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
WHERE Score.s_id in (
    SELECT Score.s_id
    FROM Score
    WHERE Score.s_score<60
    GROUP BY Score.s_id
    HAVING count(*)>=2
)
GROUP BY Student.s_id,Student.s_name;

-- 15、检索"01"课程分数小于60，按分数降序排列的学生信息(asc升序 desc降序)
SELECT student.*,score.c_id,score.s_score
FROM student LEFT JOIN score on student.s_id=score.s_id
WHERE score.c_id='01' and score.s_score<60
ORDER BY score.s_score;

-- 16、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
SELECT Student.s_id,Student.s_name 姓名,max(CASE WHEN c_id='01' THEN s_score ELSE NULL END) 语文,max(CASE WHEN c_id='02' THEN s_score ELSE NULL END) 数学,max(CASE WHEN c_id='03' THEN s_score ELSE NULL END) 英语,max(CASE WHEN c_id='04' THEN s_score ELSE NULL END) 物理,avg(Score.s_score) 平均成绩
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
GROUP BY Student.s_id,Student.s_name
ORDER BY AVG(Score.s_score) DESC;

-- 17、查询各科成绩最高分、最低分和平均分：以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
SELECT Course.c_id 课程id,Course.c_name 课程名,MAX(Score.s_score) 最高分,MIN(Score.s_score) 最低分,AVG(Score.s_score) 平均分,sum(case WHEN s_score>=60 THEN 1 ELSE 0 END)/count(s_score) 及格率,sum(case WHEN s_score>=70 and s_score<80 THEN 1 ELSE 0 END)/count(s_score) 中等率,sum(case WHEN s_score>=80 and s_score<90 THEN 1 ELSE 0 END)/count(s_score) 优良率,sum(case WHEN s_score>=90 THEN 1 ELSE 0 END)/count(s_score) 优秀率
FROM Course LEFT JOIN Score ON Course.c_id=Score.c_id
GROUP BY Course.c_id,Course.c_name;

-- 18 查询学生的总成绩并进行排名
SELECT Student.s_id,Student.s_name,sum(s_score)
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
GROUP BY Student.s_id,Student.s_name
ORDER BY sum(s_score) DESC;

-- 19查询不同老师所教不同课程平均分从高到低显示
SELECT Teacher.t_id 教师编号,Teacher.t_name 姓名,Course.c_name 课程名,avg(s_score) 平均分
FROM Teacher,Course,Score
WHERE Teacher.t_id=Course.t_id and Course.c_id=Score.c_id
GROUP BY Teacher.t_id,Teacher.t_name,Course.c_name
ORDER BY avg(s_score);

-- 20、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩
SELECT c_id,s_id,s_score
FROM score a
WHERE (
    SELECT count(*)
    FROM score b
    WHERE a.c_id = b.c_id AND a.s_score < b.s_score
) BETWEEN 1 and 2
ORDER BY c_id, s_score DESC;

-- 21 统计各科成绩各分数段人数：课程编号,课程名称,[100-85],[85-70],[70-60],[0-60]及所占百分比
SELECT Course.c_id 课程id,Course.c_name 课程名,sum(case when s_score>=85 then 1 else 0 end)/count(s_score) '[100-85]',sum(case when s_score>=70 and s_score<85 then 1 else 0 end)/count(s_score) '[85-70]', sum(case when s_score>=60 and s_score<70 then 1 else 0 end)/count(s_score) '[70-60]',sum(case when s_score<60 then 1 else 0 end)/count(s_score) '[0-60]'
FROM Course LEFT JOIN Score on Course.c_id=Score.c_id
GROUP BY Course.c_id,Course.c_name;

-- 22、查询学生平均成绩及其名次
SELECT c.*,@i:=@i+1 排名
FROM (
    SELECT a.s_id 学生编号,a.s_name 姓名,AVG(s_score) 平均成绩
    FROM student a,score b
    WHERE a.s_id=b.s_id
    GROUP BY a.s_id,a.s_name
    ORDER BY AVG(s_score) DESC
) c,(SELECT @i:=0) d;

-- 23/查询各科成绩前三名的记录
SELECT c_id,s_id,s_score
FROM score a
WHERE (
    SELECT count(1)
    FROM score b
    WHERE a.c_id = b.c_id AND a.s_score < b.s_score
) < 3
ORDER BY c_id, s_score DESC;

-- 24 查询出只有两门课程的全部学生的学号和姓名
SELECT student.s_id 学号,student.s_name 姓名
FROM student LEFT JOIN score on student.s_id=score.s_id
GROUP BY student.s_id,student.s_name
HAVING count(c_id)=2;

-- 25、查询男生、女生人数
SELECT s_sex 性别,count(*) 人数
FROM student
GROUP BY s_sex;

-- 26、查询同名同性学生名单，并统计同名人数
SELECT c.s_name 同名同姓学生,count(*) 人数
FROM (
    SELECT a.*
    from Student a
    WHERE (
        SELECT count(*)
        FROM Student b
        WHERE b.s_name=a.s_name
    ) >1
) c
GROUP BY c.s_name;

-- 27 查询课程名称为"数学"，且分数低于60的学生姓名和分数
SELECT Student.s_name 数学分数低于60的学生,Score.s_score 分数
FROM Student,Course,Score
WHERE Student.s_id=Score.s_id and Course.c_id=Score.c_id and Course.c_name='数学' and Score.s_score<60;

-- 28 查询所有学生的课程及分数情况；
SELECT Student.s_id 学号,Student.s_name 姓名,max(case when Course.c_name='语文' then s_score else null end) 语文, max(case when Course.c_name='数学' then s_score else null end) 数学,max(case when Course.c_name='英语' then s_score else null end) 英语,max(case when Course.c_name='物理' then s_score else null end) 物理
FROM Student,Course,Score
WHERE Student.s_id=Score.s_id and Course.c_id=Score.c_id
GROUP BY Student.s_id,Student.s_name;

-- 29、查询任何一门课程成绩在70分以上的姓名、课程名称和分数；
SELECT Student.s_name,Course.c_name,Score.s_score
FROM Student,Course,Score
WHERE Student.s_id=Score.s_id and Course.c_id=Score.c_id and Score.s_score>70;

-- 30 查询不及格的课程
SELECT Student.s_name,Course.c_name,Score.s_score
FROM Student,Course,Score
WHERE Student.s_id=Score.s_id and Course.c_id=Score.c_id and Score.s_score<60;

-- 31查询课程编号为01且课程成绩在80分以上的学生的学号和姓名；
SELECT Student.s_id 学号,Student.s_name 姓名
FROM Student LEFT JOIN Score on Student.s_id=Score.s_id
WHERE Score.c_id='01' and Score.s_score>=80;

-- 32 查询选修"张三"老师所授课程(可能有多个课程)的学生中，成绩最高的学生信息及其成绩
SELECT c_id,s_id,s_score
FROM score a
WHERE (
    SELECT count(*)
    FROM score b
    WHERE a.c_id = b.c_id AND a.s_score < b.s_score
) =0 and c_id in (
    SELECT c_id
    FROM course LEFT JOIN teacher on course.t_id=teacher.t_id
    WHERE t_name='张三'
)
ORDER BY c_id, s_score DESC;

-- 33查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
SELECT DISTINCT a.s_id,a.c_id,a.s_score
FROM score a LEFT JOIN score b on a.s_id=b.s_id
WHERE a.c_id<>b.c_id and a.s_score=b.s_score;

-- 34查询每门课程成绩最好的前两名
SELECT c_id,s_id,s_score
FROM score a
WHERE (
    SELECT count(1)
    FROM score b
    WHERE a.c_id = b.c_id AND a.s_score < b.s_score
) < 2
ORDER BY c_id, s_score DESC;

-- 35、统计每门课程的学生选修人数（超过5人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
SELECT Score.c_id 课程号,count(*)
FROM Score
GROUP BY Score.c_id
HAVING count(*)>5
ORDER BY count(*) DESC,Score.c_id;

-- -- 36.查询各学生的年龄
SELECT s_id 学号,s_name 姓名,(DATE_FORMAT(NOW(),'%Y')-DATE_FORMAT(student.s_birth,'%Y')) 年龄
FROM student;

-- 37 查询本月过生日的学生
SELECT s_name 本月过生日的学生
FROM student
WHERE DATE_FORMAT(s_birth,'%m')=DATE_FORMAT(NOW(),'%m');

-- 38、 查询本周过生日的学生
SELECT s_name 本周过生日的学生
FROM student
WHERE DATE_FORMAT(s_birth,'%u')=DATE_FORMAT(NOW(),'%u');
