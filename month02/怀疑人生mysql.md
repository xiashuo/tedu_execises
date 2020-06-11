sql语句练习

/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

##建表
#学生表
create database  if not exists TestSchool;
use TestSchool;
CREATE TABLE `Student`(
  `s_id` VARCHAR(20),
  `s_name` VARCHAR(20) NOT NULL DEFAULT '',
  `s_birth` VARCHAR(20) NOT NULL DEFAULT '',
  `s_sex` VARCHAR(10) NOT NULL DEFAULT '',
  PRIMARY KEY(`s_id`)
);
#课程表
CREATE TABLE `Course`(
  `c_id`  VARCHAR(20),
  `c_name` VARCHAR(20) NOT NULL DEFAULT '',
  `t_id` VARCHAR(20) NOT NULL,
  PRIMARY KEY(`c_id`)
);
#教师表
CREATE TABLE `Teacher`(
  `t_id` VARCHAR(20),
  `t_name` VARCHAR(20) NOT NULL DEFAULT '',
  PRIMARY KEY(`t_id`)
);
#成绩表
CREATE TABLE `Score`(
  `s_id` VARCHAR(20),
  `c_id`  VARCHAR(20),
  `s_score` INT(3),
  PRIMARY KEY(`s_id`,`c_id`)
);
#插入学生表测试数据
insert into Student values('01' , '赵雷' , '1990-01-01' , '男');
insert into Student values('02' , '钱电' , '1990-12-21' , '男');
insert into Student values('03' , '孙风' , '1990-05-20' , '男');
insert into Student values('04' , '李云' , '1990-08-06' , '男');
insert into Student values('05' , '周梅' , '1991-12-01' , '女');
insert into Student values('06' , '吴兰' , '1992-03-01' , '女');
insert into Student values('07' , '郑竹' , '1989-07-01' , '女');
insert into Student values('08' , '王菊' , '1990-01-20' , '女');
#课程表测试数据
insert into Course values('01' , '语文' , '02');
insert into Course values('02' , '数学' , '01');
insert into Course values('03' , '英语' , '03');
insert into Course values('04' , '物理' , '01');

#教师表测试数据
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

1.查询"01"课程比"02"课程成绩高的学生的信息及课程分数
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



SQL join 用于根据两个或多个表中的列之间的关系，从这些表中查询数据
INNER JOIN（内连接），在表中存在至少一个匹配时，INNER JOIN 关键字返回行(注释：INNER JOIN 与 JOIN 是相同的。)
JOIN: 如果表中有至少一个匹配，则返回行
LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
FULL JOIN: 只要其中一个表中存在匹配，就返回行

2.查询"01"课程比"02"课程成绩低的学生的信息及课程分数
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩 保留小数点
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

#ROUND(column_name,decimals-返回的小数位数)

4.查询平均成绩小于60分的同学的学生编号和学生姓名和平均成绩 (包括有成绩的和无成绩的)
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



5.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



6.查询不姓"李"姓老师的数量
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

    

在 SQL 中，可使用以下通配符：

通配符	描述
%	替代一个或多个字符
_	仅替代一个字符
regexp/not regexp [charlist]	字符列中的任何单一字符
[^charlist] 或者 [!charlist] 不在字符列中的任何单一字符
这种写法，mysql实际测试没有成功

  like "_i_a"
  like "%ter"

7.查询学过"张三"老师授课的同学的信息
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数

分层简化问题，先查询张三老师的教师编号，接着查询出课程编号，然后查询出选修了其中一门的学生编号 （思考，可以限定选修两门以上的学生），最后查询出学生信息

8、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



9、查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



10、查询没有学全所有课程的同学的信息
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数




11、查询至少有一门课与学号为"03"的同学所学相同的同学的信息
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 *

12、查询和"05"号的同学学习的课程完全相同的其他同学的信息
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



score表内容

s_id c_id s_score
01	01	80
01	02	90
01	03	99
01	04	67
02	01	70
02	02	60
02	03	80
02	04	98
03	01	80
03	02	80
03	03	80
04	01	50
04	02	30
04	03	20
04	04	40
05	01	76
05	02	87
06	01	31
06	03	34
07	02	89
07	03	98
08	01	89
08	02	98


05学生学习了01和02两门课程

加上c_id字段返回结果

(select s_id,c_id from score where c_id not in(select c_id from score where s_id = '05'))
1
语句查询的是该学生学习了05学习课程之外其他课程的学生信息。

在这里插入图片描述
not in 之后，剩余的学生只有两种情况:

学习了05全部课程
学习了05一部分课程
通过查询学习的课程数量，就能找到完全匹配的学生

13.查询没学过"张三"老师讲授的任一门课程的学生姓名
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

14、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



15、检索"01"课程分数小于60，按分数降序排列的学生信息(asc升序 desc降序)
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



16、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



17、查询各科成绩最高分、最低分和平均分：以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



18 查询学生的总成绩并进行排名
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */





19查询不同老师所教不同课程平均分从高到低显示
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



20、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

    



21 统计各科成绩各分数段人数：课程编号,课程名称,[100-85],[85-70],[70-60],[0-60]及所占百分比
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



    



22、查询学生平均成绩及其名次
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



23/查询各科成绩前三名的记录
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */




24 查询出只有两门课程的全部学生的学号和姓名
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



25、查询男生、女生人数
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */


26、查询同名同性学生名单，并统计同名人数
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



27 查询课程名称为"数学"，且分数低于60的学生姓名和分数
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



28 查询所有学生的课程及分数情况；
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



29、查询任何一门课程成绩在70分以上的姓名、课程名称和分数；
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



30 查询不及格的课程
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



31查询课程编号为01且课程成绩在80分以上的学生的学号和姓名；
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */


32 查询选修"张三"老师所授课程(可能有多个课程)的学生中，成绩最高的学生信息及其成绩
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



33查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



34查询每门课程成绩最好的前两名
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



35、统计每门课程的学生选修人数（超过5人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



36查询各学生的年龄
– 按照出生日期来算，当前月日 < 出生年月的月日则，年龄减一

/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



DATE_FORMAT() 函数用于以不同的格式显示日期/时间数据。

date 参数是合法的日期。format 规定日期/时间的输出格式。


DATE_FORMAT(NOW(),'%b %d %Y %h:%i %p')
DATE_FORMAT(NOW(),'%m-%d-%Y')
DATE_FORMAT(NOW(),'%d %b %y')
DATE_FORMAT(NOW(),'%d %b %Y %T:%f')

结果类似：

Dec 29 2008 11:45 PM
12-29-2008
29 Dec 08
29 Dec 2008 16:25:46.635

37 查询本月过生日的学生
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */



38、 查询本周过生日的学生
/**
–1.学生表
Student(s_id,s_name,s_birth,s_sex) –学生编号,学生姓名, 出生年月,学生性别
–2.课程表
Course(c_id,c_name,t_id) – –课程编号, 课程名称, 教师编号
–3.教师表
Teacher(t_id,t_name) –教师编号,教师姓名
–4.成绩表
Score(s_id,c_id,s_score) –学生编号,课程编号,分数
 */

