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

# __getattr__
class C():
    name = "NoName"
    age = 19

    def __getattr__(self,item):
   
        print("没找到啊")
        print("*****")
        print(item)


x = C()
#print(x.name)
print(x.addr)

class M():
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        print("设置属性：{0}".format(key))
        print("设置属性：{0}".format(value))
        # 下面语句会导致死循环
        #self.key = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super(M,self).__setattr__(key , value)

m = M()
m.age = 18


# __gt__
class Students():

    def __init__(self,name):
        self.name = name
    # 对他进行 字符转义
    def __str__(self):
        return self.name
    # 进行 大小判断
    def __gt__(self, other):
        print("哈哈 {0}会比{1}大吗".format(self,other))
        return self.name > other.name

stu1 = Students("one")
stu2 = Students("two")
print(stu1 > stu2)

# 三种方法案例
class Persons():
    # 实例方法
    def eat(self):
        print(self)
        print("EWass....")
    # 类方法
    # 类方法的第一个参数，一般命名cls区别于 self
    @classmethod
    def play(cls):
        print(cls)
        print("playing....")

    # 静态方法
    #  没有参数
    @staticmethod
    def say():
        print("say....")

yue = Persons()
yue.eat()

def word():
    pass

class word1():
    def __init__(self):
        self.name = "haha"
        self.age = 19
    # 此功能是对类变量进行读取操作的时候应该执行此函数功能
    def fget(self):
        print("我被调用了。。")
        #self.name = name
        return self.name

    # 模拟的是对变量进行写入操作的时候执行此功能
    def fset(self,name):
        print("我被写入了")
        print("图灵学院：" + name)
    # fdel模拟的是删除变量的时候进行的操作
    def fdel(self):
        print("我被删除了")
    # property函数的四个位置是固定的
    # 第一个参数代表读取的时候需要调用的函数
    # 第二个 参数代表写入的时候需要调用的函数
    # 第三个是删除函数
    name2 = property(fget , fset ,fdel, "我是一个doc")

a = word1()
print(a.name)
a.fset("aaa")
print(a.name2)
a.name2 = "hjashashas"
del a.name2


# 抽象类的实现
import abc
class Human(metaclass=abc.ABCMeta):

    #定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractmethod
    def drink(self):
        pass
    # 定义静态抽象方法
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        print("Sleep.......")


## 函数名可以当变量使用
def sayHellp(name):
    print("{0}你好,来来来，嘿嘿".format(name))

sayHellp("月月")
b = sayHellp
b("heihei")

#自己组装一个类
# 需要 import 包
from types import MethodType
class Z():
    pass
def hei(self):
    print("你猜我是谁呀！！！")

l = Z()
l.hei = MethodType(hei,Z)
l.hei()

# 利用type造一个类
# 先定义类应该具有的成员函数
def say1(self):
    print("哈嘿！")
def say2(self):
    print("嘿哈！")

# 用type来创建一个类
O = type("AName",(object,),{"class_say1":say1,"class_say2":say2})
o = O()
o.class_say1()

# 元类演示
# 元类写法是固定的，他必须继承与type
# 元类一般以 MetaClass结尾
class YuanyuanMetaClass(type):
    #注意一下写法
    def __new__(cls,name,bases,attrs):
        # 自己的业务处理
        print("我是元类！！")
        attrs['id'] = '00000'
        attrs['addr'] = '丰台三环新城'
        return type.__new__(cls,name,bases,attrs)


class Teacher(object,metaclass= YuanyuanMetaClass):
    pass
n = Teacher()
print(n.addr)



