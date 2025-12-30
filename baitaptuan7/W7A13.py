nums = list(map(int,input().split()))
res = 0
nums.sort()
left = 0
for right in range(len(nums)):
    while nums[right] - nums[left] > 1:
        left += 1
    if nums[right] - nums[left] == 1:
        res = max(res,right-left+1)
print(res)