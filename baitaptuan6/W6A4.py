items = input().split()
res = {}
for i in items:
    k,v = i.split(':')
    res.setdefault(k,[]).append(v)
print(res)
