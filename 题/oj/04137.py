for  _ in range(int(input())):
    n,k=map(int,input().split())
    N=str(n)
    stack=[]
    for i in N:
        while k>0 and stack and stack[-1]>i:
            stack.pop()
            k-=1
        stack.append(i)
    while k>0:
        stack.pop()
        k-=1
    print(''.join(stack))

