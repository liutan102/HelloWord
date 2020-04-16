import threading
from time import sleep, ctime


class ThreadFunc:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def loop(self, name, age):
        '''
        :param nloop:loop函数的名称
        :param nsec:系统休眠时间
        :return:
        '''
        print('Start loop ', name, 'at', ctime())
        sleep(age)
        print('Done loop ', name, 'at', ctime())

def main():
    print('Starting at: ', ctime())

    # ThreadFunc('loop').loop 跟以下两个式子相等：
    # t = ThreadFunc('loop')
    # t.loop
    # 以下 t1 和 t2 的定义方式相等
    t = ThreadFunc('xxx', 1)
    t1 = threading.Thread(target= t.loop, args=('loopx', 4))
    ## 下面这种写法更西方人，工业化一点
    t2 = threading.Thread(target= ThreadFunc('xxx', 1).loop, args=('loopc', 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("ALL done at: ", ctime())

if __name__ == '__main__':
    main()
