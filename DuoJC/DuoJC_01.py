# coding=utf-8

import multiprocessing
from time import sleep, ctime

print("")
'''
线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是派生进程的主要替代方案
    - Python2.4后引入
- multiprocessing
    - 使用threadiing接口派生，使用子进程
    - 允许为多核或者多cpu派生进程，接口跟threading非常相似
    - Python2.6
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - Python3.2后引入
# 多进程
    - 进程间通讯（InterprocessCommunication,IPC）
    - 进程之间无任何共享状态
    - 进程的创建
        - 直接生成Process 实例对象，案例01
        - 派生子类，案例20

- 在os中查看pid ppid 以及他们的关系
    - 案例03
- 生产消费者模型
    - JoinableQueue
    - 一个模型，可以用来搭建消息队列
    - queue 是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
    

'''
def clock(interval):
    while True:
        print('The time is {0}'.format(ctime()))
        sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    # 在主函数中没有死循环时候用非 debug模式就可运行 debug模式就不行为啥
    while True:
        print('Selping.......')
        sleep(1)