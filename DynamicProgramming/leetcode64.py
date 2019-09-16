class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        dp = []
        tmp=[grid[0][0]]
        for j in range(1,n):
            tmp.append(grid[0][j]+tmp[j-1])
        dp.append(tmp)
        for i in range(1,m):
            dp.append([grid[i][0]+dp[i-1][0]])
        for i in range(1,m):
            for j in range(1,n):
                tmp=min(dp[i][j-1],dp[i-1][j])+grid[i][j]
                dp[i].append(tmp)
        return dp[-1][-1]
grid=[[1,3,1],[1,5,1],[4,2,1]]
s=Solution()
print(s.minPathSum(grid))