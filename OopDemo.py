# 关于delf 案例
class A():

    name = "liuheizi"
    age = 18
    def __init__(self):
        self.name = "aaa"
        self.age = 10

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = "baibai"
    age = 9

a = A()
# 此时 系统会默认 把 a当做 第一个参数传入 函数中

a.say()

#此时 ，self被a替换
A.say(a)
# 同样也可以被A替换
A.say(A)
# 此时传入的是实例B 因为B 具有name和age属性，所以不会报错
# 利用鸭子模型
A.say(B)


class Person():
    # name 是共有的成员
    name = "dana"
    # __age 就是私有的成员（前边加上两个下划线即可）
    __age = 12

p = Person()
# name 是共有变量
print(p.name)
# __age是私有变量
# 注意报错信息
#print(p.__age)
# name mangling技术
print(Person.__dict__)
p._Person__age = 19
print(p._Person__age)