while True:
    try:
        n,m = map(int,input().split())
        if n==0 and m==0:
            break
        monkey=[i+1 for i in range(n)]
        a=0
        while len(monkey)>1:
            a=(a+m-1)%len(monkey)
            del monkey[a]
        print(monkey[0])
    except EOFError:
        break