n = int(input())

ar = []

    
for i in range(n):
    ar.append(list(map(int,input().split())))
    
#find the fucking insect
for x in range(n):
    for y in range(n):
        if(ar[x][y] >= 1):
            insect = ar[x][y]
            for i in range((2*insect)+1):
                for j in range((2*insect)+1):
                    if((x+i-insect >= 0 and x+i-insect < n) and (y+j-insect >= 0 and y+j-insect < n ) and ar[x+i-insect][y+j-insect] == 0):
                        ar[x+i-insect][y+j-insect] = -1
                

flower = 0
for x in range(n):
##    print(ar[x])
    for y in range(n):
        if(ar[x][y] == 0):
            flower +=1
print(flower)
