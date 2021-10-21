# cook your dish here
t = int(input())
while(t):
    l = int(input())
    L = [int(i) for i in input().split()]
    print(*L[::-1])

    for i in range(1, l):
        if(i%3==0):
            print(L[i] + 3, end=" ")
    print()
            
    for i in range(1, l):
        if(i%5==0):
            print(L[i] - 7, end=" ")
    print()
    
    p = L[3:8]
    print(sum(p))
    t-=1