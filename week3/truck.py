

N,W = input().split()
N = int(N)
W = int(W)

while(N != 0 and W != 0):
    arr = []
    inp = input()
    for i in inp.split():
        arr.append(int(i))

    tmp = 0
    tructCount = 0
    
    for i in range(N):
        if(tmp < arr[i]):
            tmp = W
            tructCount += 1
        tmp -= arr[i]
        
    print(tructCount)
    N,W = input().split()
    N = int(N)
    W = int(W)
