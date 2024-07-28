def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

print(calc_sum(1,2,3,6,7,10))

# 高阶函数除了可以接受函数作为参数外，
# 还可以把函数作为结果值返回。
def lay_sum(*args):
    def sum():
        ax=0
        for n in  args:
            ax=ax+n
        return ax
    return sum
f=lay_sum(1,3,5,7,9)
print(f())
