while True:
    N=0
    n1,n2,n3,n4,n5,n6=map(int,input().split())
    if (n1,n2,n3,n4,n5,n6)==(0,0,0,0,0,0):
        break
    #1
    n1-=11*n5
    N=n4+n5+n6
    #2
    if n2>5*n4:
        n1-=0
        n2-=5*n4
    else:
        n1-=(36-16)*n4-4*n2
        n2-=n2
    #3
    if n3%4==0:
        n1-=0
        n2-=0
        N+=n3//4
    elif n3%4==1:
        N+=n3//4+1
        if n2>5:
            n2-=5
            n1-=36-9-4*5
        else:
            n2-=n2
            n1-=36-9-4*n2
    elif n3%4==2:
        N+=n3//4+1
        if n2>3:
            n2-=3
            n1-=36-9-4*3
        else:
            n2-=n2
            n1-=36-18-4*n2
    elif n3%4==3:
        N+=n3//4+1
        if n2>1:
            n2-=1
            n1-=36-27-4*1
        else:
            n2-=n2
            n1-=36-27-4*n2
    if n1>0:
        n1-=0
    else:
        n1=0
    #4
    if (n1+4*n2)%36==0:
        N+=(n1+4*n2)//36
    else:
        N+=(n1+4*n2)//36+1
    print(N)


    



