# coding=gbk
# 程序上方设置编码格式

from functools import reduce

#Python语言的高级特性
print("函数式编程")
'''
函数式编程
    - 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数，同样可以作为返回值
    - 纯函数式编程语言：LISP，Haskell
Python函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式一半Python
需要讲述
    - 高阶函数
    - 返回函数
    - 匿名函数
    - 装饰器
    - 偏函数
lambda表达式
    - 函数：最大程度复用代码
        - 存在问题：如果函数很小，很短，则会造成啰嗦
        - 如果函数被调用次数太少，怎会造成浪费
        - 对于阅读者来说，造成阅读流程的被迫中断
lambda表达式（匿名函数）：
    - 一个表达式 函数体相对简单
    - 不是一个代码块，仅仅是 一个表达式
    - 可以有参数，有多个参数也可以，用逗号隔开
'''
# “小”函数举例
def printA():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
printA()

'''
lambda表达式的用法
以lamdba开头
紧跟一定的参数（如果有的话）
参数后用冒号和表达式主题隔开
只是一个表达式没有return
'''
# 计算一个数字的100倍数
# 因为就是一个额表达式所以没有return
stm = lambda x: 100 * x
print(stm(89))
stm2 = lambda z,c,v: z+c*10+v *100
print(stm2(2,3,5))

'''
高阶函数
把函数作为参数使用的函数叫做高阶函数
函数名称是变量
funB 和funA 只是名称不一样而已
既然函数名称是变量，则应该可以被当做参数传入另一个函数
'''
def funA():
    print("In funA")

funB = funA
funB()


#举例 funC 是普通函数 返回一个额传入数字的100倍数字
def funC(n):
    return n * 100
#再写一个函数，把传入参数乘以300倍
def funD(n):
    return funC(n) * 3
print(funD(9))

# 再写一个高阶函数
def funE(n,f):
    return f(n)*3
print(funE(9,funC))

# 比较funE 和funD 显然funE的写法要优于funD
#例如:我不想乘以100倍了我想乘以10倍那么：重新写个乘以10 倍的函数就可以了 不需要再动funE的代码了而funD需要改动代码
def funF(n):
    return n * 10
print(funE(9,funF))

'''
系统高阶函数---map

    - 原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
    - map函就是系统提供的具有映射功能的函数，返回值是一个迭代对象
'''
# map举例
# 有一个列表，想对列表里每一个元素乘以10，并得到一个新的列表
l1 = [i for i in range(10)]
print(l1)

def maplist(n):
    return n * 10
l3 = map(maplist , l1)
for i in l3:
    print(i, end="  ")




print("")

'''
reduce
原意是归并缩减
把一个可迭代的对象最后归并成一个结果
对于作为参数的函数要求：必须由两个参数，必须由返回结果
reduce(a , [1,2,3,4,5]) == f(f(f(f(1,2),3),4),5)
reduce需要导入functools包
'''
def myAdd(x,y):
    return x + y
# 对于列表【1,2,3,4,5,6】执行myAdd的reduce操作
rst = reduce(myAdd ,[1,2,3,4,5,6])
print(rst)




