import sys
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):                              #should pass self, self.number1 and self.number2
        sum = int(self.number1) + int(self.number2)
        print(sum)
    def subtract(self):
        sum = int(self.number1) - int(self.number2)
        print(sum)
    def multiply(self):
        sum = int(self.number1) * int(self.number2)
        print(sum)


my_calc = Calculator(sys.argv[1], sys.argv[2])
my_calc.add()
my_calc.subtract()
my_calc.multiply()