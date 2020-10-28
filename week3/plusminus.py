inp = input()
num = input()

sum = 0
x = 1

for i in num.split():
    if i == '-':
        x = -1
    elif i == '+':
        x = 1
    else:
        sum += int(i)*x

print(sum)

