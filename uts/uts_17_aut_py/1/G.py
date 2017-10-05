from collections import Counter
s = input()
k = int(input())
ss = []
for i in Counter(s).most_common():
    if i[1] >= k:
        ss.append(i[0])
print(*sorted(ss))
