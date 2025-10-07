n = int(input())
i = 1
k = 1
if n == 0:
    print(0)
    exit()
while i <= n:
    k *= i
    i += 1
print(k)
