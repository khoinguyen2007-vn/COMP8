while True:
    n = input().strip()
    if n == "":
        break
    else:
     if (int(n) & (int(n)-1)) == 0:
         print("true")
     else:
         print("false")
    