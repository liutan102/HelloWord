
#coding=utf-8
class A:
    def __init__(self):
        self.__foo = 'foo'
        self._bar = 'bar'
a = A()
print(a.__dict__)
print(a._bar)
print(a.__foo) #这句会报错
