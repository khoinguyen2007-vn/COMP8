num = []
numbers = list(map(int,input().split()))
for i in numbers:
    if i not in num:
        num.append(i)
print(num)
