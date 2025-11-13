n,k=map(int,input().split())
dp=[[0]*(k+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][1]=1
for i in range(2,n+1):
    for j in range(2,k+1):
        if i>=j:
            dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
print(dp[n][k])