# coding=gbk
print("")

'''
共享变量
    - 当多个线程同时访问同一个变量的时候，会产生共享变量问题
    - 案例 01
    - 解决变量：锁，信号灯
        - 锁（lock）:
            - 是一个标志，表示一个线程在占用一些资源
            使用方法：
                - 上锁
                - 使用共享资源，放心的用
                - 取消锁，释放锁
                - 案例02
                - 锁谁：哪个资源需要多个线程共享，锁哪个
                - 理解锁：锁其实不是锁住谁，而是一个令牌
    - 线程安全问题：
        - 如果 一个资源/变量，他对多线程来讲，不用加锁也不会引起任何问题，则成为线程安全
        - 线程不安全变量类型：list set dict
        - 线程安全变量类型： queue
    - 生产者消费者问题
        - 一个模型，可以 用来搭建消息队列
        - queue 是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
    - 死锁问题，案例04
    
'''
import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum + 1):
        sum += 1

def myMium():
    global sum, loopSum
    for i in range(1,loopSum + 1 ):
        sum -= 1

if __name__ == '__main__':
    print('String ....{0}'.format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMium, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End ......{0}'.format(sum))