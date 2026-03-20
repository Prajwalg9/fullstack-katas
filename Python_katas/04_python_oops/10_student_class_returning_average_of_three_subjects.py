class Student:
    def __init__(self):
        self.name=input("Enter the name of the student: ")
        self.marks1=int(input("Enter the marks of subject 1: "))
        self.marks2=int(input("Enter the marks of subject 2: "))
        self.marks3=int(input("Enter the marks of subject 3: "))
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("The average marks of the student is: ",avg)
        
s1=Student()

    