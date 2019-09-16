class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)

numc=[-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(numc))