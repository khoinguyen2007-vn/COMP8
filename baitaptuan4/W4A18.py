def gcd(a,b):
    while b != 0:
        a, b = b, a % b 
    return a
c,d = map(int, input().split())
for i in range(1, gcd(c,d)+1):
    if gcd(c,d) % i == 0:
        print(i,end=' ')