# coding=gbk
print("")
'''
���伸���߼�����
Zip
- �������ɵ�������������һ���ɵ�����tupleԪ��������ɵ�����

'''
##########zip����
# zip�ǿ��Ե��������Կ���ͨ��forѭ�� ѭ������
l1 = ["wangwang", "xiaobai", "xiaohei"]
l2 = [33, 88, 44]
l3 = zip(l1, l2)
print(l3)
for i in l3:
    print(i)

'''
enumerate
- ��zip���ܱȽ���
- �Կ��Ե����������ÿһ��Ԫ������һ��������Ȼ�����������ݹ���tuple����
'''
em = [1234, 123, 1123, 55666, 122]
e = enumerate(em)
ex = [i for i in e]
print(ex)

# ����������±�� 0 ��ʼ,�����100 ��ʼ ��ô��
ee = enumerate(em, start=100)
ek = [s for s in ee]
print(ek)
'''
# collections ģ��
- namedtuple
    - tuple����
    - ��һ����������tuple
- deque
    - �ȽϷ���Ľ����Ƶ��ɾ�����������Ч������
'''
import collections
from collections import deque

q = deque(["a","b","c"])
print(q)
q.append("d")
print(q)
q.appendleft("z")
print(q)


'''
defaultdct
- ��ֱ�Ӷ�ȡdict�����ڵ�����ʱ��ֱ�ӷ���Ĭ��ֵ
'''





















