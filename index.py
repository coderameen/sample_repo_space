class Student:
    def __init__(self) :
        self.name='Zahid'
        self.address='Hassan'
        
    def disp(self):
        print(f" name :{self.name} and address :{self.address}")
        
obj=Student()
obj.disp()