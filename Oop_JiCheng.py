
class Person():
    name = "NoName"
    age = 0
    print("Sleepint.....")

# 父类卸写在括号内
class Teacher(Person):
    pass

t = Teacher()
print(t.name)
print(t.age)