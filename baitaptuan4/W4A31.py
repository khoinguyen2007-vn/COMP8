s = input()
sum = 0
for i in s:
    if '0' <= i <= '9':
        sum += int(i)
print(sum)