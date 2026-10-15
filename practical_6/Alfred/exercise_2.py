import sys
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calc_perimeter(self):           #2PI*r
        circ = 2 * math.pi * int(self.radius)
        print("circumference is ", str(circ))
    def calc_area(self):                #2r^2
        area =  math.pi * (int(self.radius)) ** 2
        print("area is ", str(area))



circle1 = Circle(sys.argv[1])
circle1.calc_area()
circle1.calc_perimeter()
