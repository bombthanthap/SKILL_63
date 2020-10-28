n = int(input())

ar = []
for i in range(n):
##    ar.append(list(map(int,input().split())))
    hero = int(input())
    ar.append(hero)

ar.sort(reverse=True)

bad = int(input())

cnt = 0
sum = 0

for i in range(n):
    if(bad < ar[i]):
        sum += ar[i]
        cnt += 1
        break
    elif(bad >= ar[i]):
        if(sum <= bad):
            sum += ar[i]
            cnt +=1
        else:
            break

if(sum > bad):
##    print("YES")
    print(cnt)
else:
    print("YOU DIE")

