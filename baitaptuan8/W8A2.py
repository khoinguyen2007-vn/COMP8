def cnn(x):
    if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
        return True
    return False
class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def check(self):
        if self.day <= 0 or self.month <= 0 or self.year <= 0 or self.month > 12:
            return "INVALID"
        if cnn(self.year):
            if self.month == 2 and self.day > 29:
                return "INVALID"
        elif self.month == 2 and self.day > 28:
            return "INVALID"
        if self.month in [1,3,5,7,8,10,12] and self.day > 31:
            return "INVALID"
        if self.month in [4,6,9,11] and self.day > 30:
            return "INVALID"
        return "VALID"
    def nextday(self):
        if self.month == 12 and self.day == 31:
            print(f'day:{1} month:{1} year:{self.year + 1}')
        elif self.month in [1,3,5,7,8,10] and self.day == 31:
            print(f'day:{1} month:{self.month + 1} year:{self.year}')
        elif self.month in [4,6,9,11] and self.day == 30:
            print(f'day:{1} month:{self.month + 1} year:{self.year}')
        elif self.month == 2 and self.day == 29 and cnn(self.year):
            print(f'day:{1} month:{self.month + 1} year:{self.year}')
        elif self.month == 2 and self.day == 28 and not cnn(self.year):
            print(f'day:{1} month:{self.month + 1} year:{self.year}')
        else:
            print(f'day:{self.day + 1} month:{self.month} year:{self.year}')
d,m,y = list(map(int,input().split()))
date = Date(d,m,y)
if date.check() == "VALID":
    date.nextday()
else:
    print(date.check())
        
        
            