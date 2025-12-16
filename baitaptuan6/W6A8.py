xau = list(input().split())
res = {}
for i in xau:
  if i in res:
      res[i] += 1
  else:
      res.update([(i,1)])
print(res)
