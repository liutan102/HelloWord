# coding=gbk
print("")
'''
补充几个高级函数
Zip
- 把两个可迭代的内容生成一个可迭代的tuple元素类型组成的内容

'''
##########zip案例
# zip是可以迭代的所以可以通过for循环 循环出来
l1 = ["wangwang", "xiaobai", "xiaohei"]
l2 = [33, 88, 44]
l3 = zip(l1, l2)
print(l3)
for i in l3:
    print(i)

'''
enumerate
- 跟zip功能比较像
- 对可以迭代对象里的每一个元素配上一个索引，然后索引和内容构成tuple类型
'''
em = [1234, 123, 1123, 55666, 122]
e = enumerate(em)
ex = [i for i in e]
print(ex)

# 如果不想让下标从 0 开始,我想从100 开始 那么：
ee = enumerate(em, start=100)
ek = [s for s in ee]
print(ek)
'''
# collections 模块
- namedtuple
    - tuple类型
    - 是一个可命名的tuple
- deque
    - 比较方便的解决了频繁删除插入带来的效率问题
'''
import collections
from collections import deque

q = deque(["a","b","c"])
print(q)
q.append("d")
print(q)
q.appendleft("z")
print(q)


'''
defaultdct
- 当直接读取dict不存在的属性时，直接返回默认值
'''





















