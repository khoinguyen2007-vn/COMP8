n, m, k = map(int, input("Nhập n, m, k: ").split())
print(f"Nhập {n} dòng ma trận:")
matrix = [list(map(int, input().split())) for _ in range(n)]
if 0 <= k < m:
    tong_cot = sum(row[k] for row in matrix)
    print(f"Tổng các phần tử trên cột {k}: {tong_cot}")
else:

    print(f"Lỗi: Chỉ số cột k={k} không hợp lệ (phải từ 0 đến {m-1})")
