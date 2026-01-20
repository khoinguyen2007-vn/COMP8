class Triangle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def check(self):
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            return False
        if (self.x + self.y > self.z) and (self.x + self.z > self.y) and (self.y + self.z > self.x):
            return True
        return False
    def area(self):
        p = (self.x + self.y + self.z)/2
        return (p*(p - self.x)*(p - self.y)*(p - self.z))**0.5
while True:
    x,y,z = list(map(float,input().split()))
    temp = Triangle(x,y,z)
    if temp.check() == False:
        print("invalid")
    else:
        print(f'{temp.area():.2f}')
    if not input:
        break
    
    
    