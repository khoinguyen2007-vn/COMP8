even = 0
odd = 0
n = int(input())
while n > 0:
    res = n % 10
    if res % 2 == 0:
        even += 1       
    else:
        odd += 1    
    n = n // 10
print("Even:", even)
print("Odd:", odd)