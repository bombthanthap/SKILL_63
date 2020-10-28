n,m = input().split()
n = int(n)
m = int(m)

##print(n)
##print(m)
arr = []

for i in range(n):                  #input bottle
    arr.append(int(input()))
##print(arr)

for i in range(m):                  #input height
    height = int(input())
    sum = 0
    for j in range(len(arr)):
##        print("round : ",j)
        if(height < arr[j] and arr[j] != 0):
            arr[j] = 0
            sum+=1
            if(j+1 != 1):
                if(arr[j-1] <= height and arr[j-1] != 0):
                    arr[j-1] = 0
                    sum+=1
            if(j+1 < len(arr)):
                if(arr[j+1] <= height and arr[j+1] != 0):
                    arr[j+1] = 0
                    sum+=1
##        print(arr)
    print(sum)
        

