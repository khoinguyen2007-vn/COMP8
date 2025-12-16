from collections import Counter
def add(dict1,dict2):
    res = Counter(dict1) + Counter(dict2)
    return res
d1 = {'a': 1, 'b': 2}
d2 = {'a': 2}
kq = add(d1,d2)
print(dict(sorted(kq.items())))
