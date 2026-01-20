class Caculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def product(self):
        return self.x * self.y
    def power(self):
        return self.x ** self.y
    def divide(self):
        if self.y == 0:
            return "Error"
        return self.x / self.y
    def modnumber(self):
        if self.y == 0:
            return "Error"
        return self.x % self.y
    def set_numbers(self):
        self.x = float(input())
        self.y = float(input())
x = float(input())
y = float(input())
calc = Caculator(x,y)
while True:
    print("---MENU CHỨC NĂNG---")
    print("1. phép cộng")
    print("2. phép trừ")
    print("3. phép nhân")
    print("4. phép chia")
    print("5. phép lũy thừa")
    print("6. phép chia lấy dư")
    print("7. chọn 2 số mới")
    choice = input("Chọn số: ")
    if choice == '1':
        print(f'{x} + {y} = {calc.add()}')
    elif choice == '2':
        print(f'{x} - {y} = {calc.subtract()}')
    elif choice == '3':
        print(f'{x} * {y} = {calc.product()}')
    elif choice == '4':
        print(f'{x} : {y} = {calc.divide()}')
    elif choice == '5':
        print(f'{x}^{y} = {calc.power()}')
    elif choice == '6':
        print(f'{x} % {y} = {calc.modnumber()}')
    elif choice == '7':
        calc.set_numbers()
    else:
        print("Lựa chọn không hợp lệ")
    exit_check = input("Chọn yes nếu muốn thoát ")
    if exit_check in ["yes","Yes","YES"]:
        print("Đã thoát chương trình")
        break
    
