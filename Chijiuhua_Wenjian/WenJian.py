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
        print(line)


####red�ǰ��ַ���ȡ�ļ�����
##��������������������������û��ָ�����򣬴ӵ�ǰλ�ö�ȡ����β������ӵ�ǰλ�ö�ȡָ�������ַ�

with open("test01.txt","r",encoding="UTF-8") as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)

'''
��ҵ��
ʹ��read ��ȡ�ļ���ÿ�ζ�ȡһ����ʹ��ѭ������
�������ָ�ʽ
'''
with open("test01.txt","r",encoding="UTF-8") as f:
    ok = f.read(1)
    while ok:
        print(ok,end="")
        ok = f.read(1)

'''
seek (offset,from)
    - �ƶ��ļ��Ķ�ȡλ�ã�Ҳ������ȡָ��
    - from��ȡֵ��Χ��
        - 0�����ļ�ͷ��ʼƫ��
        - 1�����ļ���ǰλ�ÿ�ʼƫ��
        - 2�����ļ�ĩβ��ʼƫ��
    - �ƶ��ĵ�λ���ֽڣ�byte��
    - һ�����������ɸ��ֽڹ���
    - �����ļ�ֵ��Ե�ǰλ��

'''
# seek ����
# ���ļ���ӵ�5���ֽڿ�ʼ��ȡ
print("123123123123123123")
with open("test01.txt","r",encoding="UTF-8") as f:
    f.seek(6, 0)
    st = f.read()
    print(st)
'''
���ڶ�ȡ�ļ�����ϰ
���ļ��������ַ�һ��������ݣ�Ȼ����ʾ����Ļ��
ÿ��ȡһ�Σ���Ϣһ����
'''
import time

with open("test01.txt","r",encoding="UTF-8") as f:
    sss = f.read(3)
    while sss:
        print(sss)
        # sellp ������λ����
        # ���ε���Ϊ���±߳���������ٶȿ�
    #    time.sleep(3)
        sss = f.read(3)

'''
�����ϱ����н��Ϊɶ����ÿ�������ַ�
'''

print("�ٺ�IEhi����IEhi����IEhi����hi��")
# tell������������ʾ�ļ���дָ��ĵ�ǰλ��
with open("test01.txt","r",encoding="UTF-8") as f:
    stt = f.read(3)
    # ��ȡ��ʾ�ļ���ָ��ĵ�ǰλ��
    ops = f.tell()
    while stt:
        print(stt)
        print(ops)

        stt = f.read(3)
        ops = f.tell()

'''
�ļ���д����-write
    - write(str)�����ַ���д���ļ�
    - writeline��str�������ַ�������д���ļ�
    - ����:
        - write��������ֻ�����ַ���
        - writeline ��������д��ܶ��У�����������list��ʽ
'''
# write����
# ���ļ�׷��һ��ʫ
l = {"adad","asdsad","ewrtret","sdssss"}
with open("test01.txt","a",encoding="UTF-8")as f:
    f.write("�����յ��磬\n���κ�����\n")
    f.writelines(l)

'''
�־û� - pickle
    - ���л����־û�����أ����ѳ��������е���Ϣ�����ڴ�����
    - �����л������кŵ������
    - pickle:Python�ṩ�����л�ģ��
    - pickle.dump���л�
    - pickle.load�������л�

'''
# ���л�����
import pickle
'''
age = "asdas��˹��"
with open(r"test01.txt","w") as f:
    pickle.dump(age,f)



'''

'''
�־û� - shelve
    - �־û�����
    - �����ֵ䣬��kv�Ա������ݣ���ȡ��ʽ���ֵ�Ҳ����
    - open,close
'''
import shelve
# ���ļ�
# shv�൱��һ���ֵ�
shv = shelve.open("shv.db")

shv["one"] = 1
shv["two"] = 2
shv["three"] = 3
shv.close()
# ͨ�����ϰ��� ���� shelve�Զ������Ĳ�������һ��shv.db �ļ����������������ļ�

#shelve��ȡ����
shv = shelve.open("shv.db")
print("qaqdasdasdasda12232323")
try:
    print(shv["one"])
    print(shv['two'])
except Exception as e:
    print("������")
finally:
    shv.close()
'''
### shelve ���ԣ�
    - ��֧�ֶ��Ӧ�ò���д��
        - Ϊ�˽��������⣬open��ʱ�����ʹ��flag=r
    - д������
        - shelv
        - ���������ǿ��д�أ�writeback = true
        
'''
