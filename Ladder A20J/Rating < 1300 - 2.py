a,b,c,d,e = 0,0,0,0,0
h = []
step = 0
for i in range(5):
    l = list(map(int,input().split()))
    a = a + l[0]
    b = b + l[1]
    c = c + l[2]
    d = d + l[3]
    e = e + l[4]
    h.append(sum(l))
    
if(a==1 or e==1):
    step = step + 2
elif(b==1 or d==1):
    step = step + 1

if(h[0]==1 or h[4]==1):
    step = step + 2
elif(h[1]==1 or h[3]==1):
    step = step + 1
    
print(step)
