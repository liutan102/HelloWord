import multiprocessing
from time import ctime




def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print('put',item,'into q ')
    print('Out of procuder:', ctime())

def producer(sequence, output_q):
    print('Into producer', ctime())
    for item in sequence:
        output_q.put(item)
        print('put', item, 'into_q')
    print('Out of Producer:', ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p1 = multiprocessing.Process(target= consumer,args=(q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()
    # 生产多个项，sequence 代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或者通过一些其他方式生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # 有几个需要结束的子线程就写几个None 因为上边有break 获取一个后就会结束不会再获取下一个None了

    q.put(None)
    q.put(None)
    cons_p1.join()
    cons_p2.join()