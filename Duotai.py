# 三大特性 之---多态

class Person():
    name = "liuying"
    age = 18
    def eat(self):
        print("EAT......")

    def drink(self):
        print("DRINK........")

    def sleep(self):
        print("SLEEP......")


class Teacher (Person):
    def work(self):
        print("Worl")

class Student(Person):
    def study(self):
        print("Study")

class Tutor(Teacher,Student):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)
print("*"*200)

class TeacherMixin():
    def work(self):
        print("Work")

class StudentMixin():
    def Study(self):
        print("study")

class TutorMixin(Person,TeacherMixin,StudentMixin):
    pass
tt = TutorMixin()
print(TutorMixin.__mro__)
print(t.__dict__)
print((TutorMixin.__dict__))


# 类相关函数
class A():
    pass

class B(A):
    pass
print(issubclass(B,A))
print(issubclass(A,B))
print(issubclass(A,object))

# isinstance 相关函数
class A1():
    pass
a = A1()
print(isinstance(a,A1))
print(isinstance(A1,A1))


# hasattr 函数
class A2():
    name = ""

aa = A2()
print(hasattr(aa,"name"))
print(hasattr(aa,"age"))

help(setattr)
print(getattr(aa,"name"))

# dir
print(dir(A2))