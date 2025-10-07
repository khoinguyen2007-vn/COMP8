s = input()
xau = ''
for i in range(len(s)):
    if s[i] != ' ':
        xau +=s[i]
    else:
        break
print(xau)