create table `hobby` (
`id` int primary key auto_increment,
`name` varchar(30) not null,
`set` set("sing","dance","draw"),
`level` char(2),
`price` decimal(7,2),
`remark` text
);

--插入操作
insert into class_1 values
(1,"Lily",18,'w',92),
(2,"Tom",18,'m',77);

insert into class_1 (name,age,sex,score)
values
("Lucy",18,'w',87);

insert into class_1 (name,age,score)
values ("Emma",17,83);

insert into class_1 (name,age,sex)
values ("Joy",17,'m');

insert into hobby (name,hobby,level,price,remark) values
("Lily",'dance',"B+",16800.00,"练舞奇才");

insert into hobby (name,hobby,level,price,remark) values
("Joy",'sing,dance',"A+",16800.00,"骨骼惊奇，练舞奇才");





