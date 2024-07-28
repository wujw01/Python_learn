def enroll(name,gender,age=6,city='上海'):
    print('name:',name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('sally','F')
enroll('xiang.wei','M',9)


# 默认参数必须指向一个不变的对象
def add_end(L=[]):
    L.append('End')
    return L

print(add_end([1,2,3]))
print(add_end(['x','y','Z']))

print(add_end())
print(add_end())

def add_end_2(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L
print(add_end_2())
print(add_end_2())




