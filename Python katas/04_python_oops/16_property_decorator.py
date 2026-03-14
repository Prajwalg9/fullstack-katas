import math
class Student:
    def __init__(self,phy:int,chem:int,math:int):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    @property
    def percentage(self):
        return (str(math.floor((self.phy+self.chem+self.math)/3))+"%")
    
s1=Student(12,33,44)
print(s1.percentage)
        