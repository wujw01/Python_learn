class Animal(object):
    def run(self):
        print('Animal is running')

def run_twice(animal):
        animal.run()
        animal.run()


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
print(dog.run())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')
print(run_twice(Tortoise()))


class Husky(Dog):
     pass


a = Animal()
d = Dog()
h = Husky()
print('isinstance(h,Husky)',isinstance(h,Husky))
print('isinstance(h,Dog)',isinstance(h,Dog))

# 小结
#
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
#
