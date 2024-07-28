print(type(213))
print(type('str'))
print(type(None))

print('type(123)==type(456)', type(123) == type(456))

import types


def fn():
    pass


print('type(fn)==type.FunctionType', type(fn) == types.FunctionType)

print('dir(\'abc\')', dir('Abc'))


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

