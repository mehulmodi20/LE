import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.real + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.real - no.imaginary)
        
    def __mul__(self, no):
        real = self.real*no.real - self.imaginary*no.imaginary
        imaginary = self.real*no.imaginary + self.imaginary*no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        try: 
            return self.__mul__(Complex(no.real, -1*no.imaginary)).__mul__(Complex(1.0/(no.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None

    def mod(self):
        return Complex(pow(self.real**2+self.imaginary**2, 0.5), 0)


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    # c = map(float, input().split())
    # d = map(float, input().split())
    c = [2.0, 1.0]
    d = [5.0, 6.0]
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')