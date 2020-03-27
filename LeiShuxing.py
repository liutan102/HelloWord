# 属性案例
# 创建Student 类 描述学生类
# 学生具有Student.name属性
# 但name 格式并不统一
# 可以用增加一个函数，然后自动调用的方式但很蠢

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)
    # 介绍一下自己
    def intro(self):
        print(("Hi my name is {0}".format(self.name)))
    def setName(self,name):
        self.name = name.upper()



s1 = Student("Liu Tan",10)
s2 = Student("michi stangle",17)
s1.intro()
s2.intro()

# peroperty案例
# 定义一个Person 类 具有name age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄 我们希望内部统一用整数保存
# x = peroperty（fge,fset,fdel,doc）
class Person():
    # 函数的名称可以任意
    '''
    这是一个说明文档 可以用 __doc__ 打印出来

    '''
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget,fset,fdel,"对name进行以下操作")

p1 = Person()
p1.name = "assss"
print(p1.name)

class Studen():

    def fget(self):
        return self.age

    def fset(self,age):
        self.age = age

    def fdel(self):
        self.age = 1

    name = property(fget,fset,fdel,"对age进行赋值")

pp = Studen()
pp.age = ("%.0f"%1.5)
print(pp.age)
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)

# init 举例
class A():
    def __init__(self,name = 0,age = 1):
        print("haha 我被调用了")
a = A()

# __call__举例
class A1():
    def __init__(self,name = 0,age = 1):
        print("haha 我被调用了2")
    def __call__(self, *args, **kwargs):
        print("enheng")
a = A1()
a()

# str 函数
class A3():
    def __init__(self,name = 0,age = 1):
        print("haha 我被调用了3")

    def __str__(self):
        return "哎呀 讨厌！"
a1 = A3()
print(a1)

# repr 函数

class B():
    def __init__(self,name = 0,age = 1):
        print("haha 我被调用了4")

    def __repr__(self):
        return "哎呀 讨厌！1"
b = B()
print(b)

