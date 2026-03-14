class Person:
    name = "anoymous"
    # We can access this name using 
    
    def __init__(self):
        self.show_name()
        self.show_name_with_decorator()
        
    
    def show_name(self):
        print(self.__class__.name)
        
    # or 
    
    @classmethod
    def show_name_with_decorator(cls):
        print(cls.name)
        
p1=Person()