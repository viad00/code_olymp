n, NAVALNIY = list(map(int, input().split()))
VSTRECHAS = []
for i in range(n):
    VSTRECHAS.append(list(map(int, input().split())))
n = 1
for vst in VSTRECHAS:
    vst.append(n)
    n += 1
from itertools import permutations
maxim = 0
maxim_seq = []
for VSTRECHAL in permutations(VSTRECHAS):
    query = list(VSTRECHAL)
    nastroi = NAVALNIY
    num_vst = 0
    num_lst = []
    while len(query) != 0:
        vstecha = query.pop()
        if vstecha[0] <= nastroi <= vstecha[1]:
            nastroi += vstecha[2]
            num_vst += 1
            num_lst.append(vstecha[3])
        else:
            break
    if num_vst > maxim:
        maxim = num_vst
        maxim_seq = num_lst
        if maxim == n:
            break
ans = []
print(maxim)
for i in maxim_seq:
    print(i, end=' ')
