# coding=gbk
print("")

'''
�������
    - ������߳�ͬʱ����ͬһ��������ʱ�򣬻���������������
    - ���� 01
    - ��������������źŵ�
        - ����lock��:
            - ��һ����־����ʾһ���߳���ռ��һЩ��Դ
            ʹ�÷�����
                - ����
                - ʹ�ù�����Դ�����ĵ���
                - ȡ�������ͷ���
                - ����02
                - ��˭���ĸ���Դ��Ҫ����̹߳������ĸ�
                - �����������ʵ������ס˭������һ������
    - �̰߳�ȫ���⣺
        - ��� һ����Դ/���������Զ��߳����������ü���Ҳ���������κ����⣬���Ϊ�̰߳�ȫ
        - �̲߳���ȫ�������ͣ�list set dict
        - �̰߳�ȫ�������ͣ� queue
    - ����������������
        - һ��ģ�ͣ����� �������Ϣ����
        - queue ��һ��������ű��������ݽṹ���ص����Ƚ��ȳ����ڲ�Ԫ���Ŷӣ���������һ�������list
    - �������⣬����04
    
'''
import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum + 1):
        sum += 1

def myMium():
    global sum, loopSum
    for i in range(1,loopSum + 1 ):
        sum -= 1

if __name__ == '__main__':
    print('String ....{0}'.format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMium, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End ......{0}'.format(sum))