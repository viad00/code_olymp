import sys
problem_name = str('sum')
sys.stdin = open(problem_name + ".in", "r")
#sys.stdout = open(problem_name+".out", "w")

def deld(a):
    left = len(a) // 2
    right = len(a) // 2 + len(a) % 2
    print(0, ' ', left, ' ', right, ' ', left+right)
    b = [a[i] for i in range(left)]
    c = [a[i] for i in range(left, left+right)]
    return b, c

def build(a, fab):
    if len(a) <= 1:
        return
    left, right = deld(a)
    fab.append([0])
    fab.append([0])
    build(left, fab[0])
    build(right, fab[1])

def build_linkers(a, fab):


n, k = list(map(int, input().split()))
mas = [[0] for i in range(n)]
fab = []
build(mas, fab)
query = []
for i in range(k-1):
    s = input().split()
    s[1] = int(s[1])-1
    s[2] = int(s[2])
    if s[0] == 'A':
        mas[s[1]] = [s[2]]
    else:
        query.append(s)

print(query)
print(mas)
print(fab)