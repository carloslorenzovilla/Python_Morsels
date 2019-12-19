from math import pi

class Circle:
    """ This class represents a circle.

    """
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return (f'Circle({self.radius})')

    @property
    def radius(self):
        return self.radius_

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError('Radius cannot be negative')
        self.radius_ = r

    @property
    def diameter(self):
        return self.radius*2


    @diameter.setter
    def diameter(self, d):
        if d < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = d/2
    
    @property
    def area(self):
        return pi*(self.radius**2)