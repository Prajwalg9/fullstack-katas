class Employee:                           # define a blueprint for employees
    company_name = "Tech Corp"            # class attribute: shared by ALL employees

    def __init__(self, name, salary):     # runs when we create a new Employee
        self.name = name                  # instance attribute: specific to one employee
        self.salary = salary              # instance attribute: specific to one employee

    def get_info(self):                   # method that READS data (like a getter)
        return f"{self.name} works at {self.company_name} with salary {self.salary}"

    def give_raise(self, amount):         # method that CHANGES data
        self.salary += amount             # update this employee's salary

# create two different Employee objects
emp1 = Employee("Alice", 50000)           # emp1 has its own name and salary
emp2 = Employee("Bob", 60000)             # emp2 has its own name and salary

print(emp1.get_info())                    # uses emp1's data + shared company_name
print(emp2.get_info())                    # uses emp2's data + shared company_name

emp1.give_raise(5000)                     # change ONLY emp1's salary
print(emp1.get_info())                    # salary changed for emp1
print(emp2.get_info())                    # emp2 salary unchanged
