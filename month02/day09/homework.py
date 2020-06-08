'''
将dict.txt中点单词存入到数据库
         创建一个数据库  dict
         创建数据表     words  字段： id   word   mean
         将单词本中单词插入到这个数据表
'''
import pymysql
import re
list_words = []
with open("dict.txt") as f:
    for line in f:
        content=line.split()
        word,mean = content[0],' '.join(content[1:])
        # print(word,mean)
        list_words.append((word, mean))
# print(list_words)
db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="135456..",
    database="dict",
    charset="utf8"
)

cur=db.cursor()
try:
    sql="insert into words (word,mean) values (%s,%s)"
    cur.executemany(sql,list_words)
    db.commit()
except:
    db.rollback()
finally:
    db.close()
    cur.close()
