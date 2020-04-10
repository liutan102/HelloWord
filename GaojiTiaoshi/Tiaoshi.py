# coding=gbk

def sayHello(name):
    print("I want to say hello with your,{0}".format(name))
    print("Hello,{0}".format(name))
    print("Done..................")

if __name__ == '__main__':
    print("*************"* 10)
    name = input("Please input your name:")
    print(sayHello(name="12312"))
    print("@@@@" * 10 )