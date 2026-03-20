class Car:
    def __init__(self):
        self.type = "type"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class Toyota(Car):
    def __init__(self):
        self.name = self.__class__.__name__
        super().__init__()      # initialize parent
        self.type = "car"       # override type


t1 = Toyota()
print(t1.name, "\n", t1.type)
