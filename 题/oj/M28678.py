n=int(input())
while True:
    if n%2==0 and n>1:
        print(f"{n}/2={int(n/2)}")
        n=int(n/2)
    elif n%2==1 and n>1:
        print(f"{n}*3+1={int(n*3+1)}")
        n=int(n*3+1)
    else:
        print('End')
        break
        