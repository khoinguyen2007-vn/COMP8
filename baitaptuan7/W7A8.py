interval = []
while True:
    cp = list(map(int,input().split()))
    if not cp:
        break
    interval.append(cp)
nums = list(map(int,input().split()))
res = []
for num in nums:
    count = float('inf')
    for i in range(len(interval)):
        if interval[i][0] <= num <= interval[i][1]:
            count = min(count,interval[i][1]-interval[i][0]+1)
    if count == float('inf'):
        res.append(1)
    else:
        res.append(count)
print(*res)
        
