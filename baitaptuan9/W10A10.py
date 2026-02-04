try:
    n = int(input("Nhập N (N > 0): "))
    if n <= 0:
        raise ValueError  
    day_so = input(f"Nhập {n} số nguyên dương (cách nhau bởi dấu cách): ").split()
    mang = [int(x) for x in day_so]
    if len(mang) != n or any(x <= 0 for x in mang) or len(set(mang)) != n:
        raise ValueError
except ValueError:
    print("Mang khong hop le")
else:
    print(sum(mang))
finally:
    print("Kết thúc chương trình.")