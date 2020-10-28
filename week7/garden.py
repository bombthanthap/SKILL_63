n ,m = map(int,input().split())

ar = []

for i in range(n):
    ar.append(list(map(int,input().split())))
    
yes = 0
no = 0

for i in range(n):
    for j in range(m):
        if(ar[i][0] >= ar[i][j]):
            yes +=1
        if(ar[i][0] == ar[i][m-1])
            yes +=1
        if(ar[0][j] >= ar[i][j] and ar[n-1][j] >= ar[i][j]):
            yes +=1
        else:
            no += 1


if(no > 0):
    print("NO")
else:
    print("YES")
