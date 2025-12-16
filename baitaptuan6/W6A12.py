nums = list(map(int,input().split()))
res = 0
count = 1
max = 0
nums.sort()
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        count += 1
    else:
        if count > max:
            max = count
            res = nums[i]
        count = 1
if count > max:
    res = nums[len(nums)-1]
print(res)
