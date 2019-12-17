from math import pi

class Circle:
    def __init__(self, r=1):
        self.radius = r

    def __str__(self):
        return (f'Circle({self.radius})')

    def __repr__(self):
        return (f'Circle({self.radius})')
    
    @property
    def area(self):
        return pi*(self.radius**2)

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, d):
        self.radius = d/2

    

