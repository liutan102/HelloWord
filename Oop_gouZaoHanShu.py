# 构造函数的概念

class Dog0():
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")
# 实例化的时候，括号内的参数需要跟构造函数参数匹配
kaka = Dog0()

# 继承中的构造函数---1

class Animel():
    pass
class PaxingAni(Animel):
    pass
class Dog(PaxingAni):
    def __init__(self):
        print("I am init in dog ")
# 实例化 的时候 自动调用了Dog中构造函数
xiaobai = Dog()


# 继承中的构造函数---2

class Animel2():
    pass
class PaxingAni2(Animel2):
    def __init__(self):
        print("Paxing DongWu")
class Dog2(PaxingAni2):
    # __init__ 就是构造函数
    # 每次实例化的时候第一个被自动调用
    # 因为主要工作是进行格式化，而得名
    def __init__(self):
        print("I am init in dog ")
# 实例化 的时候 自动调用了Dog中构造函数、
# 因为找到了构造函数，则不再查找父类的构造函数
xiaobai2 = Dog2()
# 猫没有写构造函数
class Cat2(PaxingAni2):
    pass
# c此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# 在PaxingAni 中查找到了构造函数，则停止向上查找
c2 = Cat2()


# 继承中的构造函数---3

class Animel3():
    pass
class PaxingAni3(Animel3 ):
    def __init__(self,name):
        print("Paxing111 {0}".format(name))
class Dog3(PaxingAni3):
    # __init__ 就是构造函数
    # 每次实例化的时候第一个被自动调用
    # 因为主要工作是进行格式化，而得名
    def __init__(self):
        print("I am init in dog ")
# 实例化 的时候 自动调用了Dog中构造函数、
# 因为找到了构造函数，则不再查找父类的构造函数
xiaobai3 = Dog3()
# 猫没有写构造函数
class Cat3(PaxingAni3):
    pass
# 在PaxingAni 中查找到了构造函数，则停止向上查找
# 因为PaxingAni的构造函数需要两个参数，实例化的时候给了一个，报错
Dongwu = "Dongwu"
c3 = Cat3(Dongwu)


# 继承中的构造函数---4

class Animel4():
    def __init__(self):
        print("Animel")
class PaxingAni4(Animel4 ):
        pass
class Dog4(PaxingAni4):

    pass

xiaobai4 = Dog4()
# 猫没有写构造函数
class Cat4(PaxingAni4):
    pass
# 在PaxingAni 中查找到了构造函数，则停止向上查找
# 因为PaxingAni的构造函数需要两个参数，实例化的时候给了一个，报错

c4 = Cat4()
