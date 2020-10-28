
order = input()

numb = int(input())

n = 0
s = 0
w = 0
e = 0


for i in order:
    if(i == 'N'):
        n+=1
    elif(i == 'S'):
        s+=1
    elif(i == 'W'):
        w+=1
    elif(i == 'E'):
        e+=1

if (n >= s and s != 0):   
    if(s <= numb):       
        numb -= s       
        s = 0
    else:
        s -= numb
        numb = 0
elif (s > n and n != 0):   
    if(n <= numb):       
        numb -= n       
        n = 0
    else:
        n -= numb
        numb = 0
    
        
if (w >= e and e != 0):   
    if(e <= numb):       
        numb -= e       
        e = 0
    else:
        e -= numb
        numb = 0
elif (e > w and w != 0):   
    if(w <= numb):       
        numb -= w       
        w = 0
    else:
        w -= numb
        numb = 0

print((abs(n-s)+abs(w-e)-numb)*2)
#print(numb)



