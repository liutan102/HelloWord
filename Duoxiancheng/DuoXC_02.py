
import time
import _thread as thread

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
    print("End loop 2 at:",time.ctime())


def main():
    # ctime 得到当前时间
    print('Starting at :', time.ctime())
    '''
    启动多线程的意思是用多线程去执行某个函数
    启动多线程函数为start_new_thead
    参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    注意：如果函数只有一个参数，需要参数后有一个逗号
    '''
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)