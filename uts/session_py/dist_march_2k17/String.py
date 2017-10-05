import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
orig, end = input(), input()

while len(end) > len(orig):
    if end[-1] == 'A':
        end = end[:-1]
    else:
        end = end[:-1][::-1]

if orig == end:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')