def xu_ly_ma_tran():
        n = int(input("Nhập số hàng n: "))
        m = int(input("Nhập số cột m: "))
        matrix = []
        for i in range(n):
            while True:
                dong_str = input(f"Hàng {i+1}: ")
                row = [int(x) for x in dong_str.split()]
                if len(row) == m:
                    matrix.append(row)
                    break 
        for i in range(n):
            for j in range(m):
                print(f"{matrix[i][j]:>4}",end = " ")
            print() 
xu_ly_ma_tran()
