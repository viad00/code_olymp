from random import randint

k = 0
n = 100000

for i in range(n):
    h = randint(1,6)
    if (h == 2) or (h == 5):
        k += 1;
print(k/n)