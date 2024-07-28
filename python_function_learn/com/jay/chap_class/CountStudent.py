class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1
print('0个实例',Student.count)
stu=Student('张三')
print('1个实例',Student.count)
stu2=Student('李四')
print('2个实例',Student.count)
