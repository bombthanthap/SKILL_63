def Prime(x):
    if(x==1):
        return "NO"
    for i in range(2,x):
        if x % i == 0:
            return "NO"
    else:
        return "Yes"

inp = int(input(''))
if(Prime(inp)=="Yes"):
    print (0)
else:
    j=1
    while(1):
        if(Prime(inp-j)=="Yes"):
            print (j)
            break
        if(Prime(inp+j)=="Yes"):
            print (j)
            break
        j+=1
        

    



    


