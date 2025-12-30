def count(arr):
    cnt = {}
    for x in arr:
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
    res = 0
    num = 0
    for key,value in cnt.items():
        if value > res:
            num = key
            res = value
    print(f"{num} xuat hien nhieu nhat, som nhat, {res} lan")
nums = list(map(int,input().split()))
count(nums)


        