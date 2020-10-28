
inp = input()

n = 0
s = 0
w = 0
e = 0

for i in inp:
    if(i == 'N'):
        n+=1
    elif(i == 'S'):
        s-=1
    elif(i == 'W'):
        w-=1
    elif(i == 'E'):
        e+=1
    else:
        n = 0
        s = 0
        w = 0
        e = 0
        
print(e+w , n+s)



