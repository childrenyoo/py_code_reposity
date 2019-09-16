class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums[0]=(nums[0],nums[0])
        for i in range(1, len(nums)):
            n1=nums[i-1][0]*nums[i]
            n2=nums[i-1][1]*nums[i]
            n3=nums[i]
            imax=max(n1,n2,n3)
            imin=min(n1,n2,n3)
            nums[i]=(imax,imin)
        res=nums[0][0]
        for i in nums[1:]:
            res=max(res,i[0])
        return res
s=Solution()
nums=[2,3,-2,4]
print(s.maxProduct(nums))
