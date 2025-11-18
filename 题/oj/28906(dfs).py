def dfs(i,j,k):
    count=0
    if j==1:
        return 1
    elif i<j:
        return 0
    else:
        for m in range(k,i//j+1):
            count+=dfs(i-m,j-1,m)
    return count

n,k = map(int,input().split())
print(dfs(n,k,1))


