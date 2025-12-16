nums = list(map(int,input().split()))
k = int(input())
pos = -1
for num in nums:
    if num == k:
        pos = nums.index(num) + 1
        break
print(pos)
