-- 创建数据库books
create database books character set utf8;

-- 创建表book
create table book(
id int primary key auto_increment,
bookname varchar(64) not null ,
author varchar(32) not null ,
publisher varchar(64) ,
price float default 0,
remarks varchar(64)
);

-- 插入数据
insert into book(bookname, author, price) values
('《狂人日记》','鲁迅',38),
('《朝花夕拾》','鲁迅',18),
('《阿Q正传》','鲁迅',8),
('《茶馆》','老舍',17),
('《四世同堂》','鲁迅',55),
('《射雕英雄传》','金庸',18),
('《神雕侠侣》','金庸',22),
('《倚天屠龙记》','金庸',20);
