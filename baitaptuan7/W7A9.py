nums = list(map(int,input().split()))
res = []
for i in range(len(nums)):
    count = 0
    for j in range(i+1,len(nums)):
        if nums[j] < nums[i]:
            count += 1
    res.append(count)
print(res)