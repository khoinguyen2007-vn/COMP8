def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        res = arr[mid]
        if res == target:
            return mid
        elif res < target:
            left = mid + 1
        elif res > target:
            right = mid - 1
    return -1
nums = list(map(int,input().split()))
num = int(input())
print(binary_search(nums,num))