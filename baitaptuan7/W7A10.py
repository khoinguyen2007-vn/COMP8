nums = list(map(int,input().split()))
m = int(input())
dp = {0}
for num in nums:
    temp = set()
    for r in dp:
        temp.add((r+num)%m)
    dp.update(temp)
print(dp)
print(max(dp))