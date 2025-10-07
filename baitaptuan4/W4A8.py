def check(x):
    for i in range(int(len(x)/2)+1):
        if x[i] != x[len(x)-1-i]:
            return False
    return True
def reverse(y):
    s = ""
    for z in range(len(y)-1,-1,-1):
        s += y[z]
    return s
n = int(input())
dem = 0
while check(str(n)) == False:
    n += int(reverse(str(n)))
    dem += 1
print(dem," ",n)