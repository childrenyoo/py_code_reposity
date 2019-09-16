def LCS(X,Y):
    m=len(X)+1
    n=len(Y)+1
    dp=[]
    for i in range(m):
        tmp=[0]*n
        dp.append(tmp)
    for i in range(1,m):
        for j in range(1,n):
            if X[i-1]==Y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

X="ABCBDAB"
Y="BDCABA"
print(LCS(X,Y))