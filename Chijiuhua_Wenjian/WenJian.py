# coding=gbk
print("")
'''
�ļ�
    - ���ñ�����Ϣ��һ��������Ϣ����
    - ���ò���
        - �򿪹رգ��ļ�һ���򿪣���Ҫ�رղ�����
        - ��д����
        - ����
open����
    - open����������ļ������кܶ����
    - ��һ�������������У��ļ���·��������
    - mode:�����ļ���ʲô��ʽ��
        - r:��ֻ����ʽ��
        - w��д��ʽ�򿪣����ļ��Ѿ����ڣ�����
        - x:������ʽ�򿪣����ļ��Ѿ����ڣ�����
        - a��append��ʽ����׷�ӵķ�ʽ���ļ����ݽ���д��
        - b��binary��ʽ�������Ʒ�ʽд��
        - +���ɶ�д

'''
# ���ļ� ��д�ķ�ʽ
# r ��ʾ�����ַ������ݲ���Ҫת��
# f ��֮Ϊ�ļ����
f = open(r"test01","w")
# �ļ��򿪺����ر�
f.close()
# ���ϰ���˵������д�ķ�ʽ���ļ���Ĭ�������û���ļ��򴴽�

'''
with ���
    - with���ʹ�õļ�����һ�ֳ�Ϊ�����ļ�����Э��ļ�����ContextManagementProtocal��
    - �Զ��ж��ļ����������Զ��رղ���ʹ�õĴ򿪵��ļ����
    
'''
# with��䰸��
# �������鿪ʼ���ļ�f���в���
# �ڱ�ģ���в���Ҫ��ʹ��close�ر��ļ�f
with open("test01.txt", "r", encoding='UTF-8') as f:
    pass

# with����
with open("test01.txt", "r", encoding='UTF-8') as f:
    # ���ж�ȡ����
    strLine = f.readline()
    # �˽ṹ��֤�ܹ�������ȡ�ļ�ֱ������
    while strLine:
        print(strLine)
        strLine = f.readline()
print("*" * 20)
# list ���ô򿪵��ļ���Ϊ���������ļ���ÿһ��������Ϊһ��Ԫ��
with open("test01.txt", "r", encoding="UTF-8") as f:
    # �Դ򿪵��ļ�f��Ϊ�����������б�
    l = list(f)
    for line in l:
        print(line,end="")


####read�ǰ��ַ���ȡ�ļ�����
##��������������������������û��ָ�����򣬴ӵ�ǰλ�ö�ȡ����β������ӵ�ǰλ�ö�ȡָ�������ַ�
print("*" * 8)
with open("test01.txt","r",encoding="UTF-8") as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)

#��ҵ��ʹ��read ��ȡ�ļ���ÿ�ζ�ȡһ����ʹѭ������
#�������ָ�ʽ

with open("test01.txt","r",encoding="UTF_8") as f:
    gooding = list()
    while True:
        gooding = f.read(1)
        print(gooding ,end="")


'''
seek(offset, from)
    - �ƶ��ļ��Ķ�ȡλ�ã�Ҳ�ж�ȡָ��
    - fromȡֵ��Χ��
        - 0�����ļ�ͷ��ʼƫ��
        - 1�����ļ���ǰλ�ÿ�ʼƫ��
        - 2�����ļ�ĩβ��ʼƫ��
    - �ƶ��ĵ�λ���ֽڣ�byte��
    - һ�����������ɸ��ֽڹ���
    - �����ļ�ֻ��ԣ���ǰλ��
'''
# seek����
# ���ļ��󣬴ӵ�����ֽڿ�ʼ��ȡ
# �򿪶�дָ����0 �������ļ��Ŀ�ͷ
print("123123123123123123")
with open("test01.txt","r",encoding="UTF-8") as f:
    # seek�ƶ���λ���ֽ�
    f.seek(6,0)
    xyz = f.read()
    print(xyz)
























