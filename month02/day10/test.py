def test(*args, **kwargs):
    s=str(tuple(kwargs.keys()))
    s=s.replace("'","")
    print(s)
    sql=f"insert into cls "
    print(sql)

test(id=1,name="xiahsuo",score=99)
