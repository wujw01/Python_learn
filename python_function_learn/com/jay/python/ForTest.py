import heapq
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
# 如何判断一个对象是可迭代对象
# 呢？方法是通过collections模块
# 的Iterable类型判断：
from collections import Iterable
print(isinstance('abc',Iterable))  #str是否可迭代
print(isinstance([1,2,3],Iterable)) #list是否可迭代
print(isinstance(123,Iterable)) #整数是否可迭代

for i,value in enumerate(['A','B','C']):
    print(i,value)

def findMinAndMax (l):
     l.sort()
     return (l[0],l[-1])

print(findMinAndMax([3,2,4,1,5,8,7]))

def findMinAndMax_1(list):
    nlargestList=heapq.nlargest(1, list)
    nsmallestList=heapq.nsmallest(1, list)
    return (nsmallestList,nlargestList)
print(findMinAndMax_1([3,2,4,1,5,8,7]))



