# coding=gbk
import threading
import time

lock_1 = threading.Lock()
locl_2 = threading.Lock()
###����ʾ��
def fun_1():
    print('fun_1 starting..........')
    # Ϊ�˷�ֹ����
    lock_1.acquire()
    print('fun_1������ lock_1')
    time.sleep(2)
    print('fun_1�ȴ� locl_2...............')
    locl_2.acquire()
    print('fun_1������ locl_2')
    lock_1.release()
    print('fun_1�ͷ���lock_1')
    locl_2.release()
    print('fun_1�ͷ��� lock_2')

    print('fun_1 done..........................')

def fun_2():
    print('fun_2 starting..............')
    locl_2.acquire()
    print('fun_2������ locl_2')
    time.sleep(4)
    print('fun_2�ȴ� lock_1............')
    lock_1.acquire()
    print('fun_2������ lock_1')
    locl_2.release()
    print('fun_2�ͷ���locl_2.........')
    lock_1.release()
    print('fun_2�ͷ���lcok_1............')

if __name__ == '__main__':
    print('������������������������������������������')
    t1 = threading.Thread(target=fun_1, args=())
    t2 = threading.Thread(target=fun_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('�����������������������������������')
