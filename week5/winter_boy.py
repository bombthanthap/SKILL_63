def Is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

n,k=input().split()
ar=list(map(int,input().split()))
k=int(k)
hit=k
for i in ar:
    if(Is_prime(i)):
        hit=k
    else:
        hit-=1
        if(hit<0):
            print("NO")
            break

if(hit>=0):
    print("YES")
