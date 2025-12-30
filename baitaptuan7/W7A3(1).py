def bubble_sort(arr):
    for i in range(len(arr)):
        swaped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaped = True
        if swaped == False:
            break
    return arr
nums = list(map(int,input().split()))
bubble_sort(nums)
print(*nums)
    