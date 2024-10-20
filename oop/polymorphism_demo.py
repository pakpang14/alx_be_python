import math
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__(self)
        self.length = length
        self.width = width
        area = length * width
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(self)
        self.radius = radius
        area = (math.pi)*radius**2

        for area in Shape:
            if isinstance(self.length,self.width):
                print("The area of the Rectangle is: {area}")
            else:
                print("The area of the Circle is: {area}")