x, y, n = input().split()

arr = []
fall = int(x)-int(y)
cnt = 0

for i in range(int(n)):
    wall = int(input())
    arr.append(wall)

    if(int(x) >= arr[i]):
        cnt += 1

    else:
        arr[i] -= fall
        cnt += 1
        while(int(x) < arr[i]):
            arr[i] -= fall
            cnt += 1
        cnt += 1

##print(fall)
print(cnt)
