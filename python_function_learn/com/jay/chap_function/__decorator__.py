import functools
def now():
    print('2017-12-03')


f = now
print(f())


# 装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2017-12-03')


print(now())
print('now函数的函数名发生了变化：' + now.__name__)


# 原理：把@log 放在now()函数定义处，相当于
# 执行了语句：now=log(now)
# 由于log()是一个decorator，返回一个函数，所以，
# 原来的now()函数依然存在，只是现在被同名的now
# 变量指向了新的函数，于是调用now()将执行新函数，即在
# log()函数中返回的wrapper()函数


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2017-3-25')


print(now())
print('now函数的函数名发生了变化：' + now.__name__)

# 三层嵌套原理：首先执行 log('execute'),返回的是
# decorator函数，再调用返回的函数，参数是now函数，返回值最终
# 是wrapper函数


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2017-12-03')


print(now())
print('now函数的函数名没有发生变化：' + now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator
