import sys

sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')
a = []
try:
    while True:
        a.append(int(input()))
except Exception:
    pass

a.sort()
print(a[0])
print(a[len(a)-1])