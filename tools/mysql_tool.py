import pymysql


class MysqlTool:
    db = None
    cur = None

    @classmethod
    def connect_database(cls, database: str, host="localhost", port=3306, user="root", password="135456..",
                         charset="utf8"):
        cls.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset)
        cls.cur = cls.db.cursor()

    @classmethod
    def query_all(cls, table, show_one=False):
        sql = f"select * from {table}"
        cls.cur.execute(sql)
        return cls.cur.fetchall() if not show_one else cls.cur.fetchone()

    @classmethod
    def query_by(cls, table, where, value):
        sql = f"select * from {table} where {where}=%s"
        cls.cur.execute(sql, value)
        return cls.cur.fetchall()

    @classmethod
    def update(cls, table, feild, value1, where, value2):
        try:
            sql = f"update {table} set {feild}=%s where {where}=%s;"
            cls.cur.execute(sql, [value1, value2])
            cls.db.commit()
            return True
        except Exception as e:
            print(e.args)
            return False

    # 插入1条数据
    @classmethod
    def insert(cls, table, *args, **kwargs):
        try:
            feilds=str(tuple(kwargs.keys())).replace("'","")
            sql = f"insert into {table}{feilds} values {tuple(kwargs.values())}"
            # print(sql)
            cls.cur.execute(sql)
            cls.db.commit()
            return True
        except Exception as e:
            print(e.args)
            return False

    @classmethod
    def delete(cls, table, where, value):
        try:
            sql = f"delete from {table} where {where}=%s"
            cls.cur.execute(sql, value)
            cls.db.commit()
            return True
        except Exception as e:
            print(e.args)
            return False

    @classmethod
    def close(cls):
        cls.cur.close()
        cls.db.close()
