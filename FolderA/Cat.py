class Cat():
    def sound(self):
        print('Cat is sounding...')
class Dog():
    def sound(self):
        print('Dog is sounding...')
def make_sound(animal):
    animal.sound()
make_sound(Cat())
make_sound(Dog())