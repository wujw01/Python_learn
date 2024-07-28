import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"score": 88, "name": "Bob", "age": 20}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.score = score
        self.age = age


s = Student('Bob', 20, 88)
# 直接调用报错，因为不知道如何将Student实例
# 变为一个JSON的{}对象
# print(json.dumps(s))

print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"score": 88, "name": "Bob", "age": 20}'
print(json.loads(json_str, object_hook=dict2student))

