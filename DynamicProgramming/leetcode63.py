class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        if m==0:
            return 0
        n=len(obstacleGrid[0])
        if n==0:
            return 0
        dp=[]
        for i in range(m):
            tmp=[0]*n
            dp.append(tmp)

        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for j in range(1,n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=dp[0][j-1]
            else:
                dp[0][j]=0
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
            else:
                dp[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=0
        return dp[-1][-1]

ob=[[0,0,0],[0,1,0],[0,0,0]]
s=Solution()
print(s.uniquePathsWithObstacles(ob))