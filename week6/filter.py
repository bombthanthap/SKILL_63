w, h, wd = input().split()
w = int(w)
h = int(h)
wd = int(wd)

arr = []
for i in range(w):
    col=[]
    for j in range(h):
        col.append(input())
    arr.append(col)
print(arr)



