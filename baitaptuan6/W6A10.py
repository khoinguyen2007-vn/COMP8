def find_res(nums,k):
    res = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == k:
                res.add((nums[i],nums[j]))
    fres = list(sorted(res))
    return fres
tnum = list(map(int,input().split()))
g = int(input())
print(find_res(tnum,g))
