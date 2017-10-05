import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
sal = []
sup = []
mel = []
gar = []
for i in a:
    sal.append(i[0])
    sup.append(i[1])
    mel.append(i[2])
    gar.append(i[3])
from collections import Counter
print(Counter(sal).most_common(1)[0][0],
      Counter(sup).most_common(1)[0][0],
      Counter(mel).most_common(1)[0][0],
      Counter(gar).most_common(1)[0][0])