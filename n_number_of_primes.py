import math

n = int(input())
print(2)
n=n-1
l=[]
l.append(2)
a=3
while(n>0):
    flag=0
    for i in l:
        if(i>math.sqrt(a)):
            break
        if(a%i==0):
            flag=1
    if(flag==0):
        l.append(a)
        print(a)
        n=n-1
    a=a+2
