import sys

sys.stdin = open('count.in', 'r')
sys.stdout = open('count.out', 'w')

m, n = list(map(int, input().split()))
x = [[0 for i in range(31)] for j in range(31)]
s = 0
for i in range(31):
    x[1][i] = 1
for i in range(2, m+1):
    for j in range(n+1):
        for k in range(j+1):
            x[i][j] += x[i-1][k]
for i in range(n+1):
    s += x[m][i]
print(s)
