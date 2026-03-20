class Student:
    school_name = "ABC School"          # class attribute (shared by all students)

    def __init__(self, name, marks):
        self.name = name                # instance attribute (per object)
        self.marks = marks              # instance attribute (per object)

    # 1) INSTANCE METHOD
    def show_details(self):             # uses self
        return f"{self.name} has {self.marks} marks in {self.school_name}"

    # 2) CLASS METHOD
    @classmethod
    def change_school(cls, new_name):   # uses cls (class, not object)
        cls.school_name = new_name      # change shared school_name for ALL students

    # 3) STATIC METHOD
    @staticmethod
    def is_pass(marks):                 # no self, no cls
        return marks >= 40              # simple utility logic


# create two students (objects)
s1 = Student("Alice", 85)
s2 = Student("Bob", 35)

# instance method: called on object, works with that object's data
print(s1.show_details())
print(s2.show_details())

# static method: utility; can be called via class or object
print(Student.is_pass(s1.marks))        # True
print(Student.is_pass(s2.marks))        # False

# class method: change class-level data for ALL
Student.change_school("XYZ School")

# now both students see new school name
print(s1.show_details())
print(s2.show_details())
