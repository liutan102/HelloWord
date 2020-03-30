try:
    num = int(input("Plz input your number"))
    rst = 100/num
    print("计算结果{0}：".format(int(rst)))
except (ZeroDivisionError,ValueError) as e:
    print("你他娘的。。。。。。")
    # exit是退出程序的意思
    print(e)
    exit()


# raise 案例
try:
    print("赛开打阿萨德阿萨德离开假的加拉看数据")
    print(123124129847129847)
    raise ValueError
except NameError as e:
    print("名字输入错了")
except ZeroDivisionError as e:
    print("不能被0除")
except ValueError as e:
    print("我是ValueError")
finally:
    print("我肯定被执行牙！")

# raise 案例2
# 自己定义异常
# 需要注意：自定义异常必须是系统异常的子类
class LiutanValueError(ValueError):
    pass
try:
    print("啊啊啊啊啊啊啊啊啊啊啊啊啊啊")
    print(222222222222222)
    raise ValueError
except NameError as e:
    print("名字输入错了")
except ZeroDivisionError as e:
    print("不能被0除")
except ValueError as e:
    print("我是ValueError")
finally:
    print("我肯定被执行牙！")

# else 语句案例
try:
    num = int(input("Plz input your number"))
    rst = 100 / num
    print("计算结果{0}：".format(int(rst)))
except (ZeroDivisionError, ValueError) as e:
    print("你他娘的。。。。。。")
else:
    print("No Exception")
finally:
    print("反正我会被执行")


