# Python 学习
# 汉诺塔
a = "1"
b = "2"
c = "3"
def hannuo(a,b,c,n):
    if n == 1:
        print("{} @@@> {}".format(a,c))
        return None
    if n == 2:
        print("{} @@@> {}".format(a,b))
        print("{} @@@> {}".format(a,c))
        print("{} @@@> {}".format(b,c))
        return None
    hannuo(a,c,b,n-1)
    print("{} @@@> {}".format(a,c))
    hannuo(b,a,c,n-1)
hannuo(a,b,c,5)

hannuo(a,b,c,3)
hannuo(a,b,c,1)
hannuo(a,b,c,3)
hannuo(a,b,c,1)

def hannuo1(a,b,c,n):
    if n == 1:
        print("{} @@@> {}".format(a,c))
        return None
    if n == 2:
        print("{} @@@> {}".format(a,b))
        print("{} @@@> {}".format(a,c))
        print("{} @@@> {}".format(b,c))
        return None
    hannuo1(a,c,b,n-1)
    print("{} @@@> {}".format(a,c))
    hannuo(b,a,c,n-1)

'''
定义一个学生类 用来形容学生

'''

# 定义一个空的类
class Student():
    # 一个空类 pass代表直接跳过
    # 此处的pass必须有
    pass

# 定义一个对象
mingyue = Student()

# 定义一个类用来描述听Python 的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 19
    course = "Python"

    # 需要注意的
    # 1.def doHomework 的缩进层级
    # 2. 系统默认由一个self参数
    def doHomework(self):
        print("我在做作业")
        return None

# 实例化一个叫 yueyue的学生 是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

yueyue.doHomework()
