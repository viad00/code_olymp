import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n, m = map(int, input().split())
mas = []
for i in range(n):
    mas.append(list(map(int, input().split())))
ans = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        dist = 1000
        for k in range(n):
            for l in range(m):
                if mas[k][l] == 1:
                    dist = min(dist, abs(k - i) + abs(l-j))
        ans[i][j] = dist
for i in range(len(ans)):
    print(*ans[i])
    #http://127.0.0.1:41017/