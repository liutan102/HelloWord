import time
import _thread as thread
import threading


def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 把参数打印出来
    print("我是参数 ", in1)
    # 睡眠时间  单位秒
    time.sleep(4)
    print("End loop 1 at", time.ctime())


def loop2(in1, in2):
    print("Start loop 2 at:", time.ctime())
    # 把参数in1和参数 In2 打印出来，代表使用
    print("我是参数", in1, "和参数", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:", time.ctime())


def main():
    print("Starting at:", time.ctime())
    '''
        启动多线程的意思是用多线程去执行某个函数
        启动多线程函数为start_new_thead
        参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
        注意：如果函数只有一个参数，需要参数后有一个逗号
    '''
    t1 = threading.Thread(target=loop1, args=("红色", ))
    t1.start()
    # 这有 0.001秒延迟的意思是 为了 防止在控制台打印的结果顺序混乱
    #time.sleep(0.001)
    t2 = threading.Thread(target=loop2, args=("白白","兰兰"))
    t2.start()
    #time.sleep(0.001)

    print("All done at :", time.ctime())


if __name__ == '__main__':
    main()
    '''
    一定要有while语句
    因为启动多线程后本程序就作为主线程存在
    如果主线程执行完毕，则子线程可能也需要终止

    '''
    while True:
        time.sleep(10)