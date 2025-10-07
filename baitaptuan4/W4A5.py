n = int(input())
numbers = map(int, input().split())
for x in numbers:
    if x == 42:
        print("I've found the meaning of life!")
        exit()
    else:
        continue
print("It's a joke!")