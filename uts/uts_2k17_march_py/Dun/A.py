import sys
from math import factorial
problem_name = str('combs')
sys.stdin = open(problem_name + ".in", "r")
#sys.stdout = open(problem_name+".out", "w")
n, k = list(map(int, input().split()))
print(int(factorial(n)/(factorial(k)*factorial(n-k))))
f = open('safdsf')
f.close()