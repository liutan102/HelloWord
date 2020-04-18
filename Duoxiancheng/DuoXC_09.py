import  threading
import time

# 1.类需要继承自threading.Thread

class MyThread(threading.Thread):
    def __init__(self, arg):
        # 以下两句话是一样的，目的都是为了调用threading.Thread类的__init__
        #super(MyThread, self).__init__()
        threading.Thread.__init__(self)
        self.arg = arg

    # 必须重写run函数，run函数代表的是真正执行的功能
    def run (self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

for i in range(4):
    t = MyThread(i)
    t.start()
    t.join()
print("Main thread is done !!!")