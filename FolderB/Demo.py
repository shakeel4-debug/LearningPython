# class Demo:
#     def __new__(self):
#         print("__new__")
#         return super().__new__(self)
#     def __init__(self):
#         print("__init__")
# demo=Demo()

# class Parent:
#     def __init__(self):
#         print("Parent constructor")
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")
# c=Child()


class Student:
    def __init__(self,age,name="Visitor"):
        self.name=name
        self.age=age
s=Student("John",18)
print(s.name,s.age)
guest=Student(10)
print(guest.name,guest.age)