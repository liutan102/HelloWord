import time
import threading
def fun():
    print('Start fun')
    time.sleep(2)
    print('end fun')
print('Main thread')


t1 = threading.Thread(target=fun, args=())
# 守护线程方法 必须在start 之前设置，否则无效
t1.setDaemon(True)

t1.start()

time.sleep(1)
print('Min thread end')