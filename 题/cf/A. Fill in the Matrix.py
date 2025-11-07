t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if m==1:
        print(0)
        for j in range(n):
            print(0)
    else:
        if n < m:
            print(n + 1)
        else:
            print(m)
        for j in range(n):
            if j < m - 1:
                a = [(j + k) % m for k in range(m)]
            else:
                a = [(0 + k) % m for k in range(m)]
            print(*a)
