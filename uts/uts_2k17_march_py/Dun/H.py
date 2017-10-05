import sys
import re
problem_name = str('patterns')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")
if re.compile(input().replace('*', '.*').replace('?', '.')).match(input()) != None:
    print('YES')
else:
    print('NO')
