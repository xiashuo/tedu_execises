class StudentModel:
    """
        学生模型:封装数据
    """

    def __init__(self, name="", sex="男", age=0, score=0, sid=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
        self.sid = sid  # 对信息的唯一标识

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if value=='男' or value=='女':
            self.__sex=value
        else:
            raise Exception("性别输入错误，请重新输入！","输入‘男’或者‘女’")
