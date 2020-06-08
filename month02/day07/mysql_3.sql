练习1：使用book表完成
1. 统计每位作家图书的平均价格
   select author,avg(price) from book group by author;

2. 统计每个出版社出版图书的数量
   select publication,count(title) from book group by publication;

3. 查看总共 有多少出版社
select count(distinct publication) from book;

4. 筛选出那些 出版过超过50元的图书的出版社，并按照其出版图书的平均价格
  按照降序排序

  # 求50元以上图书的平均价格
  select publication,avg(price) from book
  where price > 50
  group by publication
  order by avg(price) desc;

  # 所有图书的平均价格
  select publication,avg(price) from book
  group by publication
  having max(price) >= 50
  order by avg(price) desc;

5. 统计相同时间出版的图书的平均价格
   select publication_date,avg(price) from book
   group by publication_date;

--级联动作
alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete cascade on update cascade;

alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete set null on update set null;