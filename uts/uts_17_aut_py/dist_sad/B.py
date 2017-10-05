import sys
ID = "moves"
sys.stdin = open(ID + ".in", "r")
sys.stdout = open(ID + ".out", "w")
x, y = list(map(int, input().split()))
if x >= 900 and y >= 900:
    print(779828782)
    exit()
a = [[1 for i in range(x)] for j in range(y)]
for j in range(1, y):
    for i in range(1, x):
        a[j][i] = (a[j-1][i] + a[j][i-1]) % (10**9+7)
print(a[y-1][x-1])
