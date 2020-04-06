# coding =  gbk

print("")
'''
filter函数
过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
跟map想比较：
    - 相同：都对列表的每一个元素逐一进行操作
    - 不同：
        - map会生成一个跟原来数据相对应的新队列
        - filter 不一定，只要符合条件的才会进入新的数据集合
    - filter 函数怎么写：
        - 利用给定函数进行判断
        - 返回值一定是个布尔值
        - 调用格式：filter(f,data),f 是过滤函数，data是数据

'''
#########################################filter案例##############################################################################################################################################################################
'''
对于一个列表，对其进行过滤，偶数组成一个新列表
需要定义过滤函数
过滤函数要求有输入，返回值
'''
def isEven(n):
    return n % 2 == 0
l = [2,3,4,5,6,7,8,82,2,34,22,33,11]
res = filter(isEven,l)

print(type(res))
print(res)
# 以下两种都可以，有什么不太好的后边自己找不同
print([i for i in res])

print(list(res))
'''
高阶函数- 排序---- sorted
- 把一个序列按照给定算法进行排序
- key:在排序前对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序
- Python2 和Python3相差巨大
#案例
'''
a = [21,3,43,54,6,76,5,4,43,3,32,34,5,5,56,76,7,67,56,4,43,3,23,3,4]
# 后边参数是给他进行正序或者倒叙排序
al  = sorted(a,reverse=True)
print(al)
print(help(sorted))

#################################返回函数################################################################################################################
'''
返回函数
    - 函数可以返回具体的值
    - 也可以返回一个函数作为结果
    
'''
def myF(n):
    print("In myF")
    return None
a = myF(6)
print(a)
# 函数作为一个返回值，被返回的函数在函数体内定义
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3
# 使用上边定义
# 调用myF2,返回一个函数的myF3,赋值给" l "
ll = myF2()
print(ll)
print(type(ll))
ll()


'''
#### 复杂一点的返回函数例子
# args:参数列表
1,myF4定义函数，返回内部定义的函数myF5
2，myF5使用了外部变量，这个变量是myF5
'''

def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5
f5 = myF4(1,2,3,4,5,6,7,0)
f5()
print(myF4)
print(f5())

'''
闭包（closure）
- 当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，当内部函数被当做
返回值的时候，相关参数和变量保存在返回的函数中，这种结果叫闭包
- 上面定义的myF4是一个标准的闭包
'''
# 闭包常见的坑
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f 是一个闭包结构
        def f():
            # 结果想打印的是 1*1 2*2 3*3
            return i * i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
'''
出现问题的原因：
    - 返回函数引用了变量i，i并非立即执行，而是等到三个函数都返回的时候才会统一使用，此时的i已经变成了3
    最终调用的时候，返回都是3*3
- 此问题描述：返回闭包时候，返回函数不能引用任何循环变量
解决方案：再创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不在改变
'''
# 解决办法
def count1():
    fs = []
    def g(j):
        def f():
            return j * j
        return f
    for i in range(1, 4):
        fs.append(g(i))
    return fs
q1,q2,q3 = count1()
print(q1())
print(q2())
print(q3())

'''
装饰器
- 在不改动代码的基础上无限制扩展函数功能的一种机制，本质上，装饰器是一个返回函数的高阶函数
- 装饰器的使用：使用@语法，即在每次要扩展到函数定义前使用@ + 函数名
装饰器好处：
- 一点定义则可以装饰任意函数
- 一旦被其装饰，则吧装饰器的功能直接添加定义函数的功能上

'''
import time

def hello():
    print("hello Word")

f = hello
f()

# 对hello函数功能进行扩展，每次执行hello前打印当前时间
def printTime(m):
    def wrapper(*args ,**kwargs):
        print("时间：",time.ctime())
        # 在着return的意思是为了 防止把函数当做参数传进来的时候情况
        return m(*args ,**kwargs)
    return wrapper


@printTime
def hello1():
    print("hello,Word")

x = hello1
x()
######手动执行装饰器
def hello3():
    print("我是手动执行的")

hello3()

hello33 =printTime(hello3)
hello33()
f = printTime(hello3)
f()
'''
偏函数
参数固定的函数，相当于一个由特定参数的函数体
functools.partial的作用，把一个函数某些函数固定，返回一个新的函数
'''
import functools

int16 = functools.partial(int,base = 16)
print(int16("123123"))
