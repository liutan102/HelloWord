#coding=gbk
print("")
'''
����
    - https://www.cnblogs.com/jokerbj/p/7460260.html
    - https://www.dabeaz.com/python/UnderstandingGIL.pdf

���߳� vs �����
    - ����һ�Ѵ������ı���ʽ����һ���ĵ�
    - ���̣��������е�һ��״̬
        - ������ַ�ռ䣬�ڴ棬����ջ��
        - ÿ���������Լ���ȫ���������л���������̹���������һ������
    - �̣߳�
        - һ�����̵Ķ�������Ƭ�Σ�һ�����̿����ж���߳� 
        - �������Ľ���
        - һ�����̵Ķ���̼߳乲�����ݺ����������л���
        - �����������
    - ȫ�ֽ���������GIL��
        - Python�����ִ������Python��������п���
        
    - Python��
        - thread:������ �����ã�Python3�ĳ���   _thread
        - threading��ͨ�еİ�
        ����01 ,02,03��
    - threading��ʹ��
        - ֱ������ threading.Thread����Threadʵ��
            1.t = threading.Thread(target=xxx, args=(xxx, ))
            2. t.start():�������߳�
            3. t.join():�ȴ����߳�ִ�����
            4.����04
            5.����05 ����join��ȽϺͰ���04����ͬ
    - �ػ��߳� - daemon
        - ����ڳ����н����߳����ó��ػ��̣߳������̻߳������߳̽�����ʱ���Զ��˳�
        - һ����Ϊ���ػ��̲߳���Ҫ�������������߳��뿪���̶߳������У���ô���ʱ��Ҫ�������ó��ػ��߳�
        - �ػ��̰߳����ܷ���Ч�����������
        - ���� 06���ػ��߳�
        - ���� 07 �ػ��߳�
    - �̳߳�������
        - threading.currentThread:���ص�ǰ�̱߳���
        - threading.enumerate:����һ�������������е��̵߳�list �������е��߳�ָ�����߳�������ͽ���ǰ��״̬
        - threading.activeCount:�����������е��߳�������Ч����len(threading,enumerate)��ͬ
        - thr.setName�����߳���������
        - thr.getName���õ��̵߳�����
    - ֱ�Ӽ̳�����threading.Thread
        - ֱ�Ӽ̳�Thread
        - ��дrun����
        - ��ʵ������ֱ������
        - ����09
        - ����10
        
        
        
        
        
# ����time������������������
# ˳�����
�����ܵ�����ʱ��
'''

import time
def loop1():
    # ctime �õ���ǰʱ��
    print('Start loop 1 at :',time.ctime())
    # ˯�߶೤ʱ�� ��λ��
    time.sleep(4)
    print("End loop 1 at",time.ctime())


def loop2():
    # ctime �õ���ǰʱ��
    print('Start loop 2 at :',time.ctime())
    # ˯�߶೤ʱ�� ��λ��
    time.sleep(2)
    print("End loop 2 at",time.ctime())


def main():
    # ctime �õ���ǰʱ��
    print('Starting at :',time.ctime())
    # ˯�߶೤ʱ�� ��λ��
    loop1()
    loop2()
    print("All done at",time.ctime())

if __name__ == '__main__':
    main()