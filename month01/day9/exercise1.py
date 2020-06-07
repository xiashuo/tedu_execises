'''
调用下列函数
    def func01(*args,**kwargs):
        print(args)
        print(kwargs)

    def func02(p1, p2, *args, p3, p4=4):
        print(p1)
        print(p2)
        print(args)
        print(p3)
        print(p4)
'''


def func01(*args, **kwargs):
    print(args)
    print(kwargs)


def func02(p1, p2, *args, p3, p4=4):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(p4)


a = (1, 2, 3)
b = {"a": 1, "b": 2, "c": 3}
func01(*a, **b)
func01(1, 2, 3, a=1, b=2, c=3)

func02(1,2,3,4,5,p3=6)
a=[3,4,5]
func02(1,2,*a,p3=6)
