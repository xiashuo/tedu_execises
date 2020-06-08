-- 创建一个数据库 books 使用utf8编码
create database books charset=utf8;

-- 在数据库中创建数据表 book  字段有
-- id  书名  作者  出版社  价格   备注
-- 数据类型和约束自己拟定
use books;

create table book(
id int primary key auto_increment,
title varchar(50) not null,
author varchar(30) not null,
publication varchar(50),
price float,
comment text
);


-- 向数据库中插入若干数据 （>8条）
-- 作者 ： 老舍  鲁迅  冰心  。。。。
-- 价格 ： 30 -- 120
-- 出版社： 中国文学  人民教育  机械工业
insert into book (title,author,publication,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into book (title,author,publication,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("巨人传","忘了","人名教育出版社",47);

--练习1 ：　使用ｂｏｏｋ
--1. 查找30多元的图书
select * from book where price >= 30  and price < 40;

--２．查找人民教育出版社出版的图书　
select * from book where publication = "人民教育出版社";

--３．查找老舍写的，中国文学出版社出版的图书　
select * from book where author ="老舍" and publication ="中国文学出版社";

--４．查找备注不为空的图书
select * from book where comment is not null;

--５．查找价格超过６０元的图书，只看书名和价格
select title,price from book where price > 60;

--６．查找鲁迅写的或者茅盾写的图书
select * from book where author ="鲁迅" or author ="茅盾";
select * from book where author in ("鲁迅","茅盾");


--练习2： 使用book表
--1. 将呐喊的价格改为45
update book set price = 45 where title="呐喊";
--2. 修改所有老舍的作品，价格增加5元
update book set price = price+5 where author="老舍";
--3. 修改价格字段的数据类型为 decimal(5,2)
alter table book modify price decimal(5,2);
--4. 增加一个字段，字段名称为  出版日期  类型为 date 放在 price后面
alter table book add publication_date date after price;
--5. 删除所有价格超过65元的图书
delete from book where price > 65;

--练习3：
--1. 将所有老舍的作品出版时间给为 2016-10-1
update book set publication_date="2016-10-1" where author="老舍";

--2. 修改所有中国文学出版社出版的图书出版时间为 2018-10-1，但是不要改老舍的
update book set publication_date="2018-10-1"
where publication="中国文学出版社" and author != "老舍";

--3. 所有出版时间为 null 的图书 将出版时间设置为2020-1-1
update book set publication_date="2020-1-1" where publication_date is null;


练习4 ：

在stu 创建 数据表 三国
id   name   gender  country   attack   defense

create table sanguo(
id int primary key auto_increment,
name varchar(30),
gender enum('男','女'),
country enum('魏','蜀','吴'),
attack smallint,
defense tinyint
);


insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);

1. 查找所有蜀国人的信息，按照攻击力排名
select * from sanguo where country="蜀" order by attack desc;

2. 将赵云的攻击力设置为360 防御力设置为 70
update sanguo set attack=360,defense=70 where name="赵云";

3. 吴国英雄攻击力超过300的改为300 最多修改2个
update sanguo set attack=300 where country="吴" and attack > 300 limit 2;

4. 查找攻击力超过200的魏国英雄名字和攻击力，并且显示为 姓名  攻击力
select name as 姓名,attack as 攻击力
from sanguo where country="魏" and attack > 200;

5. 所有英雄攻击力按照降序排序，如果攻击力相同则按照防御力降序排序
select * from sanguo order by attack desc,defense desc;

6. 查找名字为3个字的英雄
select * from sanguo where name like "___";

7. 查找比魏国最高攻击力的英雄攻击力还高的蜀国英雄
select * from sanguo
where country="蜀" and
attack>(select attack
from sanguo
where country="魏"
order by attack
desc limit 1);

8. 找到魏国防御力排名 前2的英雄
select * from sanguo where country ="魏" order by defense desc limit 2;

9. 查到所有女性角色同时查找所有男性角色中攻击力少于250的
select * from sanguo where gender='女' union
select * from sanguo where gender="男" and attack < 250;











