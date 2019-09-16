class Solution(object):
    def __init__(self):
        self.dp=[0,1,2,3,1]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=len(self.dp)-1:
            return self.dp[n]
        for i in range(5,n+1):
            self.dp.append(self.core(i))
        return self.dp[-1]


    def core(self,n):
        nums = []
        s = int(n ** 0.5)
        for i in range(s, 0, -1):
            tmp = n - i ** 2
            if tmp == 0:
                nums.append(1)
                break
            nums.append(self.dp[tmp] + 1)
        return min(nums)

s=Solution()
print(s.numSquares(16))

