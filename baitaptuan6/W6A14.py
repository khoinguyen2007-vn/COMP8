s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
same = []
res = []
for num in s1:
    if num in s2 and num not in same:
        res.append(num)
        same.append(num)
print(res)
        
