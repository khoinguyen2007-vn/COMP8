class Cylinder:
    def __init__(self,radius,height):
        self.r = radius
        self.h = height
        self.pi = 3.14
    def area(self):
        return 2 * self.pi * self.r * (self.h + self.r)
    def vol(self):
        return self.pi * self.r * self.r * self.h
r = float(input())
h = float(input())
cyl = Cylinder(r,h)
print(f'{cyl.area():.2f}')
print(f'{cyl.vol():.2f}')