n = int(input())
s = ""
dem = 0
xau = str(n)
for i in xau:
    dem += 1
    if dem % 3 == 0 and dem != len(xau):
        s += i + "."
    else:
        s += i
print(s)