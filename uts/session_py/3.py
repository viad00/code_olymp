import sys

problem_name = str('calendar')
sys.stdin = open(problem_name + ".in", "r")
# sys.stdout = open(problem_name+".out", "w")

def get_mass(num):
    arr = []
    n = num
    while n > 0:
        arr.append(n%10)
        n = n//10
    return arr

def bad_char(start, end, bad):
    counterr = 0
    for day in range(start, end):
        an = get_mass(day)
        for nu in num:
            if nu in an:
                counterr += 1
    return counterr


n, k = map(int, input().split())
a = list(map(int, input().split()))
num = list(map(int, input().split()))
print(n,' ',k)
counter = 0
a.sort()
print(a)
lastmas = 0
lastcount = 0

for mounth in a:
    if lastmas == mounth:
        counter = counter + lastcount
    else:
        counter = counter + lastcount + lastcount + bad_char(lastmas, mounth, num)
        lastmas = mounth
print(counter)