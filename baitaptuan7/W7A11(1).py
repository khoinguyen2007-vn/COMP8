s = input()
word = input()
res = 0
for i in range(len(s)-len(word)+1):
    if s[i:i+len(word)] == word:
        res += 1
print(res)
