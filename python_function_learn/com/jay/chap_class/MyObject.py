class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


myObj = MyObject()
print('hasattr-x', hasattr(myObj, 'x'))
print('hasattr-y', hasattr(myObj, 'y'))
print('obj.x', myObj.x)


