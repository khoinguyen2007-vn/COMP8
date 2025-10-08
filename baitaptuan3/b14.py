a = float(input())
b = float(input())
if a == 0 and b == 0:
    print("Vô số nghiệm")
elif a == 0 and b != 0:
    print("Vô nghiệm")
else:
    print(format(-b/a,".2f"))
