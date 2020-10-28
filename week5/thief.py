n, t = input().split()
##t = int(t)

##stl=list(map(int,input("").split()))
stl = input().split()

##stl.sort(reverse = True)
##print(stl)

sum = 0
for i in range(int(t)):
    sum += int(stl[-1-i])
##    print(stl[-1-i])

print(sum)
