# RZ2T(SAM)_7.py
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

s = input()
a = []
for i in range(len(s)):
    try:
        if 1 <= int(s[i] + s[i+1]) <= 26:
            a.append(int(s[i] + s[i+1]))
            s = s[:i] + 'aa' + s[i+2:]
        else:
            raise Exception('No number')
    except Exception:
        try:
            if int(s[i]):
                a.append(int(s[i]))
                s = s[:i] + 'a' + s[i + 1:]
        except Exception:
            pass
s = ''
slov = {
    1: 'z',
    2: 'y',
    3: 'x',
    4: 'w',
    5: 'v',
    6: 'u',
    7: 't',
    8: 's',
    9: 'r',
    10: 'q',
    11: 'p',
    12: 'o',
    13: 'n',
    14: 'm',
    15: 'l',
    16: 'k',
    17: 'j',
    18: 'i',
    19: 'h',
    20: 'g',
    21: 'f',
    22: 'e',
    23: 'd',
    24: 'c',
    25: 'b',
    26: 'a',
}
for i in a:
    s += slov[i]
print(s)
# ------------------------------------------ #
