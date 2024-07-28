class Student(object):
    name = 'XIANG.WEI'

    def __init__(self):
        self.name = 'lisi'


s = Student()
print('s.name1', s.name)
print('Student.name1', Student.name)

s.name = 'Michael'
print('s.name2', s.name)
print('Student.name2', Student.name)
del s.name
print('del s.name',s.name)
