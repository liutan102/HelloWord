#coding=gbk
print("")
'''
环境
    - https://www.cnblogs.com/jokerbj/p/7460260.html
    - https://www.dabeaz.com/python/UnderstandingGIL.pdf

多线程 vs 多进程
    - 程序：一堆代码以文本形式存入一个文档
    - 进程：程序运行的一个状态
        - 包含地址空间，内存，数据栈等
        - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
    - 线程：
        - 一个进程的独立运行片段，一个进程可以有多个线程 
        - 轻量化的进程
        - 一个进程的多个线程间共享数据和上下文运行环境
        - 共享互斥的问题
    - 全局解释器锁（GIL）
        - Python代码的执行是由Python虚拟机进行控制
        
    - Python包
        - thread:有问题 不好用，Python3改成了   _thread
        - threading：通行的包
        案例01 ,02,03：
    - threading的使用
        - 直接利用 threading.Thread生成Thread实例
            1.t = threading.Thread(target=xxx, args=(xxx, ))
            2. t.start():启动多线程
            3. t.join():等待多线程执行完成
            4.案例04
            5.案例05 加入join后比较和案例04的异同
    - 守护线程 - daemon
        - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
        - 一般认为，守护线程不重要，当不允许子线程离开主线程独立运行，那么这个时候要把他设置成守护线程
        - 守护线程案例能否有效果跟环境相关
        - 案例 06非守护线程
        - 案例 07 守护线程
    - 线程常用属性
        - threading.currentThread:返回当前线程变量
        - threading.enumerate:返回一个包含正在运行的线程的list 正在运行的线程指的是线程启动后和结束前的状态
        - threading.activeCount:返回正在运行的线程数量，效果跟len(threading,enumerate)相同
        - thr.setName：给线程设置名字
        - thr.getName：得到线程的名字
    - 直接继承来自threading.Thread
        - 直接继承Thread
        - 重写run函数
        - 类实例可以直接运行
        - 案例09
        - 案例10
        
        
        
        
        
# 利用time函数，生成两个函数
# 顺序调用
计算总的运行时间
'''

import time
def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    # 睡眠多长时间 单位秒
    time.sleep(4)
    print("End loop 1 at",time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :',time.ctime())
    # 睡眠多长时间 单位秒
    time.sleep(2)
    print("End loop 2 at",time.ctime())


def main():
    # ctime 得到当前时间
    print('Starting at :',time.ctime())
    # 睡眠多长时间 单位秒
    loop1()
    loop2()
    print("All done at",time.ctime())

if __name__ == '__main__':
    main()