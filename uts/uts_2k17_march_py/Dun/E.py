import sys
problem_name = str('goat')
sys.stdin = open(problem_name + ".in", "r")
#sys.stdout = open(problem_name+".out", "w")

m, n, k = map(int, input(). split())
T = [[False]*(n+1) for i in range(m+1)]
for i in range(k):
    n, y = map(int, input().split())
    T[n - 1][y - 1] = True
C = [[0]*(n+1) for i in range(m+1)]
C[1][1] = 1
dead = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            comb = 1
        else:
            comb = C[i-1][j] + C[i][j-1]
        if T[i][j]:
            dead += comb
            comb = 0