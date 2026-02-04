import re
try:
    t = int(input("Nhập số lượng testcase: "))
    for _ in range(t):
        s = input()
        try:
            re.compile(s)
        except re.error:
            print("Invalid")
        else:
            print("Valid")
except ValueError:
    print("So luong testcase khong hop le")
finally:
    print("Kết thúc chương trình.")