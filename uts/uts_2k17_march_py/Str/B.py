import sys
import collections
problem_name = str('substr')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")

print(collections.Counter(input()).most_common()[0][0])