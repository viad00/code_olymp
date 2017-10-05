from itertools import permutations
n = int(input())
pool = list(map(int, input().split()))
pool.reverse()
maxim = 0
def play(nel):
    c_nush = 0
    c_bara = 0
    last = 0
    for cookie in nel:
        if c_nush > c_bara:
            c_bara += cookie
            last = 1
        elif c_bara > c_nush:
            c_nush += cookie
            last = 0
        elif c_bara == c_nush and last == 0:
            c_nush += cookie
        elif c_bara == c_nush and last == 1:
            c_bara += cookie
    return c_nush
maxim = play(pool)
print(maxim)
