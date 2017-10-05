from random import *

from math import cos, pi

n = 10000
k = 0
for i in range(n):
    y = uniform(-1, 1)
    x = uniform(-pi, pi)
    if ((y <= cos(x)) and (x >= -pi) and (x <= pi) and (y >= 0)) \
            or ((y >= cos(x)) and (x >= -pi) and (x <= pi) and (y <= 0)):
        k += 1
print(k/n*pi*4)