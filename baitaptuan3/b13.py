n = int(input())
if n <= 50:
    print(n*1500)
if 50 < n <= 100:
    print(50*1500 + (n-50)*2000)
if n > 100:
    print(50*1500 + 50*2000 + (n-100)*3000)