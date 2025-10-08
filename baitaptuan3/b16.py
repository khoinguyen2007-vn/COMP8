n = float(input())
if (n > int(format(n, '.0f'))):
    print(int(format(n, '.0f')) + 1,int(format(n, '.0f')), int(format(n, '.0f')) )
if (n < int(format(n, '.0f'))):
    print(int(format(n, '.0f')),int(format(n, '.0f')) - 1,int(format(n, '.0f')) - 1 )
if (n == int(format(n, '.0f'))):
    print(int(format(n, '.0f')),int(format(n, '.0f')) ,int(format(n, '.0f')) )