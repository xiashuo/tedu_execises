import pymysql

db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="135456..",
    database="stu",
    charset="utf8"
)

cur=db.cursor()
# name=input("name:")
# sql="select name,score from cls where name=%s;"
# cur.execute(sql,name)
# print(cur.fetchone())
try:
    sql="update cls set name=%s where id =%s;"
    cur.executemany(sql,[('张三',6),('李四',7),('王五',8),
                         ('赵六',9),('孙七',10)])
    db.commit()
    cur.execute("select * from cls;")
    print(cur.fetchall())
except:
    db.rollback()

finally:
    cur.close()
    db.close()
