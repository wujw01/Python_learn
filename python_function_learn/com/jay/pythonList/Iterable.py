from collections import Iterable
print("[]是否是一个Iterable对象："+str(isinstance([],Iterable)))
print("{}是否是一个Iterable对象："+str(isinstance({},Iterable)))
print("'abc'是否是一个Iterable对象："+str(isinstance('abc',Iterable)))
print("(x for x in range(10))是否是一个Iterable对象："+str(isinstance((x for x in range(10)),Iterable)))
print("100是否是一个Iterable对象："+str(isinstance(100,Iterable)))

from collections import Iterator
print("[]是否是一个Iterator对象："+str(isinstance([],Iterator)))
print("{}是否是一个Iterator对象："+str(isinstance({},Iterator)))
print("'abc'是否是一个Iterator对象："+str(isinstance('abc',Iterator)))
print("(x for x in range(10))是否是一个Iterator对象："+str(isinstance((x for x in range(10)),Iterator)))
print("100是否是一个Iterator对象："+str(isinstance(100,Iterator)))

# Iterator 对象表示的是一个数据流，Iterator 对象可以被
# next()函数调用并不断返回下一个数据，知道没有数据时抛出stopIteeration错误

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

for x in [1,2,3,4,5]:
    pass

# 等同于
it=iter([1,2,3,4])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
