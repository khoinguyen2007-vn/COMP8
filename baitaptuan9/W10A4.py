def tinh_tong():
    try:
        so_1 = float(input("Nhập số thứ nhất: "))
        so_2 = float(input("Nhập số thứ hai: "))
        ket_qua = so_1 + so_2
    except ValueError:
        print("Lỗi: Dữ liệu bạn nhập không phải là số hợp lệ!")
    else:
        if ket_qua.is_integer():
            print(f"Tổng của hai số là: {int(ket_qua)}")
        else:
            print(f"Tổng của hai số là: {ket_qua}")
    finally:
        print("Kết thúc chương trình.")
if __name__ == "__main__":
    tinh_tong()