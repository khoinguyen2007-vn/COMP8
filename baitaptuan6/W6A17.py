n = int(input("Nhập kích thước n: "))
a = [list(map(int, input().split())) for _ in range(n)]
cheo_chinh = [a[i][i] for i in range(n)]
cheo_phu = [a[i][n - 1 - i] for i in range(n)]
print(f"Đường chéo chính: {cheo_chinh}")
print(f"Đường chéo phụ:   {cheo_phu}")
