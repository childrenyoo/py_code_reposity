class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        dp=[0,nums[0]]
        for i in range(1,len(nums)):
            tmp=max(dp[i],dp[i-1]+nums[i])
            dp.append(tmp)
        return dp[-1]
nums=[1,2,3,1]
s=Solution()
print(s.rob(nums))