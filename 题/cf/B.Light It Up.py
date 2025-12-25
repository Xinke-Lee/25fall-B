k=int(input())
heights=list(map(int,input().split()))
dp=[1]*k
for i in range(1,k):
    for j in range(i):
        if heights[i]<=heights[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))