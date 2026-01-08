class House:
    def __init__(self,color,doors):
        self.color = color
        self.doors = doors

    def describe(self):
        print(f"This is a {self.color} house with {self.doors} doors.")

my_house = House("Blue",4)
new_house = House("Red",2)
my_house.describe()
new_house.describe()

class Mansion(House):
    def __init__(self,color,doors,has_pool):
        super().__init__(color,doors)
        self.has_pool = has_pool
big_mansion=Mansion("White",20,True)
big_mansion.describe()