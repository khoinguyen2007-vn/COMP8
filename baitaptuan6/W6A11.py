nums = list(map(int,input().split()))
odd = ()
even = ()
for num in nums:
    if num % 2 == 0:
        even += (num,)
    else:
        odd += (num,)
print(even)
print(odd)
        
