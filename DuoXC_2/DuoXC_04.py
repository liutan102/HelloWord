# coding=gbk
import threading
import time

lock_1 = threading.Lock()
locl_2 = threading.Lock()
###死锁示例
def fun_1():
    print('fun_1 starting..........')
    # 为了防止死锁
    lock_1.acquire()
    print('fun_1申请了 lock_1')
    time.sleep(2)
    print('fun_1等待 locl_2...............')
    locl_2.acquire()
    print('fun_1申请了 locl_2')
    lock_1.release()
    print('fun_1释放了lock_1')
    locl_2.release()
    print('fun_1释放了 lock_2')

    print('fun_1 done..........................')

def fun_2():
    print('fun_2 starting..............')
    locl_2.acquire()
    print('fun_2申请了 locl_2')
    time.sleep(4)
    print('fun_2等待 lock_1............')
    lock_1.acquire()
    print('fun_2申请了 lock_1')
    locl_2.release()
    print('fun_2释放了locl_2.........')
    lock_1.release()
    print('fun_2释放了lcok_1............')

if __name__ == '__main__':
    print('主程序启动。。。。。。。。。。。。。。。。')
    t1 = threading.Thread(target=fun_1, args=())
    t2 = threading.Thread(target=fun_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('程序结束。。。。。。。。。。。。。。')
