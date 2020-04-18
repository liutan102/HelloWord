# coding=utf-8
import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def fun_1():
    print('Fun_1 starting......')
    lock_1.acquire(timeout=4)
    print('fun_1 申请了 lock_1。。。。。。。。')
    time.sleep(2)
    print("Fun_1 等待lock_2....")

    rst = lock_2.acquire(timeout=2)
    if rst:
        print('fun_1 已经得到了lock_2。。。。。。。。。。')
        lock_2.release()
        print('func_1 释放了锁 lock_2')
    else:print('Fun_1 注定没申请到lock_2')
    lock_1.release()
    print('func_1 释放了 lock_1')
    print('fun_1 done......')

def fun_2():
    print('Fun_2 starting......')
    lock_1.acquire(timeout=10)
    print('fun_2 申请了 lock_1。。。。。。。。')
   # time.sleep(1)
    print("Fun_2 等待lock_1....")

    lock_2.acquire()
    print('func_2 释放了锁 lock_1')


    lock_2.release()
    print('func_2 释放了 lock_2')
    print('fun_2 done......')


if __name__ == '__main__':
    print('主程序启动。。。。。。。。。。。。')
    t1 = threading.Thread(target=fun_1, args=())
    t2 = threading.Thread(target=fun_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('主程序结束。。。。。。。。。。')





















