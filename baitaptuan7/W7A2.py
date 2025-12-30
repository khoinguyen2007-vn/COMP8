def count(arr,target):
    res = 0
    for i in range(len(arr)):
        if arr[i] == target:
            res += 1
    return res
nums = list(map(int,input().split()))
x = int(input())
print(count(nums,x))