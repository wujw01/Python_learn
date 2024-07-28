def power(x):
    return x*x;

print(power(5));

def power_n(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s;
print(power_n(5,4))
# print(power_n(5))

# 设置默认参数
def power_n2(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power_n2(5))
print(power_n2(5,6))


