def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n;
    return sum


print(calc([1, 2, 3]));
print(calc([1, 3, 5, 7]));


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))

# *nums 表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Michael', 30))
print(person('Bob', 35, city='BeiJing'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))


# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack',24,city='BeiJing',addr='Chaoyang',zipcode=123456)
