s = list(input().split())
k = int(input())
res = {}
for i in range(0,len(s),2):
    if int(s[i+1]) > k:
        res[s[i]] = s[i+1]
print(res)
