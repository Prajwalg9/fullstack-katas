class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def display(self):
        if self.imaginary>= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {abs(self.imaginary)}i")

    def add(self,other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def sub(self,other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def mul(self,other):
        real=self.real * other.real - self.imaginary * other.imaginary
        imaginary=self.imaginary * other.real + self.real * other.imaginary
        return Complex(real, imaginary)

    def div(self,other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real, imag)


c1 = Complex(3, 4)
c2 = Complex(1, 2)

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("Addition:")
c1.add(c2).display()

print("Subtraction:")
c1.sub(c2).display()

print("Multiplication:")
c1.mul(c2).display()

print("Division:")
c1.div(c2).display()