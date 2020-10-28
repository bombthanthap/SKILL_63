n = int(input())

ar = []
ar2 = []
ar3 = []
for i in range(n):
    
    m = int(input())
    
    if(m<0):
        ar.append(m)
        
    elif(m>0):
        ar2.append(m)
        
    else:
        ar3.append(m)

        
ar.sort()

ar2.sort(reverse=True)

sum=0

for i in range(len(ar)//2):
    sum += ar[0] * ar[1]
    ar.pop(0)
    ar.pop(0)


for i in range(len(ar2)//2):
    sum += ar2[0] * ar2[1]
    ar2.pop(0)
    ar2.pop(0)

    
if(len(ar)!=0 and len(ar3)!=0):
    sum += ar[0] * ar3[0]
    ar.pop(0)
    ar3.pop(0)


    
if(len(ar)!=0 and len(ar2)!=0):
    sum += ar[0] * ar2[0]
    ar.pop(0)
    ar2.pop(0)

    
if(len(ar)!=0):
    sum += ar[0]

    
if(len(ar2)!=0):
    sum += ar2[0]



##for i in range(len(ar)//2):
##    sum += ar[0]
##    ar.pop(0)
##
##
##for i in range(len(ar2)):
##    sum += ar2[0] * ar2[1]
##    ar2.pop(0)
##
##    
##if(len(ar)!=0):
##    sum += ar[0] * ar3[0]
##    ar.pop(0)
##    ar3.pop(0)
##
##    
##if(len(ar)!=0 and len(ar2)!=0):
##    sum += ar[0] * ar2[0]
##    ar.pop(0)
##    ar2.pop(0)
##
##    
##if(len(ar)!=0):
##    sum += ar[0]
##
##    
##if(len(ar2)!=0):
##    sum += ar2[0]



 
print(sum)
