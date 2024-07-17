
# Hybrid Inheritence :---------------------
# class a
# class b(a)
# class c(a)
# class d(b,c)

class school:
    def fun1(self):
        print("i am school class")

class teacher1(school):
    def fun2(self):
        print("I am teacher 1")

class teacher2(school):
    def fun3(self):
        school.fun1(self)  # this will return to fun1 and again continue
        print("i am teacher 2")

class student(teacher1, teacher2):
    def fun4(self):
        print("I am a student")


d=student()
d.fun1()
d.fun2()
d.fun3()
d.fun4()





