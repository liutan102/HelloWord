import threading
import time


#    Timer 利用多线程 可以再指定时间后启动一个功能
def func():
    print('今天周日，十八点零六分')
    time.sleep(3)
    print('今天下雨了。。。。')

if __name__ == '__main__':

    time.sleep(3)
    t = threading.Timer(6, func)

    i = 0
    while True:

        print('{0}***********************'.format(i))

        t.start()
        i += 1