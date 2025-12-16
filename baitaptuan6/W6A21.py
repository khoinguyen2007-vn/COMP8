x = list(input().split())
res = {}
for i in range(len(x)):
   res.setdefault(x[i],[]).append(i)
print(res)
