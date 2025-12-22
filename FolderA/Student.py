class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def study(self,subject):
        return f"{self.name} is studying {subject}"

alice=Student("Alice","A")
bob=Student("Bob","B")

print(alice.study("Math"))
print(f"{bob.name}'s grade: {bob.grade} ")