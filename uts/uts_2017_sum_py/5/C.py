#import sys

#sys.stdin = open('rectangles.in', 'r')
#sys.stdout = open('rectangles.out', 'w')
n, m, k = map(int, input().split())
a = [[100000, 0, 100000, 0] for i in range(k)]
field = []

for i in range(n):
    field.append(list(map(int, input().split())))

field.reverse()

for i in range(n):
    for j in range(m):
        if field[i][j] > 0:
            v = field[i][j] - 1
            a[v][0] = min(a[v][0], j)
            a[v][1] = max(a[v][1], j)
            a[v][2] = min(a[v][2], i)
            a[v][3] = max(a[v][3], i)

for i in range(k):
    print(a[i][0], a[i][2], a[i][1] + 1, a[i][3] + 1)
