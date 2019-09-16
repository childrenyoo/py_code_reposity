class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if cost==[]:
            return 0
        elif len(cost)==1:
            return cost[0]
        elif len(cost)==2:
            return min(cost)
        dp=[0,0]
        for i in range(2,len(cost)+1):
            tmp=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
            dp.append(tmp)
        return dp[-1]

