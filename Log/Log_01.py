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