
sum = 0

for i in range(4):
    inp = int(input())
    sum += inp

if(sum <= 49):
    text = 'F'
    
elif(sum >= 50 and sum <= 54):
    text = 'D'

elif(sum >= 55 and sum <= 59):
    text = 'D+'

elif(sum >= 60 and sum <= 64):
    text = 'C'

elif(sum >= 65 and sum <= 69):
    text = 'C+'

elif(sum >= 70 and sum <= 74):
    text = 'B'

elif(sum >= 75 and sum <= 79):
    text = 'B+'

elif(sum >= 80 and sum <= 100):
    text = 'A'

print(text)
