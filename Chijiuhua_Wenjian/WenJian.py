# coding=gbk
print("")
'''
文件
    - 长久保存信息的一种数据信息集合
    - 常用操作
        - 打开关闭（文件一但打开，需要关闭操作）
        - 读写内容
        - 查找
open函数
    - open函数负责打开文件，带有很多参数
    - 第一个参数：必须有，文件的路径和名称
    - mode:标明文件用什么方式打开
        - r:以只读方式打开
        - w：写方式打开，如文件已经存在，报错
        - x:创建方式打开，如文件已经存在，报错
        - a：append方式，以追加的方式对文件内容进行写入
        - b：binary方式，二进制方式写入
        - +：可读写

'''
# 打开文件 用写的方式
# r 表示后面字符串内容不需要转义
# f 称之为文件句柄
f = open(r"test01","w")
# 文件打开后必须关闭
f.close()
# 以上案例说明，以写的方式打开文件夹默认是如果没有文件则创建

'''
with 语句
    - with语句使用的技术是一种称为上下文件管理协议的技术（ContextManagementProtocal）
    - 自动判断文件的作用域，自动关闭不再使用的打开的文件句柄
    
'''
# with语句案例
# 下面语句块开始对文件f进行操作
# 在本模块中不需要再使用close关闭文件f
with open("test01.txt", "r", encoding='UTF-8') as f:
    pass

# with案例
with open("test01.txt", "r", encoding='UTF-8') as f:
    # 按行读取内容
    strLine = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strLine:
        print(strLine)
        strLine = f.readline()
print("*" * 20)
# list 能用打开的文件作为参数，把文件内每一行内容作为一个元素
with open("test01.txt", "r", encoding="UTF-8") as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)


####red是按字符读取文件内容
##允许输入参数决定读几个，如果没有指定规则，从当前位置读取到结尾；否则从当前位置读取指定个数字符

with open("test01.txt","r",encoding="UTF-8") as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)

'''
作业：
使用read 读取文件，每次读取一个，使用循环读完
尽量保持格式
'''
with open("test01.txt","r",encoding="UTF-8") as f:
    ok = f.read(1)
    while ok:
        print(ok,end="")
        ok = f.read(1)

'''
seek (offset,from)
    - 移动文件的读取位置，也叫作读取指针
    - from的取值范围：
        - 0：从文件头开始偏移
        - 1：从文件当前位置开始偏移
        - 2：从文件末尾开始偏移
    - 移动的单位是字节（byte）
    - 一个汉字由若干个字节构成
    - 返回文件值针对当前位置

'''
# seek 案例
# 打开文件后从第5个字节开始读取
print("123123123123123123")
with open("test01.txt","r",encoding="UTF-8") as f:
    f.seek(6, 0)
    st = f.read()
    print(st)
'''
关于读取文件的练习
打开文件，三个字符一组读出内容，然后显示在屏幕上
每读取一次，休息一秒钟
'''
import time

with open("test01.txt","r",encoding="UTF-8") as f:
    sss = f.read(3)
    while sss:
        print(sss)
        # sellp 参数单位是秒
        # 屏蔽掉是为了下边程序的运行速度快
    #    time.sleep(3)
        sss = f.read(3)

'''
解释上边运行结果为啥不是每行三个字符
'''

print("嘿嘿IEhi二环IEhi二环IEhi诶诶hi恶化")
# tell函数：用来显示文件读写指针的当前位置
with open("test01.txt","r",encoding="UTF-8") as f:
    stt = f.read(3)
    # 读取显示文件的指针的当前位置
    ops = f.tell()
    while stt:
        print(stt)
        print(ops)

        stt = f.read(3)
        ops = f.tell()

'''
文件的写操作-write
    - write(str)：把字符串写入文件
    - writeline（str）：把字符串按行写入文件
    - 区别:
        - write函数参数只能是字符串
        - writeline 参数可以写入很多行，参数可以是list格式
'''
# write案例
# 想文件追加一句诗
l = {"adad","asdsad","ewrtret","sdssss"}
with open("test01.txt","a",encoding="UTF-8")as f:
    f.write("锄禾日当午，\n汗滴禾下土\n")
    f.writelines(l)

'''
持久化 - pickle
    - 序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
    - 反序列化：序列号的逆过程
    - pickle:Python提供的序列化模块
    - pickle.dump序列化
    - pickle.load：反序列化

'''
# 序列化案例
import pickle
'''
age = "asdas阿斯达"
with open(r"test01.txt","w") as f:
    pickle.dump(age,f)



'''

'''
持久化 - shelve
    - 持久化工具
    - 类似字典，用kv对保存数据，存取方式跟字典也类似
    - open,close
'''
import shelve
# 打开文件
# shv相当于一个字典
shv = shelve.open("shv.db")

shv["one"] = 1
shv["two"] = 2
shv["three"] = 3
shv.close()
# 通过以上案例 发现 shelve自动创建的不仅仅是一个shv.db 文件，还包括其他的文件

#shelve读取案例
shv = shelve.open("shv.db")
print("qaqdasdasdasda12232323")
try:
    print(shv["one"])
    print(shv['two'])
except Exception as e:
    print("哈哈哈")
finally:
    shv.close()
'''
### shelve 特性：
    - 不支持多个应用并行写入
        - 为了解决这个问题，open的时候可以使用flag=r
    - 写回问题
        - shelv
        - 解决方法：强制写回：writeback = true
        
'''
