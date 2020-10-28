num = int(input())

ar = []
win = []

for i in range(4*num):
    inp = int(input())
    ar.append(inp)
    
for i in range(4):
    max = 0
    index = 0
    for j in range(num*i,num*(i+1)):
        if(max < ar[j]):
            max = ar[j]
            index = j
    win.append(index)

if(ar[win[0]] >= ar[win[1]]):
    winA = win[0]
    loseA = win[1]
else:
    winA = win[1]
    loseA = win[0]

if(ar[win[2]] >= ar[win[3]]):
    winB = win[2]
    loseB = win[3]
else:
    winB = win[3]
    loseB = win[2]

if(ar[winA] >= ar[winB]):
    print(winA+1,winB+1,loseA+1,loseB+1)
else:
    print(winB+1,winA+1,loseA+1,loseB+1)
