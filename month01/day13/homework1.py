'''
内置可重写函数练习1
    (1). 创建父子类,添加实例变量
            创建父类:人(姓名,年龄)
            创建子类:学生(成绩)
    (2). 创建父子对象,直接打印.
            格式: 我是xx,今年xx.
                 我是xx,今年xx,成绩是xx.
    (3). 通过eval + __repr__拷贝对象,体会修改拷贝前的对象名称,不影响拷贝后的对象.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"我是{self.name},今年{self.age}."

    def __repr__(self) -> str:
        return f"Person('{self.name}',{self.age})"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self) -> str:
        # return f"我是{self.name},今年{self.age},成绩是{self.grade}."
        return super().__str__() + f",{self.grade}"

    def __repr__(self) -> str:
        return f"Student('{self.name}',{self.age},{self.grade})"


person1 = Person("大明", 35)
print(person1)
student1 = Student("小明", 10, 90)
print(student1)

person2 = eval(person1.__repr__())
person1.age = 37
print(person2.age)

student2 = eval(student1.__repr__())
student1.grade = 100
print(student2.grade)
