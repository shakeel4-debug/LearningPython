class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def details(self):
        print(self.name,self.color)

    def start(self):
        print("car is starting")

my_car=Car("Toyota","White")
my_car.details()
my_car.start()
new_car=Car("BMW","Black")
new_car.start()
new_car.details()