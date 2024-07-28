def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))
# 在计算机中，函数调用是通过
# 栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，
# 栈就会减一层栈帧,由于计算机中的栈不是无限的。所以，
# 递归调用的次数过多，会导致栈溢出
# print(fact(1000))

def fact_1(n):
    return fact_item(n,1)

def fact_item(num,product):
    if num==1:
        return product
    return fact_item(num-1,num*product)

# print(fact_item(1000,5))

# 请编写move(n, a, b, c)函数，它接收参数n，
# 表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法
# http://blog.csdn.net/hikobe8/article/details/50479669
def move(n,a,b,c):
    if (n==1):
        print(a,'--->',c)
        return
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)
print(move(3,'A','B','C'))


