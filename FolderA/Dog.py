class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        return f"{self.name} says Woofs!"

my_dog=Dog("Buddy","Golden Retriever")
print(my_dog.bark())
print(f"{my_dog.name} is a {my_dog.breed}.")