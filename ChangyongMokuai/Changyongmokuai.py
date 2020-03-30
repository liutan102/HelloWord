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
