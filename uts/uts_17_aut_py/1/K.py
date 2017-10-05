ser = int(input())
mas = list(map(int, input().split()))
from collections import Counter
cer = Counter(mas).most_common()
for i in cer:
    if i[1] == 1:
        print(i[0])
        break
