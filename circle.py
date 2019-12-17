from math import pi

class Circle:
    def __init__(self, r=1):
        self.radius_ = r

    def __str__(self):
        return (f'Circle({self.radius_})')

    def __repr__(self):
        return (f'Circle({self.radius_})')

    @property
    def radius(self):
        return self.radius_
    
    @property
    def area(self):
        return pi*(self.radius_**2)

    @property
    def diameter(self):
        return self.radius_*2

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError('Radius cannot be negative')
        self.radius_ = r

    @diameter.setter
    def diameter(self, d):
        if d < 0:
            raise ValueError('Radius cannot be negative')
        self.radius_ = d/2
    
    

