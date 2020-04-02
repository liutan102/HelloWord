import os
import os.path as op
import shutil
import zipfile
import random

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


#os.path 模块，跟路径相关的模块
'''
abspath()将路径转化为绝对路径
abselute 绝对路径
格式：os.path.abspath(''路径)
返回值：路径的绝对路径形式
linux中 . 号代表当前目录  ..代表父目录
'''
absp = op.abspath(".")
print(absp)

'''
basename()获取当前路径中path最后的文件名。如果path以/或\结尾,那么就会返回空值
格式 os.path.basename(路径)
返回值：文件名字符串
'''
bn = op.basename("C:/Users/Administrator/Desktop")
print(bn)
bs = op.basename("/Users/Amd")
print(bs)

'''
join()将多个路拼一个路径
格式：os.path.join(路径1，路径2.。。。)
返回值：组合之后的新路径字符串
'''
db = "C:/Users/Administrator/Desktop/"
fn = "dd/aa/cc"
print(op.join(db,fn))

'''
split()将路径切割为文件夹部分和当前文件部分;如果不写文件它会把最后一个文件夹当做文件去处理
格式 os.path.split(路径)
返回值：路径和文件名组成的元组

'''
t = op.split("/home/tlxy/adna.dana")
print(t)
g,h = op.split("/home/tlxy/adna.dana")
print(g,h)

'''
isdir() 检测是否是目录
格式 os.path.isdir(路径)
返回值：布尔值

'''
rst = op.isdir("C:/Users/Administrator/Desktop/")
print(rst)

'''
exists()检测文件或者目录是否存在
格式 os.path.exists(路径)
返回值：布尔值

'''
e = op.exists("C:/Users")
print(e)

# shutil模块

'''
copy()复制文件
格式：shutil.copy(来源路径，目标路径)
返回值：返回目标路径
拷贝的同时，可以给文件重命名

'''
r = shutil.copy("C:/Users/Administrator/11.txt","C:/Users/Administrator/Desktop/")


'''
copy2()复制文件，保留元组（文件信息）
格式：shutil.copy2(来源路径，目标路径)
返回值：返回目标路径
注意：copy 和copy2的唯一区别在于copy2复制文件时尽量保留元数据（元数据被定义为：描述数据的数据，对数据及信息资源的描述性信息。）
'''
po = shutil.copy2("C:/Users/Administrator/22.txt","C:/Users/Administrator/Desktop/")
print(po)

'''
copyfile()将一个文件中的内容复制到另一个文件中
格式：shutil.copyfile('原路径','目标路径')
返回值：无

'''
help(shutil.copyfile)
aa = shutil.copyfile("11.txt","22.txt")
print(aa)
'''
move() 移动文件/文件夹
格式：shutil.move(原路径，目标路径)
返回值：目标路径

'''
ab = shutil.move("C:/Users/Administrator/Desktop/22.txt","C:/Users/Administrator/Desktop/bin")
'''
remove() 删除一个文件
格式：os.remove(路径)
返回值：无
'''
vv = os.remove("C:/Users/Administrator/Desktop/bin/22.txt")


##########################################归档和压缩##########################################################################################
'''
归档：把多个文件或者文件夹合并到一个文件当中
压缩：用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
make_archive()归档操作
格式：shutil.make_archive（"归档之后的目录和文件名","后缀","需要归档的文件夹"）
返回值：归档之后的地址
'''
hh = shutil.make_archive("C:/Users/Administrator/Desktop/liutan2","zip","C:/Users/Administrator/Desktop/222")
print(hh)

'''
unpack_archive()解包操作
格式:shutil.unpack_archive("归档文件地址","解包之后的地址")
返回值：
'''
kk = shutil.unpack_archive("C:/Users/Administrator/Desktop/liutan2.zip","C:/Users/Administrator/Desktop/123")
print(kk)
'''
ZIP压缩包
模块（方法）名称叫 zipfile
创建一个zipfile对象表示一个zip文件 参数file表示文件的路径或类文件对象
'''
zf = zipfile.ZipFile("C:/Users/Administrator/Desktop/liutan2.zip")
print(zf)
'''
ZipFile.getinfo(name)
获取zip文档内指定文件信息，返回一个zipfile.Zipinfo对象他包括文件的详细信息
'''
ll = zf.getinfo("11.txt")
print(ll)

'''
zipfile.namelist()
获取zip文档内所有文件的名称列表
'''
nl = zf.namelist()
print(nl)
'''
zipfile.extractall()
解压zip文档中的所有文件到当前目录，参数members的默认值为zip文档内的所有文件名称
'''
iu = zf.extractall("C:/Users/Administrator/Desktop/")
print(iu)

############################random模块###################################################################################################################
'''
random
随机数
所有的随机模块都是伪随机
random() 获取0-1之间的随机小数
格式：random.random()
返回值：随机0-1之间的小数
'''
print(int(random.random()* 100) )

'''
chon

'''
















