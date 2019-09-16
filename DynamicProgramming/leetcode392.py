class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        index1=0
        index2=0
        length=len(t)
        dp=[]
        while index2<len(s) and index1<length:
            if t[index1]==s[index2]:
                index2+=1
            index1+=1
        return index2==len(s)
s="leeeeetcode"
t="leeeeeetcode"
c=Solution()
print(c.isSubsequence(s,t))


