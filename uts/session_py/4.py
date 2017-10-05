import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n = int(input())
count = 0
for i in range(n):
    for j in list(map(int, input().split())):
        count = count + j
count = count / 2
print(int(count))