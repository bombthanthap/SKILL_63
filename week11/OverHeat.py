x1,y1,w1,h1 = input().split()
x2,y2,w2,h2 = input().split()

x1 = int(x1)
y1 = int(y1)
w1 = int(w1)
h1 = int(h1)

x2 = int(x2)
y2 = int(y2)
w2 = int(w2)
h2 = int(h2)

OverlapX = max(0,(min(x1+w1,x2+w2)-max(x1,x2)))
OverlapY = max(0,(min(y1+h1,y2+h2)-max(y1,y2)))

OverlapX = int(OverlapX)
OverlapY = int(OverlapY)

print((OverlapX*OverlapY))
