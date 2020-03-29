# 包含一个学生
#一个sayHolle函数
# 一个打印语句
class Student():
    def __init__(self,name= "NoName",age = 18):
        self.name = name
        self.age = age
    def say(self):
        print("hai  {0}  aaa".format(self.name))

def sayhello():
    print("Hi 北京欢迎您！")

# 此判断语句建议一直作为成语的入口
if __name__ == '__main__':
    print("我是模块Baodaoru，找我干哈？")