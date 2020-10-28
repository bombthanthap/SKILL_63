N = int(input(''))
last = N%10
while(N>=10):
    N/=10
first = int(N)
print (str(first)+str(last))
