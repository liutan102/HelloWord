
class Person():
    name = "NoName"
    age = 0
    print("Sleepint.....")

# 父类写在括号内
class Teacher(Person):
    shengao = 180
    def make_test(self):
        pass


t = Teacher()
print(t.name)
print(t.age)

# 继承 中 公用 受保护的 私有的 变量案例
class Person1():
    name = "NoName"
    age = 18
    __score = 0 # 私有的 用连个下划线表示
    _petname = "小白"# 小名 是受保护的
    def sleep(self):
        print("Sleepint.....")

# 父类写在括号内
class Teacher1(Person1):
    teacher_id = "9978"
    name = "heiha" # 当子类中和父类中有相同的 名称变量 那么优先用子类的
    shengao = 180
    def make_test(self):
        pass


t = Teacher1()
print(t.name)
# 小名 也就是 _petname 直接打印是可以的但是不能通过" . "出来
print(t._petname)
#print(t.__score)
t.sleep()
print(t.teacher_id)
print(t.name)

# 子类扩充父类功能的案例
# 人由工作的函数，老师也有工作的函数，但老实的工作需要讲课


class Person2():
    name = "NoName"
    age = 18
    __score = 0 # 私有的 用连个下划线表示
    _petname = "小白"# 小名 是受保护的
    def sleep(self):
        print("Sleepint.....")

    def work(self):
        print("make some money")


# 父类写在括号内
class Teacher2(Person2):
    teacher_id = "9978"
    name = "heiha" # 当子类中和父类中有相同的 名称变量 那么优先用子类的
    shengao = 180
    def make_test(self):
        print("attention")


    def work(self):
        # 扩充父类的功能只需要调用相同的函数就可以了
        # super().work() 和 Person2.wotk(self) 是一样的
       # super().work()
        Person2.wotk(self)
        self.make_test()

t = Teacher2()
t.work()
