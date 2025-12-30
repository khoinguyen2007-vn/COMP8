def max_length(nums):
    if len(nums) == 0:
        return 0
    else:
        tails = []
        for x in nums:
            left = 0
            right = len(tails) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] >= x:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if pos == -1:
                tails.append(x)
            else:
                tails[mid] = x
    return len(tails)
arr = list(map(int,input().split()))
print(max_length(arr))