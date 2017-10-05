import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n, m = map(int, input().split())
n_mas = [0 for i in range(n)]
for i in range(m):
    for j in list(map(int, input().split())):
        n_mas[j-1] += 1
print(*n_mas)