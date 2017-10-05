import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
s = int(input())
l = 1
h = int(10e18)
while l <= h:
    mid = (l+h)//2
    x = mid
    now = mid
    while x != 0:
        st = str(x)
        st = st[:-1]
        if len(st) == 0:
            break
        x = int(st)
        now += x
    if now == s :
        print(mid)
        quit()
    elif now < s :
        l = mid + 1
    else :
        h = mid - 1
print(-1)
