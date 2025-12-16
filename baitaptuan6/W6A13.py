def reverse(x):
    res = {}
    for key,value in x.items():
        res[value] = key
    return res
s = list(input().split())
d = {}
for i in range(0,len(s),2):
   d[s[i]] = s[i+1] 
print(reverse(d))
