N,B=map(int,input().split())
val=list(map(int,input().split()))
wei=list(map(int,input().split()))
dp=[0]*(B+1)
for i in range(N):
    for j in range(B,wei[i]-1,-1):
        dp[j]=max(dp[j-wei[i]]+val[i],dp[j])
print(dp[B])