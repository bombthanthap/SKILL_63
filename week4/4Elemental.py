inp = int(input())

ar=list(map(int,input("").split()))
#print(ar)

num = int(input())

sum = 0

for i in range(inp-3):
    for j in range(i+1,inp-2):
        for k in range(j+1,inp-1):
            for l in range(k+1,inp):
                sum = ar[i]+ar[j]+ar[k]+ar[l]
                #print(ar[i],ar[j],ar[k],ar[l])
                if(sum == num):
                    print(ar[i],ar[j],ar[k],ar[l])
                    print('YES')
                    exit(0)
print('NO')
#print(sum)
