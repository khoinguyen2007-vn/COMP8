while True:
    n = input()
    if n=="":
        break
    if int(n) % 400 == 0 or (int(n) % 4 == 0 and int(n) % 100 != 0):
        print("Yes")
    else:
        print("No")