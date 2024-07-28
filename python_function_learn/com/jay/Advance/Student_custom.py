class Student_custom(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name: %s)' % self.name


print(Student_custom('Michael'))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    def __iter__(self):
        return self  # 实例本身就是迭代

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
# for n in Fib():
#     print(n)
#
# class Fib1(object):
#     def __init__(self):
#         self.a = 0,
#         self.b = 1,
#         self.i = 0
#
#     def printFib(self, number):
#         while self.i < number:
#             print self.a
#             self.a, self.b = self.a, self.a + self.b
#             self.i = self.i + 1
#
#
# fib = Fib1()
# for n in fib.printFib(1000):
#     print(n)
