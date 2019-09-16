class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[1]
        i2=0
        i3=0
        i5=0
        while len(dp)<n:
            tmp=min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            if tmp!=dp[-1]:
                dp.append(tmp)
            if tmp==dp[i2]*2:
                i2+=1
            elif tmp==dp[i3]*3:
                i3+=1
            else:
                i5+=1
        return dp[-1]

s=Solution()
print(s.nthUglyNumber(10))