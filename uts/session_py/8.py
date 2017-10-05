from random import *

n = 10000
k = 0

for i in range(n):
    y = randint(0, 7) + random()
    x = randint(0, 9) + random()
    if (y <= 4 * x) and (y <= 10-x) and (y >= 0):
        k += 1
print((k/n)*80)