class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height

rect=Rectangle(10,10)
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")

rect.width=7
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")