try:
    chuoi_nhap = input("Nhập chuỗi cần chuyển: ")
    so_nguyen = int(chuoi_nhap)
except ValueError:
    print("Chuoi khong hop le")
else:
    print(so_nguyen)
finally:
    print("Kết thúc chương trình.")