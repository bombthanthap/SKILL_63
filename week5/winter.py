def Prime(x):
    if(x==1):
        return "YES"
    elif(x==2):
        return "NO"
    for i in range(2,x):
        if x % i == 0:
            return "YES"
        else:
            return "NO"

n, x = input().split()

ww = input().split()

hit = int(x)

for i in ww:
    if(Prime(int(i)) == "YES"):
##        print(i," is Monster")
        if(hit > 0):
            hit -= 1
        elif(hit == 0):
##            print("break")
            break
##        print("hit is : ",hit)

    elif(Prime(int(i)) == "NO"):
        hit = int(x)
##        print(i," is friend")
##        print("hit is : ",hit)

if(hit > 0 and hit <= int(x)):
    print("YES")
else:
    print("NO")
