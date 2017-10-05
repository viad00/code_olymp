import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

#for i in range(len(a)):
#    print(a[i])

def check(mas):
    f = True
    for i in range(len(mas)):
        if mas[i] != mas[0]:
            f = False
    return f

for i in range(len(a)):
    if not check(a[i]):
        print('NO')
        quit()
try:
    slov = {}
    pos = 0
    last = a[pos][0]
    slov[a[pos][0]] = 0
    while a[pos][0] == last:
        slov[a[pos][0]] += 1
        last = a[pos][0]
        pos += 1
    last = a[pos][0]
    ###
    try:
        if slov[a[pos][0]]:
            print('NO')
            quit()
    except Exception:
        pass
    slov[a[pos][0]] = 0
    while a[pos][0] == last:
        slov[a[pos][0]] += 1
        last = a[pos][0]
        pos += 1
    last = a[pos][0]
    ###
    try:
        if slov[a[pos][0]]:
            print('NO')
            quit()
    except Exception:
        pass
    slov[a[pos][0]] = 0
    while len(a) != pos and a[pos][0] == last:
        slov[a[pos][0]] += 1
        last = a[pos][0]
        pos += 1

    #print(slov)
    las = -1
    for i in slov:
        if las == -1:
            las = slov[i]
        elif las != slov[i]:
            print('NO')
            quit()
except Exception:
    print('NO')
    quit()
print('YES')
