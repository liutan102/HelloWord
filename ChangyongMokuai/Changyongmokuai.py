# calendar
# 跟日历相关的模块
# 需要先导入
import calendar
# calendar:获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2020)
print(cal)
print(type(cal))


# isleap:判断某一年是否是闰年
print(calendar.isleap(2020))

# leapdays 获取指定年份之间的闰年的个数
print(calendar.leapdays(2002,2050))

# month() 获取某个月的日历字符串
# 格式：calendar.month(年，月)
# 回值：月日历的字符串
m3 = calendar.month(2018,3)
print(m3)

# monthrange() 获取一个月的周几开始即和天数
# 格式 calendar，monthrange（年，月）
# 回值；元组（周几开始，总天数）
# 注意；周默认0-6 表示周一到周天
help(calendar.monthrange)
m = calendar.monthcalendar(2020,3)
print(m)
for x in m:

    for a in x:

        print(a,end='  ')
    print()


# prcal：print calendar 直接打印日历
calendar.prcal(2020)
# prmonth 直接打印整个月的日历
# 格式：calendar.prmonth（年，月）
calendar.prmonth(2020,1)


# weekday()获取周几
# 格式；calendar.weekday(年，月，日)
#返回值：周几对应的数字
print(calendar.weekday(2020,2,20))

# 需要单独导入
import time
# 时间模块的属性
# timezone ；当前时区和UTC时间相差的秒数，有没有夏令时的情况下的间隔,东八区的是 -28800
# altzone 获取当前时区与UTC时间相差的秒数，在没有夏令时的情况下
# daylight:测当前是否是夏令时间 状态0 表示 是
print(time.timezone)

# 得到时间戳
print(time.time())

# localtime 得到当前时间的时间结构
t = time.localtime()

print(t)

tt = time.asctime(t)
print(tt)

# ctimel:获取字符串化得当前时间
x = time.ctime()
print(type(x))
print(x)

# mktime() 使用时间元组获取对应的时间戳
# 格式； time.mktime(时间元组)
# 返回值：浮点数的时间戳
ts = time.localtime()
print("*")
print(type(ts))
lt = time.mktime(ts)
print(lt)


print(time.time())


# clock 获取cpu时间 3.0---3.3版本直接使用，3.6调用有问题
#print(time.clock())


# sleep 使程序进入睡眠 n秒后继续
for i in  range(1,10):
    print(i)
    time.sleep(0)


#help(range)

# strftime;将时间元组转化为自定义的字符串格式

# 把时间表示成 2020.3.31 17.27
import locale
locale.setlocale(locale.LC_CTYPE,'chinese')
q = time.localtime()

ff = time.strftime("%Y年%m月%d日  %H时：%M分" , q)

print(ff)


