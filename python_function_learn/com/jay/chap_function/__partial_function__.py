# 偏函数
int('12345')
print('八进制转化' + str(int('12345', 8)))

import functools

int2 = functools.partial(int, base=2)
# print(int2('10000'))
print('二进制转化：' + str(int2('10000')))

# 小结：当函数的参数个数太多，需要简化时，
# 使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时
# 更加简单