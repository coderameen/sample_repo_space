class Student:
    def __init__(self) :
        self.name='Zahid'
        self.address='Hassan'
        
    def disp(self):
        print(f" name :{self.name} and address :{self.address}")
        
    def add_extra_future_ameen(self):
        print("added feature by ameen hasan")
        
obj=Student()
obj.disp()
obj.add_extra_future_ameen()