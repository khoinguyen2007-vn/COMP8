data = ["10", 25, "3.14", "python", 50, None, "100"]
ket_qua = []
for item in data:
    try:
        ket_qua.append(int(item))
    except (ValueError, TypeError):
        print(f"Cảnh báo: Bỏ qua phần tử '{item}' (Không thể chuyển đổi)")
print("Danh sách sau khi xử lý:", ket_qua)