n,a,b,c=map(int,input().split())
dp=[0]+[-1e9]*n
for i in a,b,c:
    for j in range(i,n+1):
        dp[j]=max(dp[j],dp[j-i]+1)
print(dp[n])