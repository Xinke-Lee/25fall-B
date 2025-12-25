for _ in range(int(input())):
    E,F=map(int,input().split())
    N=int(input())
    coins=[]
    for __ in range(N):
        P,W=map(int,input().split())
        coins.append((P,W))
    weight=F-E
    dp=[0]+[1e9]*weight
    for i in range(N):
        for j in range(coins[i][1],weight+1):
            dp[j]=min(dp[j],dp[j-coins[i][1]]+coins[i][0])
    if dp[weight]==1e9:
        print("This is impossible.")
    else:
        print(f"The minimum amount of money in the piggy-bank is {dp[weight]}.")