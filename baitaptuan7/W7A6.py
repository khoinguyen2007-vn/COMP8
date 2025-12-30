matrix = []
while True:
    nums = list(map(int,input().split()))
    if len(nums) == 0:
        break
    matrix.append(nums)
for a in matrix:
    for i in range(len(a)):
        print(a[i],end = " ")
