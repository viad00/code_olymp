import sys
problem_name = str('slalom')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")

n= int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
count=0
for i in reversed(range(len(a)-1)):
    for j in range(len(a[i])):
        a[i][j] = a[i][j] + max(a[i+1][j], a[i+1][j+1])
print(a[0][0])