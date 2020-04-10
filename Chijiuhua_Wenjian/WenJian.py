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
