class Rectangle:
    def __init__(self,w,h,k):
        self.w = w
        self.h = h
        self.k = k
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
    def scale(self):
        self.w = self.k * self.w
        self.h = self.k * self.h
x,y,z = list(map(float,input().split()))
res = Rectangle(x,y,z)
res.scale()
print(f'{res.area():.2f}',f'{res.perimeter():.2f}')