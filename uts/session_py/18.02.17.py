import sys
sys.stdin = open("sta.txt", "r")

sta, n = list(map(int, input().split()))
s = []
for i in range(sta):
    s.append(input())
print(s)
