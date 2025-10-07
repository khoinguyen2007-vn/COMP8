xau = input()
t = 0
h = 0
s = 0
for i in xau:
    if 'a' <= i <= 'z':
        t +=1
    if 'A' <= i <= 'Z':
        h +=1
    if '0' <= i <= '9':
        s +=1
print(t," ",h," ",s)
