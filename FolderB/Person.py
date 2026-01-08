class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
    def show_details(self):
        print(self.name,self.emp_id)
e=Employee("James",1)
e.show_details()
e.show_name()