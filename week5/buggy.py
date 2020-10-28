n, m, k =input().split()            #5 2 9

walk = 0
bwalk = 0
path = int(k)                       #path = 9

if(path <= int(n)):                 #9 <= 5 ? N
    walk += int(k)                                  
    
else:
    bwalk = int(n)-int(m)    #bwalk = 3
    while(1):
        if(path <= int(n)):         #9 <= 5 ? N     6 <= 5? N   3 <= 5? Y
            walk += path                                        #14+3
            break
        else:
            walk += int(n)+int(m)    #walk = 7      walk = 14
            path -= bwalk            #path = 6      path = 3
    
print(walk)
