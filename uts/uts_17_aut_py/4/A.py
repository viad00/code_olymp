n, k, x = list(map(int, input().split()))
from itertools import combinations_with_replacement
cnt = 0
for i in combinations_with_replacement(range(1, n+1), k):
    if cnt == x:
        for j in i:
            print(j, end=' ')
        break
    cnt += 1
