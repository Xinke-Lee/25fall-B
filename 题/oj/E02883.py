while True:
    try:
        a=list(map(int,input().split()))
        b=sorted(a)
        c=list(map(str,b))
        if a==b:
            print('Yes')
        else:
            print('No '+' '.join(c))
    except EOFError:
        break
