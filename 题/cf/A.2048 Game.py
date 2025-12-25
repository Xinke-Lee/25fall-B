q=int(input())
for _ in range(q):
    n=int(input())
    s1=list(map(int,input().split()))
    s=[]
    for i in s1:
        if i<=2048:
            s.append(i)
    b=0
    s.sort(reverse=True)
    if s:
        for i,nums in enumerate(s):
            b+=nums
            if b==2048:
                print('YES')
                break
            if i==len(s)-1 and b!=2048:
                print('NO')
                break
    else:
        print('NO')
