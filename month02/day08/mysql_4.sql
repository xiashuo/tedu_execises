--朋友圈练习
--用户表
create table user(
id int primary key auto_increment,
name varchar(32),
passwd char(64)
);

--朋友圈
create table pyq(
id int primary key auto_increment,
image blob,
content text,
time datetime,
u_id int,
constraint u_fk foreign key (u_id) references user(id)
);

--点赞评论
create table user_pyq(
id int primary key auto_increment,
uid int,
pid int,
lk bit default 0,
comment text default null,
constraint ufk foreign key (uid) references user(id),
constraint pfk foreign key (pid) references pyq(id)
);


练习1： 使用cls和hobby表完成
1. 学生对应的兴趣爱好和兴趣班价格
select cls.name,hobby.hobby,hobby.price
from cls inner join hobby on cls.name=hobby.name;

2. 查询所有学生信息，同时标注学生兴趣爱好是什么，没有兴趣的写Null
select cls.name,cls.sex,hobby.hobby
from cls left join hobby
on cls.name=hobby.name;

进阶练习 2: books数据库

create table class(cid int primary key auto_increment,
                  caption char(4) not null);

create table teacher(tid int primary key auto_increment,
                    tname varchar(32) not null);

create table student(sid int primary key auto_increment,
                    sname varchar(32) not null,
                    gender enum('male','female','others') not null default 'male',
                    class_id int,
                    foreign key(class_id) references class(cid)
                    on update cascade
                    on delete cascade);

create table course(cid int primary key auto_increment,
                   cname varchar(16) not null,
                   teacher_id int,
                   foreign key(teacher_id) references teacher(tid)
                   on update cascade
                   on delete cascade);

create table score(sid int primary key auto_increment,
                  student_id int,
                  course_id int,
                  number int(3) not null,
                  foreign key(student_id) references student(sid)
                   on update cascade
                   on delete cascade,
                   foreign key(course_id) references course(cid)
                   on update cascade
                   on delete cascade);

insert into class(caption) values('三年一班'),('三年二班'),('三年三班');
insert into teacher(tname) values('波多老师'),('苍老师'),('小泽老师');
insert into student(sname,gender,class_id) values('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3);
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66);

1. 查询每位老师教授的课程数量
select teacher.tname,count(course.teacher_id)
from teacher left join course on teacher.tid=course.teacher_id
group by teacher.tname;

2. 查询学生的信息及学生所在班级信息
select caption,sname,gender
from student left join class on class.cid = student.class_id;

3. 查询各科成绩最高和最低的分数,形式 : 课程ID 课程名称 最高分  最低分
select cid,cname,max(number),min(number)
from course left join score on course.cid=score.course_id
group by cid,cname;

4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid,sname,avg(number)
from student left join score on student.sid=score.student_id
group by student.sid,sname
having avg(number) >85;

5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student.sid,student.sname
from student left join score on student.sid=score.student_id
where score.course_id = 2 and number > 80;

6. 查询各个课程及相应的选修人数
select course.cname,count(*)
from course left join score on course.cid = score.course_id
group by course.cname;

函数
create function st1() returns int
begin
update cls set score=99 where id=1;
delete from cls where score < 60;
return (select age from cls where id=1);
end $$

create function st2() returns int
begin
declare a int;
declare b int;
set a=(select score from cls order by score desc limit 1);
select score from cls order by score limit 1 into b;
return a+b;
end $$

create function st3(uid int) returns varchar(30)
begin
return (select name from cls where id=uid);
end $$

--存储过程
create procedure p_in ( in num int )
begin
    select num;
    set num=100;
    select num;
end $$

set @a=10;
call p_in(@a)

create procedure p_out (out num int )
begin
    select num;
    set num=100;
    select num;
end $$

set @a=10;
call p_out(@a)


练习3 使用cls表：
  1. 写一个函数，传入两个学生的ID，得到这连个学生分数只差

  create function score(uid1 int,uid2 int)
  returns float
  begin
  declare a float;
  declare b float;
  select score from cls where id=uid1 into a;
  select score from cls where id=uid2 into b;
  return a-b;
  end $$


  2. 写一个存储过程，传入一个学生的姓名，通过外部的变量得到该学生的成绩
  create procedure get_score(inout uname varchar(30))
  begin
  set uname=(select score from cls where name=uname);
  end $$

  set @score="Lily"
  call get_score(@score)

作业 ：　１．　语句内容总结分类　　－－－　思维导图　
　　　　　２．将　ｂｏｏｋ 表拆分
            书籍信息表
            出版社信息表
            作家信息表
           设计表关系并完成E-R模型图，根据模型图 创建这一组表结构
