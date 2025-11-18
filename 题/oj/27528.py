N=int(input())
dp=[0]*N
dp[0]=1
if N==1:
    print(dp[0])
else:
    dp[1]=2
    for i in range(2,N):
        dp[i]=sum(dp)+1
    print(dp[N-1])