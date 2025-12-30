def cnt(arr, x):
    res = 0
    seen = {}  
    for num in arr:
        num_find = x - num  
        if num_find in seen:
            res += seen[num_find]
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    return res
nums = list(map(int, input().split()))
target = int(input())
print(cnt(nums, target))