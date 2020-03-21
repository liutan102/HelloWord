# Python 学习
# 汉诺塔
a = "1"
b = "2"
c = "3"
def hannuo(a,b,c,n):
    if n == 1:
        print("{} @@@> {}".format(a,c))
        return None
    if n == 2:
        print("{} @@@> {}".format(a,b))
        print("{} @@@> {}".format(a,c))
        print("{} @@@> {}".format(b,c))
        return None
    hannuo(a,c,b,n-1)
    print("{} @@@> {}".format(a,c))
    hannuo(b,a,c,n-1)
hannuo(a,b,c,5)

hannuo(a,b,c,3)
hannuo(a,b,c,1)
hannuo(a,b,c,3)
hannuo(a,b,c,1)

def hannuo1(a,b,c,n):
    if n == 1:
        print("{} @@@> {}".format(a,c))
        return None
    if n == 2:
        print("{} @@@> {}".format(a,b))
        print("{} @@@> {}".format(a,c))
        print("{} @@@> {}".format(b,c))
        return None
    hannuo1(a,c,b,n-1)
    print("{} @@@> {}".format(a,c))
    hannuo(b,a,c,n-1)