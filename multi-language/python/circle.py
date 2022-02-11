import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2.0 * math.pi * self.radius

    def summary(self):
        return ("area={area}, perimeter={perimeter}".format(area=round(self.area(),2), perimeter=round(self.perimeter(),2)))

