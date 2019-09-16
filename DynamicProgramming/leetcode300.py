class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp=[1]
        for i in range(1,len(nums)):
            imax =0
            for j in range(i):
                if nums[i]>nums[j]:
                    imax=max(imax,dp[j])
            dp.append(imax+1)
        return max(dp)
nums=[10,9,2,5,3,7,101,18]
s=Solution()
print(s.lengthOfLIS(nums))