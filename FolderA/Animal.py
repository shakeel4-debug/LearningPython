class Animal:
    def sound(self):
        print('Animal is sounding...')
class Dog(Animal):
    def sound(self):
        print('Dog is sounding...')

d=Dog()
d.sound()