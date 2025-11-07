def nums(m):
    hang,lie=len(m),len(m[0])
    table=[[False for _ in range(lie)] for _ in range(hang)]
    nums_r=0
    nums_b=0

    def dfs(i,j,cry):
        if 0<=i<hang and 0<=j<lie and m[i][j]==cry and not table[i][j]:
            table[i][j]=True
            dfs(i+1,j,cry)
            dfs(i-1,j,cry)
            dfs(i,j-1,cry)
            dfs(i,j+1,cry)

    for i in range(hang):
        for j in range(lie):
            if m[i][j]=='r' and not table[i][j]:
                dfs(i,j,'r')
                nums_r+=1
            if m[i][j]=='b' and not table[i][j]:
                dfs(i,j,'b')
                nums_b+=1
    return nums_r,nums_b

k=int(input())
for _ in range(k):
    n=int(input())
    m=[[] for ___ in range(n)]
    for i in range(n):
        district=input()
        for k in district:
            m[i].append(k)
    print(*nums(m))

