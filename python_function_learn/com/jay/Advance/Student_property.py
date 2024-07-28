class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100!')
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())


# s.set_score(111)
# print(s.get_score())


# 装饰器
class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


s = Student1()
s.score = 60
print(s.score)
s.score = 999
print(s.score)


# 只读属性
class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


class Screen(object):
    @property
    def width(self):
        return self.width

    @property.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        return self.height

    @property.setter
    def height(self, value):
        self.width = value
    @property
    def resolution(self):
        return self.resolution
    @property.setter
    def resolution(self,value):
        self.resolution=value

s=Screen()
s.width=1024