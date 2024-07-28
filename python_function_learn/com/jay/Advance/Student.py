class Student(object):
    pass


def set_age(self, age):
    self.age = age


s = Student()
from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(100)
print(s.age)
# s2 = Student()
# s2.set_age(90)


# __slots__ 只允许对Student实例添加
# name和age属性

class Student2(object):

    __slots__ = ('name', 'age')
s=Student2()
s.name='Xiang.wei'
s.age=25
s.score=11
