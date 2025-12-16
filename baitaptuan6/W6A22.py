nums = list(map(int,input().split()))
res = 0
max = nums[0]
for i in range(1,len(nums)):
    if nums[i] > max:
        max = nums[i]
        res = i + 1
print(res)
