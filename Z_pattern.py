n=int(input())

for i in range(0,n,1):
    
    if(i==0 or i==n-1):
        for j in range(0,n,1):
            print('*',end='')
    else:
        for k in range(0,n,1):
            if(k==n-i-1):
                print('*',end=' ')
            else:
                print('',end=' ')
    print()
