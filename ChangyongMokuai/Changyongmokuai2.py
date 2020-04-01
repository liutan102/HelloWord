import os


# os 模块
mydir = os.getcwd()
print(mydir)

# chdir()改变当前的工作目录
# change directory
# 格式：os.chdir（路径）
# 返回值：无
os.chdir('C:/Users/Administrator/Desktop')
o = os.getcwd()
print(o)

# listdir() 获取一个目录中所有子目录和文件的名称列表
# 格式：os.listdir(路径)
# 返回值：所有子目录和文件名称的列表
# 括号如果不写则 查找的是当前工作目录
ld  = os.listdir('D:/vue_wtoip')
print(ld)

# makedirs() 递归创建文件
# 格式：os.makedirs (递归路径)
# 返回值；无
# 递归路径：多个文件夹蹭蹭包含的路径就是递归路径 例如 a/b/c...
'''
rst = os.makedirs("liutan2")

'''



# system() 运行系统shell命令
# 格式：os.system('系统命令')
# 返回值：打开一个shell或者终端界面
# ls 是列出当前文件和文件夹的系统命令
#一般推荐使用subprocess代替
#括号内是liunx系统的命令Windows不适用
sys = os.system('ls')
print('**********')
print(sys)

# 在当前目录下创建一个 dana.haha的文集
# 括号内是liunx系统的命令Windows不适用
rst = os.system("touch dana.haha")
print(rst)

# getenv() 获取指定的系统环境变量
# 格式：os.getenv('环境变量')
# 返回值：指定环境变量对应的值
env = os.getenv('PATH')
print(env)

# exit()退出当前程序
# 格式：exit()
# 返回值：无
'''
这块不屏蔽 下边程序就没法运行了
ex = os._exit(2)
print(ex)
'''
# 值部分
'''
os.curdir: curretn dir 当前目录
os.pardir : parent dir 父亲目录
os.sep:当前系统的路径分隔符
os.linesep:当前系统的换行符
os.name:当前系统的名称
'''
# 当前目录
print(os.curdir)
# 父目录
print(os.pardir)
#当前系统的路径分隔符
print(os.sep)
# 当前系统的换行符
print(os.linesep+'11')
# 当前系统的名称
# windows:nt
# mac unix linux:posix
print(os.name)

