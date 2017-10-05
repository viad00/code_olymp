import sys
import itertools
sys.stdin = open('balls.in', 'r')
#sys.stdout = open('balls.out', 'w')

n = int(input())
query = [int(input()) for i in range(n)]
'''
yadra = [0]
count = 0
storona = 2
while count <= 300000:
    sum = 0
    for i in range(storona):
        sum += i
    storona += 1
    count += sum
    yadra.append(sum + yadra[-1])

print(yadra)
yadra.pop(0)
'''
yadra = [1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330, 1540, 1771, 2024, 2300, 2600, 2925, 3276, 3654, 4060, 4495, 4960, 5456, 5984, 6545, 7140, 7770, 8436, 9139, 9880, 10660, 11480, 12341, 13244, 14190, 15180, 16215, 17296, 18424, 19600, 20825, 22100, 23426, 24804, 26235, 27720, 29260, 30856, 32509, 34220, 35990, 37820, 39711, 41664, 43680, 45760, 47905, 50116, 52394, 54740, 57155, 59640, 62196, 64824, 67525, 70300, 73150, 76076, 79079, 82160, 85320, 88560, 91881, 95284, 98770, 102340, 105995, 109736, 113564, 117480, 121485, 125580, 129766, 134044, 138415, 142880, 147440, 152096, 156849, 161700, 166650, 171700, 176851, 182104, 187460, 192920, 198485, 204156, 209934, 215820, 221815, 227920, 234136, 240464, 246905, 253460, 260130, 266916, 273819, 280840, 287980, 295240, 302621]

for coun in query:
    count = coun
    counter = 0
    index = 0
    while yadra[index + 1] <= count:
        index += 1
    late = yadra[:index+1]
    combs = 1
    flag = True
    while flag:
        for i in itertools.combinations_with_replacement(late, combs):
            if count - sum(i) == 0:
                print(combs)
                flag = False
                break
        combs += 1
