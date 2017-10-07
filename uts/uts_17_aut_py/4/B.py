n, k = list(map(int, input().split()))
find = tuple(map(int, input().split()))
from itertools import combinations_with_replacement
cnt = 0
for i in combinations_with_replacement(range(1, n+1), k):
    if i == find:
        print(cnt)
        break
    cnt += 1
