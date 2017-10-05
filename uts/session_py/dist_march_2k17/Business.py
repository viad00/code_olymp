import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
c = [None for i in range(n+1)]
for i in range(1, n, 2):
    c[i] = 0
c[2] = 1
c[0] = 1
def recursion(n, c):
    if c[n] != None:
        return c[n]
    kkk = 0
    for i in range(1, n):
        kkk += recursion(i-1, c) * recursion(n-i-1, c)
    c[n] = kkk
    return kkk
print(recursion(n, c))