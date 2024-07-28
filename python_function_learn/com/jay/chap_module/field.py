# 作用域：在Python中，是通过
# _前缀来实现的

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
