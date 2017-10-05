#RZ2T(CAM)_7.py:
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = list(map(int, input().split()))
t = int(input())

a.sort()
u, y = 0, 0
for i in range(t):
    x = list(map(int, input().split()))
    if x[0] == 1:
        u = u + 1
    elif x[0] == 2:
        y = y + x[1]
    elif x[0] == 3:
        q = y / u
        d = n
        for j in range(n):
            if a[j] > q:
                d = j
                break
        print(n - d)

sys.stdout.close()

#RZ2T(CAM)_8.py:
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

x = int(input())
a, b, c = list(map(int, input().split()))
z = [[a, 'a'], [b, 'b'], [c, 'c']]
z.sort()
c, b, a = z[0], z[1], z[2]

for i in range(int(x / a[0]) + 1):
    for j in range(int((x - a[0]) / b[0]) + 1):
        if (x - j * b[0] - i * a[0]) % c[0] == 0:
            a[0], b[0], c[0] = i, j, (x - j * b[0] - i * a[0]) / c[0]

s = ''
for i in [a, b, c]:
    if i[1] == 'a':
        s = str(i[0])

for i in [a, b, c]:
    if i[1] == 'b':
        s = s + ' ' + str(i[0])

for i in [a, b, c]:
    if i[1] == 'c':
        s = s + ' ' + str(i[0])

print(s)

sys.stdout.close()

#RZ2T_7.py:
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = list(map(int, input().split()))

b = 0
for i in range(n):
    a = list(map(int, input().split()))
    c = 0
    for j in a:
        if j == 0:
            c = c + 1
        else:
            b = max(b, c)
            c = 0
    b = max(b, c)

print(b)

sys.stdout.close()

#RZ2T_8.py:
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
sal = []
sup = []
mel = []
gar = []
for i in a:
    sal.append(i[0])
    sup.append(i[1])
    mel.append(i[2])
    gar.append(i[3])
from collections import Counter

print(Counter(sal).most_common(1)[0][0],
      Counter(sup).most_common(1)[0][0],
      Counter(mel).most_common(1)[0][0],
      Counter(gar).most_common(1)[0][0])

#RZ2T_9.py:
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

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
