class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        self.show_num()
        
    def show_num(self):
        print(self.real,"i + ",self.img,"j")
        
    def __add__(self,num2):
        new_real=self.real+num2.real
        new_img=self.img+num2.img
        return Complex(new_real,new_img)

num1=Complex(6,3)
num2=Complex(2,4)
num3=num1+num2