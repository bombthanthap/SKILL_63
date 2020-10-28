
order = input()

#arr = []
Rb = 'N'

for i in order:
    if(i == 'N'):
        if(Rb == 'N'):
            Rb = 'N'
        elif(Rb == 'E'):
            print('RRR',end="")
            #arr.append('RRR')
        elif(Rb == 'S'):
            print('RR',end="")
            #arr.append('RR')
        elif(Rb == 'W'):
            #arr.append('R')
            print('R',end="")
        #arr.append('F')
        print('F',end="")
        Rb = 'N'


    elif(i == 'E'):
        if(Rb == 'E'):
            Rb = 'E'
        elif(Rb == 'N'):
            print('R',end="")
        elif(Rb == 'W'):
            print('RR',end="")
        elif(Rb == 'S'):
            print('RRR',end="")
        print('F',end="")
        Rb = 'E'

    elif(i == 'S'):
        if(Rb == 'S'):
            Rb = 'S'
        elif(Rb == 'E'):
            print('R',end="")
        elif(Rb == 'N'):
            print('RR',end="")
        elif(Rb == 'W'):
            print('RRR',end="")
        print('F',end="")
        Rb = 'S'
        
    elif(i == 'W'):
        if(Rb == 'W'):
            Rb = 'W'
        elif(Rb == 'S'):
            print('R',end="")
        elif(Rb == 'E'):
            print('RR',end="")
        elif(Rb == 'N'):
            print('RRR',end="")
        print('F',end="")
        Rb = 'W'

    elif(i == 'Z'):
        Rb = 'N'
        print('Z',end="")


#print("")
#print('Robot direction is : '+Rb)
#print("boat",end="")
