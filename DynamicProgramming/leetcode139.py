class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s=="":
            return False
        dp=[True]
        i=1
        while i<=len(s):
            j=0
            while j<i:
                if dp[j] and s[j:i] in wordDict:
                    dp.append(True)
                    break
                j+=1
            if j==i:
                dp.append(False)
            i+=1
        return dp[-1]
s=Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))