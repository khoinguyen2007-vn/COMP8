try:
    tuoi = int(input("Nhập tuổi của bạn: "))
    if tuoi < 0:
        raise ValueError
except ValueError:
    print("Tuoi khong hop le")
else:
    nam_sinh = 2025 - tuoi
    print(nam_sinh)
finally:
    print("Kết thúc chương trình.")