x,y,x1,y1,x2,y2 = map(int, input().split())

sqr1 = (x-y1) * (y-x2)

sqr2 = (x-x1) * (y-y2)

sqr3 = (x-x1-x2) * (y-y2)

inx=0
iny=0



if(x1 >= x-y1):
    inx=1
    
if(x1 >= y-y2):
    iny=1
    
if(inx==0 and iny==1):
    print(max(sqr1,sqr2,(x-x1-y1)*y))
    
elif(inx==1 and iny==0):
    print(max(sqr1,sqr2,(y-x2-y2)*x))
else:
    print(max(sqr1,sqr2))
