numbers = []
n=int(input())
for i in range(n):
    numbers.append(int(input()))
for x in numbers:
    if x % 2 == 0:
        print('even')
    else:
        print('odd')