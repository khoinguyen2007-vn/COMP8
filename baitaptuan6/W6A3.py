nums = tuple(map(int,input().split()))
k = int(input())
k = k % len(nums)
res = nums[k:] + nums[:k]
print(res)
