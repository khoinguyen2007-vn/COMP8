def GCD(c,d):
    while d != 0:
        c,d = d, c%d
    return c
a,b = map(int,input().split())
print(GCD(a,b))
