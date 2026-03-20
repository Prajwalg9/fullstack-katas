class Account:
    def __init__(self,name,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #using __ before name can make it private or not accessible outside the class
        self.name=name
        self.__greet()
        
    def show_pass(self):
        print(self.__acc_pass)
        
    def __greet(self): #user will not have to greet himself we will do it 
        print("Welcome ",self.name)
    
        
    
        
a1=Account("Ram",1234,80000)
# we can not use print(a1.__acc_pass)
a1.show_pass()
        
        