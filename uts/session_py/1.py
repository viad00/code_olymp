from random import randint
#x=int(input())
#y=int(input())
x=10
y=10
sum=0;
maxoffset = 0;
cordx=0;
cordy=0;
mini = min(x,y)
mass = [[randint(0,1) for i in range(x)] for o in range(y)]
for i in range(y):
    print(mass[i])
for i in range(y):
    for o in range(x):
        if mass[i][o] == 0:
            sum=0;
            ii = 0;
            #print("found zero at ",o,i)
            for ii in range(mini):
                if ii+o >= x:
                    break
                if ii+i >= y:
                    break
                sum = sum + mass[i + ii][o + ii]
                for oo in range(ii):
                    sum = sum + mass[i+ii][o+oo]
                    sum = sum + mass[i+oo][o+ii]
                if sum != 0:
                    break
            #print("end zero at offset", ii)
            if (maxoffset< ii):
                maxoffset = ii
                cordx = o
                cordy = i
                #print("!write bigger offset")
print(cordx+1, cordy+1, cordx+maxoffset, cordy+maxoffset)
print('these numbers should be zeroes')
for i in range(cordy,cordy+maxoffset):
    for o in range(cordx,cordx+maxoffset):
        print(mass[i][o])