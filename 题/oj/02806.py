while True:
    try:
        a,b=input().split()
    except EOFError:
        break

    lena=len(a)
    lenb=len(b)
    dp=[[0]*(lena+1) for _ in range(lenb+1)]
    for i in range(1,lenb+1):
        for j in range(1,lena+1):
            if b[i-1]==a[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[lenb][lena])