class Student(object):
    def __init__(self, name, gender):
        """
         相当于Java中的构造器
        """
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


bart = Student('Bart Simpson', 'male')
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功！')


# 实际上__name变量已经被Python解释器自动改成
# _Student_name,而外部代码给bart新增了一个
# __name变量
