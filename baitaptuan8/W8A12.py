class ComplexNumber:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def realpart(self):
        return self.a*self.c - self.b*self.d
    def imaginarypart(self):
        return self.a*self.d + self.b*self.c
x,y = list(map(int,input().split()))
z,t = list(map(int,input().split()))
cn = ComplexNumber(x,y,z,t)
print(f'{cn.realpart()} {cn.imaginarypart()}')