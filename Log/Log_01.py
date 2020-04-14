#coding=gbk
print("")
'''
log
https://www.cnblogs.com/yyds/p/6901864.html
logging
-logging模块提供模块级别的函数记录日志 

'''

'''
#日志相关概念
- 日志
- 日志级别（level）
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO 操作==》不要频繁操作
- log的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - logj
    - log4php
    - logging
'''
# logging 模块
'''
- 初始化/写 日志实力需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方法：
    - 直接使用logging（封装了其他组件）
    - logging四大组件直接定制
# 2.1 logging模块级别的日志
    - 使用一下几个函数
        logging.debug(msg,*args,**kwargs) 创建一条严重级别为DEBUG的日志记录
        logging.info(msg,*args,**kwargs) 创建一条严重级别为INFO的日志记录
        logging.warning(msg,*args,**kwargs) 创建一条严重级别为WARNING的日志记录
        logging.error(msg,*args,**kwargs) 创建一条严重级别为ERROR的日志记录
        logging.critical(msg,*args,**kwargs) 创建一条严重级别为CRITICAL的日志记录
        logging.log(level,*args,**kwargs) 创建一条严重级别为LEVEL的日志记录
        logging.basicConfig(**kwargs) 对root logger进行一次性配置
'''
'''
logging.basicConfig(**kwargs)     对root logger进行一次性配置
    - 只在第一次调用的时候起作用
    - 不配置logger则使用默认值
    - 输出  sys.stderr
    - 级别 WARNING
    - 格式：lever:log_name:content

logging模块常用format格式说明
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息

原文链接：https://blog.csdn.net/orca123456/article/details/84864785


'''

import logging

LOG_FORMAT = "%(asctime)s=========%(levelname)s+++++++++++%(message)s-----------%(pathname)s"
logging.basicConfig(filename="TheLog.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log ")
logging.error("This is a error log")
logging.critical("This is a critical log ")



# 另一种写法
logging.log(logging.DEBUG, "This is a DEBUG log")
logging.log(logging.INFO, "This is a INFO log")
logging.log(logging.WARNING, "This is a WARNING log")
logging.log(logging.ERROR, "This is a ERROR log")
logging.log(logging.CRITICAL, "This is a CRITICAL log")



'''
2.1 logging 模块的处理流程
- 四大组件
    - 日志器（logger）:产生日志的一个接口
    - 处理器（Handler）: 把产生的日志发送到相应的目的地
    - 过滤器（Filter）：更精细的控制那些日志输出
    - 格式器（Formatter）：对输出信息进行格式化
'''





