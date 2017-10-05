import sys
problem_name = str('field')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")

n, m = map(int, input().split())
a = []
b = [[10**9] * n for i in range(m)]
for i in range(m):
    a.append(list(map(int, input().split())))
b[0][0] = 0
for i in range(m):
    for j in range(n):
        if i - 1 >= 0:
            b[i][j] = abs(a[i][j] - a[i - 1][j]) + b[i - 1][j]
        if j - 1 >= 0:
            b[i][j] = min(b[i][j], b[i][j - 1] + abs(a[i][j] - a[i][j - 1]))
print(b[m - 1][n - 1])