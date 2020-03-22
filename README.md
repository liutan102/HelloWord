# helloWord
Python练习项目


- 实例化类
    变量 = 类名（）# 实例化了一个对象
- 访问对象成员
    - 使用点操作符
        
            ojb.成员属性名称
            obj.成员方法
            
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
    
            # dict前后各有两个下划线
            obj.__dict__
    - 类所有成员
            # dict前后各有两个下划线
            class_name.__dict__

# 3 anaconda基本使用

- anaconda 主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list:显示anaconda安装的包
- conda evn list:显示anaconda虚拟环境列表
- conda create -n xxx(环境名称) python=3.6：创建python版本为3.6的虚拟环境 名称为xxx