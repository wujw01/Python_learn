L=[x*x for x in range(10)]
print(L)

# g=(x*x for x in range(10))
# for n in g:
#     print(n)

# 赋值语句 a,b=b,a+b 相当于
# t=(b,a+b) t是一个tuple
# a=t[0]
# b=t[1]

def fib(max):
    n,a,b=0,1,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
o=odd()
print(next(o))
print(next(o))
print(next(o))


def fibGen(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1;
    return 'done'

for n in  fibGen(6):
    print(n)

g=fibGen(6)
while True:
    try:
        x=next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break






