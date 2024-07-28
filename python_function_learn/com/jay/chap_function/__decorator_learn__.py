import time

# t = time.time()
# begin = int(round(t * 1000))
def metric(fn):
    def wrapper(*args,**kwargs):
        begin=int(round(time.time()*1000))
        rs=fn(*args,**kwargs)
        print('%s executed in %s ms' % (fn.__name__, int(round(time.time()*1000))-begin))
        return rs
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
f=fast(11,22)

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z
s=slow(11,22,33)

if f!=33:
    print("测试失败")
elif s!=7986:
    print("测试失败！")




