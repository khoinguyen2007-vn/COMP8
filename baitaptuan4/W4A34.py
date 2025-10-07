a = input()
b = input()
pos = a.find(b)
a = a[:pos] + a[pos+len(b):]
if a[0] == ' ':
    a = a[1:]
print(a)