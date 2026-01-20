def gcd(x,y):
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x
def scm(n1,n2):
    return n1 * n2 // gcd(n1,n2)
class Fraction:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def add(self):
        tmp1 = self.a * (scm(self.b,self.d) // self.b) + self.c * (scm(self.b,self.d) // self.d)
        tmp2 = scm(self.b,self.d)
        return f'{tmp1 // gcd(tmp1,tmp2)} / {tmp2 // gcd(tmp1,tmp2)}'
    def sub(self):
        tmp1 = self.a * (scm(self.b,self.d) // self.b) - self.c * (scm(self.b,self.d) // self.d)
        tmp2 = scm(self.b,self.d)
        return f'{tmp1 // gcd(tmp1,tmp2)} / {tmp2 // gcd(tmp1,tmp2)}'
    def div(self):
        tmp1 = self.a * self.d
        tmp2 = self.b * self.c
        return f'{tmp1 // gcd(tmp1,tmp2)} / {tmp2 // gcd(tmp1,tmp2)}'
    def mul(self):
        tmp1 = self.a * self.c
        tmp2 = self.b * self.d
        return f'{tmp1 // gcd(tmp1,tmp2)} / {tmp2 // gcd(tmp1,tmp2)}'
line = input().split()
a = int(line[0])
b = int(line[1])
op = line[2]
c = int(line[3])
d = int(line[4])
fra = Fraction(a,b,c,d)
if op == '+':
    print(fra.add())
elif op == '-':
    print(fra.sub())
elif op == '/':
    print(fra.div())
elif op == '*':
    print(fra.mul())
