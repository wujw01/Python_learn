L=['Xiang','Li','Wang','Bob','Liu']
r=[]
n=3
for i in range(n):
    r.append(L[i])
print(r)

# 切片方式
# 取出前三个，但是不包括索引3
print(L[0:3])
print(L[1:3])
print(L[-1])

L=list(range(100))
print(L)

print(L[:10])
print(L[:])
# tuple也是一种list，唯一
# 的区别是tuple不可变
print((0,1,2,3,4,5)[:3])