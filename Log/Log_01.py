#coding=gbk
print("")
'''
log
https://www.cnblogs.com/yyds/p/6901864.html
logging
-loggingģ���ṩģ�鼶��ĺ�����¼��־ 

'''

'''
#��־��ظ���
- ��־
- ��־����level��
    - ��ͬ���û���ע��ͬ�ĳ�����Ϣ
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO ����==����ҪƵ������
- log������
    - ����
    - �˽�������������
    - ������λ����
- ��־��Ϣ
    - time
    - �ص�
    - level
    - ����
- ����ĵ�������־
    - logj
    - log4php
    - logging
'''
# logging ģ��
'''
- ��ʼ��/д ��־ʵ����Ҫָ������ֻ�е�������ڻ����ָ������ű���¼
- ʹ�÷�����
    - ֱ��ʹ��logging����װ�����������
    - logging�Ĵ����ֱ�Ӷ���
# 2.1 loggingģ�鼶�����־
    - ʹ��һ�¼�������
        logging.debug(msg,*args,**kwargs) ����һ�����ؼ���ΪDEBUG����־��¼
        logging.info(msg,*args,**kwargs) ����һ�����ؼ���ΪINFO����־��¼
        logging.warning(msg,*args,**kwargs) ����һ�����ؼ���ΪWARNING����־��¼
        logging.error(msg,*args,**kwargs) ����һ�����ؼ���ΪERROR����־��¼
        logging.critical(msg,*args,**kwargs) ����һ�����ؼ���ΪCRITICAL����־��¼
        logging.log(level,*args,**kwargs) ����һ�����ؼ���ΪLEVEL����־��¼
        logging.basicConfig(**kwargs) ��root logger����һ��������
'''
'''
logging.basicConfig(**kwargs)     ��root logger����һ��������
    - ֻ�ڵ�һ�ε��õ�ʱ��������
    - ������logger��ʹ��Ĭ��ֵ
    - ���  sys.stderr
    - ���� WARNING
    - ��ʽ��lever:log_name:content

loggingģ�鳣��format��ʽ˵��
    %(levelno)s: ��ӡ��־�������ֵ
    %(levelname)s: ��ӡ��־��������
    %(pathname)s: ��ӡ��ǰִ�г����·������ʵ����sys.argv[0]
    %(filename)s: ��ӡ��ǰִ�г�����
    %(funcName)s: ��ӡ��־�ĵ�ǰ����
    %(lineno)d: ��ӡ��־�ĵ�ǰ�к�
    %(asctime)s: ��ӡ��־��ʱ��
    %(thread)d: ��ӡ�߳�ID
    %(threadName)s: ��ӡ�߳�����
    %(process)d: ��ӡ����ID
    %(message)s: ��ӡ��־��Ϣ

ԭ�����ӣ�https://blog.csdn.net/orca123456/article/details/84864785


'''

import logging

LOG_FORMAT = "%(asctime)s=========%(levelname)s+++++++++++%(message)s-----------%(pathname)s"
logging.basicConfig(filename="TheLog.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log ")
logging.error("This is a error log")
logging.critical("This is a critical log ")



# ��һ��д��
logging.log(logging.DEBUG, "This is a DEBUG log")
logging.log(logging.INFO, "This is a INFO log")
logging.log(logging.WARNING, "This is a WARNING log")
logging.log(logging.ERROR, "This is a ERROR log")
logging.log(logging.CRITICAL, "This is a CRITICAL log")



'''
2.1 logging ģ��Ĵ�������
- �Ĵ����
    - ��־����logger��:������־��һ���ӿ�
    - ��������Handler��: �Ѳ�������־���͵���Ӧ��Ŀ�ĵ�
    - ��������Filter��������ϸ�Ŀ�����Щ��־���
    - ��ʽ����Formatter�����������Ϣ���и�ʽ��
'''





