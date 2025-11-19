MOD = 1000000007
MAX_N = 100001
t, k = map(int, input().split())
dp=[0]*MAX_N
for i in range(1, MAX_N):
    if i<k:
        dp[i]=1
    elif i==k:
        dp[i]=2
    else:
        dp[i] = (dp[i-1]+dp[i-k]) % MOD
prefix_sum=[0]*MAX_N
for i in range(1,MAX_N):
    prefix_sum[i]=(prefix_sum[i-1]+dp[i])%MOD
for _ in range(t):
    a, b = map(int, input().split())
    ans=(prefix_sum[b]-prefix_sum[a-1]+MOD)%MOD
    print(ans)