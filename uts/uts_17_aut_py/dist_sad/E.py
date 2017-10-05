import sys
import math
sys.stdin=open('storage.in','r')
sys.stdout=open('storage.out','w')
def NEPALUS(s,n):
    if s=='0':
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return 4
    elif s=='1':
        if n==2:
            return 3
        elif n==0:
            return 5
    elif s=='2':
        if n==1:
            return 3
        elif n==0:
            return 6
    elif s=='4':
        if n==1:
            return 5
        elif n==2:
            return 6
    else:
        return 7
def VASHE(s,n):
    if s=='1' and n!=1 or s=='2' and n!=2 or s=='4' and n!=0 or s=='3' and n==0 or s=='5' and n==2 or s=='6' and n==1:
            return s
    if s=='3':
        if n==1:
            return 2
        elif n==2:
            return 1
    elif s=='5':
        if n==1:
            return 4
        elif n==0:
            return 1
    elif s=='6':
        if n==2:
            return 4
        elif n==0:
            return 2
    elif s=='7':
        if n==1:
            return 6
        elif n==2:
            return 5
        elif n==0:
            return 3
    else:
        return 0
n,m=map(int,input().split())
c=math.ceil(n/3)
a={}
for i in range(m):
    q=list(map(str,input().split()))
    if q[0]=='Login':
        a[q[1]]='0'*c
    elif q[0]=='Completed':
        q[2]=int(q[2])
        if q[2]==0:
            pass
        else:
            l=(q[2]-1)//3
            a[q[1]]=a[q[1]][:l]+str(NEPALUS(a[q[1]][l],q[2]%3))+a[q[1]][(l+1):]
    elif q[0]=='Clear':
        q[2]=int(q[2])
        if q[2]==0:
            pass
        else:
            l=(q[2]-1)//3
            a[q[1]]=a[q[1]][:l]+str(VASHE(a[q[1]][l],q[2]%3))+a[q[1]][(l+1):]
    else:
        print(q[1],a[q[1]])
