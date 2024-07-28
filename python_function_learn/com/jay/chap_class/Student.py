class Student(object):
    def __init__(self, name, score):
        """
         相当于Java中的构造器
        """
        self.name = name
        self.score = score

    def print_score(self):
        """
        打印学生的成绩
        :param std:  学生实体
        :return:
        """
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# bart = Student()
# print(bart)

bart = Student('Bart Simpson', 59)
print(bart.name)

print(bart.print_score())
print(bart.get_grade())

print('bart-name', hasattr(bart, 'name'))
print('hasattr-score', hasattr(bart, 'score'))


# 小结：类是创建实例的模板，而实例则是一个一个
# 具体的对象，各个实例拥有的数据都互相独立，互不影响
# 方法就是与实例绑定的函数，和普通函数不同，方法
# 可以直接访问实例的数据
# 通过在实例上调用方法，我们就直接操作了对象内部的数据
# 但无需知道方法内部的实现细节
