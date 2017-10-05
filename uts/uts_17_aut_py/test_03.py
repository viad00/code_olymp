import sys, os
from operator import xor

disk0 = ['0xA', '0x3', '0x0', '0x8', '0x8', '0x1']
disk1 = ['', '', '', '', '', '']
disk2 = ['0x5', '0x7', '0xB', '0x6', '0x6', '0xC']

a = disk0
b = disk1
c = disk2

for i in range(len(disk0)):
    disk0[i] = int(disk0[i], base=16)
    disk2[i] = int(disk2[i], base=16)

print(disk0)
print(disk2)

for i in range(len(disk0)):
    if b[i] == '':
        b[i] = xor(c[i], a[i])
    elif c[i] == '':
        c[i] = xor(a[i], b[i])
    elif a[i] == '':
        a[i] = xor(c[i], b[i])
    tmp = a
    a = b
    b = c
    c = tmp

print(disk1)

print(hex(sum(disk0) + sum(disk1)))
summ = 0

for i in range(0, len(disk0), 3):
    summ += disk0[i]
    summ += disk1[i]
    print('Число: {0}'.format(i))
    summ += disk1[i+1]
    summ += disk2[i+1]

    summ += disk2[i+2]
    summ += disk0[i+2]

print(hex(summ))
