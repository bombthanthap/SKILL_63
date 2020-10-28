while(1):
    
    n,d,r = map(int,input().split())
    
    if(n != 0 and d != 0 and r != 0):
        
        cnt = 0

        x = input().split()
        x = list(map(int, x))
        x.sort(reverse = True)
            
        y = input().split()
        y = list(map(int, y))
        y.sort()
        
        for i in range(n):
            if (x[i] + y[i]) > d:
                cnt += (x[i] + y[i]) - d
        print(cnt*r)

    else:
       break

                
