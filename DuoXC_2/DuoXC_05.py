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
