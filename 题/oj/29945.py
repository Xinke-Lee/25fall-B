n=int(input())
if n==1:
    print('End')
else:
    while True:
        if n%2==0:
            n=n/2
            print(f"{int(2*n)}/2={int(n)}")
        else:
            n=3*n+1
            print(f"{int((n-1)/3)}*3+1={int(n)}")
        if n==1:
            print('End')
            break