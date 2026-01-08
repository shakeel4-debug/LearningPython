class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed=breed
    def bark(self):
        return f"{self.name} is {self.age} years old"

my_dog=Dog("Buddy",21,"Golden Retriever")
print(my_dog.bark())
print(f"{my_dog.name} is a {my_dog.breed}")