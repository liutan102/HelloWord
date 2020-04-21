import multiprocessing
from time import sleep, ctime

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.__init__构造函数
    2.run
    '''
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print('The time is {0}'.format(ctime()))
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    # 在主函数中没有死循环时候用非 debug模式就可运行 debug模式就不行为啥