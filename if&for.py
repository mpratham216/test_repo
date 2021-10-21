test = int(input())
userVal=[None]*test
for i in range(0,test):
    userVal[i]=int(input())

for x in userVal:
    for i in range(0,x):
        if(i==0):
            print(3+i, end=' ')
        elif(i%2==0):
            print(2*i, end=' ')
        else:
            print(i*i, end=' ')
    print(" ")