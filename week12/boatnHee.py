n,m = map(int,input().split())

ar = []
ar2 = []

cnt = 0
deepB = 0
deepS = 0

for i in range(int(n)):
    inp = int(input())
    ar.append(inp)
ar.sort(reverse=True)


for i in range(int(m)):
    inp2 = int(input())
    ar2.append(inp2)
ar2.sort(reverse=True)

while(deepB < n and deepS<m):
    if(ar[deepB] >= ar2[deepS]):
        deepB += 1
        deepS += 1
        cnt += 1
    else:
        if(ar[deepB] < ar2[deepS]):
            deepS +=1
print(cnt)
