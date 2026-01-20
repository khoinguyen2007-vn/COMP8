class ShoppingCart:
    def __init__(self):
        self.sc = {}
    def add(self,name,price):
        self.sc[name] = price
    def delete(self,name):
        if len(self.sc) == 0:
            print("Không có sản phẩm")
            return
        if name not in self.sc:
            print("không tồn tại sản phẩm")
            return
        del self.sc[name]
    def check(self):
        if len(self.sc) == 0:
            return "Giỏ hàng bị rỗng"
        return "Giỏ hàng không rỗng"
    def cost(self):
        res = 0
        for k,v in self.sc.items():
            res += v
        return f'Giá trị giỏ hàng là {res}'
    def show(self):
        for key,value in self.sc.items():
            print(key,value)
    def delall(self):
        self.sc.clear()
sp = ShoppingCart()
while True:
    print("----Menu----")
    print("1.Thêm sản phẩm")
    print("2.Xóa sản phẩm")
    print("3.Kiểm tra giỏ hàng")
    print("4.Tính tiền giỏ hàng")
    print("5.Hiển thị giỏ hàng")
    print("6.Xóa giỏ hàng")
    choice = input("Chọn số: ")
    if choice == '1':
        n = input()
        p = float(input())
        sp.add(n,p)
    elif choice == '2':
        n = input()
        sp.delete(n)
    elif choice == '3':
        print(sp.check())
    elif choice == '4':
        print(sp.cost())
    elif choice == '5':
        sp.show()
    else:
        sp.delall()
    exit_check = input('Bạn có muốn thoát không? ')
    if exit_check in ['Có','có','CÓ']:
        print("Đã thoát khỏi chương trình")
        break




    

        