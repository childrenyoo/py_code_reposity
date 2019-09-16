class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        if n==0:
            return 0
        dp=[[0 for j in range(n)]for i in range(m)]
        maxL=0
        for j in range(n):
            dp[0][j]=eval(matrix[0][j])
            maxL = max(maxL, dp[0][j])
        for i in range(1,m):
            dp[i][0]=eval(matrix[i][0])
            maxL = max(maxL, dp[i][0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=="1":
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    maxL = max(maxL, dp[i][j])
                else:
                    dp[i][j]=0
        return maxL**2
s=Solution()
matrix=[["1","0","1","1","0","1"],
        ["1","1","1","1","1","1"],
        ["0","1","1","0","1","1"],
        ["1","1","1","0","1","0"],
        ["0","1","1","1","1","1"],
        ["1","1","0","1","1","1"]]
print(s.maximalSquare(matrix))

