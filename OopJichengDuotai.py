#OOP3
# 多继承例子
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("I am swimming")
class Bird():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print("I am flying")

class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print("Working........")

# 多继承例子
class SuperMan(Person,Bird,Fish):
    pass
s = SuperMan("yueyue")
s.fly()
s.swim()


# 单继承例子
class Student(Person):
    def __init__(self, name):
        self.name = name
stu = Student("yueyue")
stu.work()

#### 菱形继承问题
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass


# 构造函数
class Person():
    # 对Person 类进行实例化的时候
    #姓名要确定
    # 年龄要确定
    #地址肯定要有
    def __init__(self):
        self.name = "NoName"
        self.age = 18
        self.address = "adslkadj"

# 实例化一个人
p = Person()
# 构造函数的调用顺序
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class E():
    def __init__(self):
        print("E")
class F(E):
    def __init__(self):
        print("B")

class C(F):
    pass

#此时，首先查找C的构造函数
# 如果 没有就按着MRO 顺序查找父类的构造函数，找到为止

c = C()


# 构造函数顺序调用-3
class G():
    def __init__(self):
        print("G")

class H(G):
    def __init__(self, name):
        print("H")
        print(name)

class I(H):
    # I 中想扩展H的构造函数
    # 既调用H 的构造函数后再添加一些功能
    # 由两种方法实现
    #第一种是通过父类名调用

# 以下三种实现方式 注意子函数的传参
   def __init__(self,name):
       super().__init__(name)
       print("我是I中的附加功能")

'''
    def __init__(self,name):
        H.__init__(self,name)
        print("这是I中的附加功能")
'''



'''
    def __init__(self):
        super(H,H.__init__(self,name=0))
        print("我是I中的你")
'''
# 此时，首先查找I的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
# 此时，会出现参数结构不对应错误
i = I("我是我")