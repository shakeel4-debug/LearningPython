class A:
    def __init__(self):
        self.public=1
        self._protected=2
        self.__private=3
class B(A):
    def show(self):
        print(self.public)
        print(self._protected)
       # print(self.__private)
b=B()
b.show()
