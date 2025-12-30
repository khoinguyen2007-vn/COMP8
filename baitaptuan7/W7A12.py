words = []
copy = []
res = {}
while True:
    word = input()
    if not word:
        break
    words.append(word)
    copy.append(word)
copy.sort()
res[copy[0]] = 'A'
res[copy[1]] = 'B'
res[copy[2]] = 'C'
res[copy[3]] = 'D'
print(res[words[0]],res[words[1]],res[words[2]],res[words[3]])
