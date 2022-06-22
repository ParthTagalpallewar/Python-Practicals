from math import sqrt

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c1, c2):
        temp = complex(c1.real + c2.real, c1.imag + c2.imag)
        temp = c1.real + c2.real
        temp = c1.imag + c2.imag
        return temp

    def __sub__(self, c1, c2):
        temp = complex(c1.real - c2.real, c1.imag - c2.imag)
        temp = c1.real - c2.real
        temp = c1.imag - c2.imag
        return temp

if __name__ == "__main__":
    c1 = complex(1, 2)
    c2 = complex(3, 4)

    print("Addition: ", c1 + c2)
    print("Subtraction: ", c1 - c2)

    
