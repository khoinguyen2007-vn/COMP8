try:
    n = int(input())
    nums = list(map(int,input().split()))
    x = int(input())
    print(nums[x])
except:
    print("Error: Index out of range")
    
