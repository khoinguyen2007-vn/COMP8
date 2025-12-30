n = int(input())
nums = list(map(int,input().split()))
res = []
for i in range(len(nums)):
    if nums[i] == 7:
        res.append(i)
if len(res) == 0:
    print("Not Found")
else:
    for i in range(len(res)-1,-1,-1):
        print(res[i],end = " ")
