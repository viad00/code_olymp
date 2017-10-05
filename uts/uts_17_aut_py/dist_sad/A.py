import sys, math

ID = "quadros"
sys.stdin = open(ID + ".in", "r")
sys.stdout = open(ID + ".out", "w")
n = int(input())
n = n // 2
n = int(math.sqrt(n))
print(n)
