nums = list(map(int,input().split()))
res = {}
pos,neg,zr = 0,0,0
for num in nums:
    if num > 0:
       pos += 1  
    elif num < 0:
       neg += 1
    else:
       zr += 1 
res.setdefault('positives',pos)
res.setdefault('negatives',neg)
res.setdefault('zero',zr)
print(res)
