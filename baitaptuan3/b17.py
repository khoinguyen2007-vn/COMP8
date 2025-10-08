a,b,c = map(int,input().split())
if (a + b > c) and (b + c > a) and (c + a > b) and (a>0) and (b>0) and (c>0):
    if a == b == c:
        print("tam giác đều")
    elif  a == b or b == c or c == a:
        print("tam giác cân")
    elif  a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("tam giác vuông")
    else: 
     print("tam giác thường")
else:
    print("không phải tam giác")
