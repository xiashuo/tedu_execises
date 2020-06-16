
--创建数据库
CREATE DATABASE employee_info_system character set utf8;
use employee_info_system;
-- 1. 创建表

-- 部门表
CREATE TABLE dept (
  d_id int(11) PRIMARY KEY AUTO_INCREMENT,
  d_name varchar(32) NOT NULL
) ;

-- 员工表
CREATE TABLE employee (
  e_id int(11) PRIMARY KEY AUTO_INCREMENT,
  cn_name varchar(32) NOT NULL,
  id_card varchar(32) NOT NULL,
  en_name varchar(32) ,
  salary int(11) NOT NULL,
  dimission bit DEFAULT 0,
  UNIQUE index en_name_unique (en_name)
);

-- 部门-员工表
CREATE TABLE emp_dept (
  ed_id int(11) PRIMARY KEY AUTO_INCREMENT,
  e_id int(11) NOT NULL,
  d_id int(11) NOT NULL,
  CONSTRAINT did_id FOREIGN KEY (d_id) REFERENCES dept (d_id),
  CONSTRAINT eid_id FOREIGN KEY (e_id) REFERENCES employee (e_id)
);

-- 向表中插入数据
INSERT into dept VALUES
(1,'研发部'),
(2,'营销部'),
(3,'行政部'),
(4,'财务部');

INSERT into employee VALUES
(1,'张三','42100219940714291X','boll',12000,0),
(2,'李四','42100219930714291X','lisi',12000,0),
(3,'王五','42100219920714291X','wangwu',12000,0),
(4,'赵柳','42100219910714291X','zhaoliu',12000,0),
(5,'孙起','42100219940714292X','suanqi',12000,0),
(6,'王八','42100219940714293X','wangba',12000,0),
(7,'周久','42100219940714294X','zhoujiu',12000,0),
(8,'钱十','42100219940714295X','qianshi',12000,0),
(9,'吴天','42100219940714261X','wutian',12000,0),
(10,'郑板','42100219940714271X','zhengban',12000,0);

INSERT into emp_dept VALUES
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,2),
(6,6,3),
(7,7,1),
(8,8,4),
(9,9,1),
(10,10,2),
(11,1,2),
(12,3,4),
(13,6,3),
(14,9,1);

-- 2.查询每个部门工资最高的员工姓名和工资
SELECT a.d_name 部门,a.cn_name 工资最高员工,a.salary 工资
FROM (
	SELECT dept.d_name,employee.cn_name,employee.salary 
	FROM employee,dept,emp_dept 
	WHERE employee.e_id=emp_dept.e_id and emp_dept.d_id=dept.d_id
) as a
WHERE (
	SELECT COUNT(*) 
	FROM (
		SELECT dept.d_name,employee.cn_name,employee.salary 
		FROM employee,dept,emp_dept 
		WHERE employee.e_id=emp_dept.e_id and emp_dept.d_id=dept.d_id
	) as b 
	WHERE a.d_name=b.d_name and a.salary<b.salary
)=0;

-- 3.查询某个是身份证号的员工是否离职
SELECT employee.cn_name 姓名,employee.id_card 身份证,dept.d_name 部门,employee.dimission 是否离职 from employee,dept,emp_dept WHERE employee.e_id=emp_dept.e_id and dept.d_id=emp_dept.d_id and employee.id_card='42100219940714291X'; 
SELECT employee.cn_name 姓名,employee.id_card 身份证,dept.d_name 部门,employee.dimission 是否离职 from employee,dept,emp_dept WHERE employee.e_id=emp_dept.e_id and dept.d_id=emp_dept.d_id and employee.id_card='42100219930714291X'; 
SELECT employee.cn_name 姓名,employee.id_card 身份证,dept.d_name 部门,employee.dimission 是否离职 from employee,dept,emp_dept WHERE employee.e_id=emp_dept.e_id and dept.d_id=emp_dept.d_id and employee.id_card='42100219940714293X'; 

-- 4.查询英文名以e结尾的员工，是否会使用数据库索引，为什么？
-- 答：会。因为英文名字段是唯一的，即加了unique唯一约束，和主键约束的创建一样，都需要依靠索引，如果在创建主键或唯一约束的时候没有已经建好的索引可以使用的话，数据库会自动建立一个唯一的索引。
