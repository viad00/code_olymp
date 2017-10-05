import sys

problem_name = str('input')
sys.stdin = open(problem_name + ".txt", "r")
sys.stdout = open("output.txt", "w")

n, m = map(int, input().split())
n_mas = list(map(int, input().split()))
m_mas = list(map(int, input().split()))
s = []
for i in n_mas:
    if not (i in m_mas):
        s.append(i)
for i in m_mas:
    if not (i in n_mas):
        s.append(i)
if s == []:
    print('EQUAL')
else:
    s.sort()
    for i in s:
        if i in n_mas:
            print('+'+str(i))
        else:
            print('-'+str(i))
#vlaDDisLaVuYtk