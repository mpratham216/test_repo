def stars(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if((i+j)<=n+1):
                if(j%5==0):
                    print("#",end="")
                else:
                    print("*",end="")
            else:
                print(" ",end="")
        print(" ")

#main
test=int(input())
val=[None]*test
for i in range(0,test):
    val[i]=int(input())
    
for i in range(0,test):
    stars(val[i])

