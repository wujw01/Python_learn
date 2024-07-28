class Student(object):
    def __init__(self, name, score):
        """
         相当于Java中的构造器
        """
        self.__name = name
        self.__score = score

    def print_score(self):
        """
        打印学生的成绩
        :param std:  学生实体
        :return:
        """
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad scoreßßßßßßß')


bart = Student('Bart Simpson', 59)
print(bart.print_score())
print(bart.get_grade())


bart.__name='New Name'
print(bart.__name)
print(bart.get_name())

# 实际上__name变量已经被Python解释器自动改成
# _Student_name,而外部代码给bart新增了一个
# __name变量


