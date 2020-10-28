
while(1):

    inp = int(input())

    tax = 0
    total = 0

    if(inp == 0):  #step 1
        break

    elif(inp > 100000 and inp <= 1000000): #step 2 tax0.06
        total = (inp-100000)*0.06
        
    elif(inp > 1000000 and inp <= 5000000): #step 3 tax0.06 + tax0.12
        tax = 54000 
        total = (inp-1000000)*0.12+tax

    elif(inp > 5000000 and inp <= 10000000): #step 4 0.06 + 0.12 + 0.20
        tax = 54000 + 480000
        total = (inp-5000000)*0.20+tax
        
    elif(inp > 10000000 ): #step 5 0.06 + 0.12 + 0.20 + 0.32
        tax = 54000 + 480000 + 1000000
        total = (inp-10000000)*0.32+tax

    print(int(total))
    

