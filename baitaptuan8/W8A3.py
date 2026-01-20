class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self):
        return ((self.x)**2 + (self.y)**2)**0.5
    def hor(self):
        if self.y == 0:
            return True
        return False
    def ver(self):
        if self.x == 0:
            return True
        return False
x = float(input())
y = float(input())
res = Point(x,y)
if res.hor():
    print("Nam tren truc hoanh")
else:
    print("Khong nam tren truc hoanh")
if res.ver():
    print("Nam tren truc tung")
else:
    print("Khong nam tren truc tung")
print(f'khoang cach den goc toa do {res.distance():.2f}')