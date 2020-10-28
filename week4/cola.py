numCola = int(input()) #buy

bottle = numCola+1 #borrow friend rec 1 bottle

drink = numCola     #eat all buy

while(1):                   #loop for check bottle
    if(bottle < 3):         #bottle < 3 cant change just eat
        break
    chBottle = bottle//3    #keep change bottle
    drink += chBottle       #drink all 
    bottle -= chBottle*2    #find bottle dont eat to change

print(drink)

