import math

n = 10000000

a = [True] * n

for i in range(2, int(math.sqrt(n))):
	for j in range(i * 2, n, i):
		a[j] = False
b = [i for i in range(2, n) if a[i]]

#print(b)
print(len(b))
