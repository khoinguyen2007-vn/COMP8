s = input()
x = 0
y = 0
z = 0
t = 0
if len(s) < 6:
    print("No")
else:
    for i in s:
        if ('a' <= i <= 'z'):
            x += 1
        elif ('A' <= i <= 'Z'):
            y += 1  
        elif ('0' <= i <= '9'):
            z += 1  
        else:
            t += 1
    if x > 0 and y > 0 and z > 0 and t > 0:
        print("Yes")    
    else:
        print("No")
