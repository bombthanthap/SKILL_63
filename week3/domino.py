def fibo(n): 
    f = 0
    s = 1
    if n < 0: 
        return 0 
    elif n == 0: 
        return f 
    elif n == 1: 
        return s 
    else: 
        for i in range(2,n+2): 
            c = f + s 
            f = s 
            s = c 
        return s
    
#while True:
n = int(input())
print(fibo(n))
    
        
            
