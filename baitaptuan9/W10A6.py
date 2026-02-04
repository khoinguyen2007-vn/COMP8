import math
try:
    x = float(input("Nhập số x: "))
    if x < 0:
        raise ValueError
    ket_qua = math.sqrt(x)
except ValueError:
    print("So am")
else:
    print(f"{ket_qua:.2f}")
finally:
    print("Kết thúc chương trình.")