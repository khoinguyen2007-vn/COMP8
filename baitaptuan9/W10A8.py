try:
    ten_file = input("Nhập tên file: ").strip().lower()
    if not (ten_file.endswith(".txt") or ten_file.endswith(".zip")):
        raise ValueError
except ValueError:
    print("File khong hop le")
else:
    print("Doc file thanh cong")
finally:
    print("Kết thúc chương trình.")