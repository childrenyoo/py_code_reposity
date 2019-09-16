class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="" or s=="0":
            return 0
        dp=[1,1]
        for i in range(1,len(s)):
            tmp=0
            if s[i]>="1":
                tmp+=dp[-1]
            if s[i-1:i+1]>="10" and s[i-1:i+1]<="26":
                tmp+=dp[-2]
            dp.append(tmp)
        return dp[-1]
s=Solution()
t="226"
print(s.numDecodings(t))