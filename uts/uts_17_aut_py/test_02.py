import sys
from itertools import permutations


def x(a,b,c):
    return int(a and b or (not a) and c or not b and (not c))


if __name__ == '__main__':
    mas = []
    for i in range(8):
        print(bin(i))
        mas.append(list(map(int, bin(i)[2:])))
    print(mas)
    for sr in mas:
        if len(sr) == 1:
            sr.insert(0, 0)
            sr.insert(0, 0)
        elif len(sr) < 3:
            sr.insert(0, 0)
    print(mas)
    sas = ''
    for i in mas:
        kek = x(i[0], i[1], i[2])
        sas = str(kek) + sas
    sas = '0b' + sas
    print(int(sas, base=2))

# 219
# 28
# 60
# =если($c3<e3;b$5;$e$2)
# 8
# 240
# 30
# 64
# 2
# 11111011
