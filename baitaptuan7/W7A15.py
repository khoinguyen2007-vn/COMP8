n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)
for i in range(n):
    if names[i] == "Nemo":
        if i == n:
            print(f"{names[n-2]} and {names[0]}")
        elif i == 0:
            print(f"{names[1]} and {names[n-1]}")
        else:
            print(f"{names[i-1]} and {names[i+1]}")
        break

