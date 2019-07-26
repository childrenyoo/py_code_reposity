#给定一个字符串，将其分割，使得每一个子串都是回文串
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.partition1(s,1)
    def partition1(self,s,index):
        if len(s[index:]) == 0:
            if s==s[::-1]:
                return [[s]]
            else:return None
        else:
            res = []
            k = s[:index]
            if k == k[::-1]:
                tmp1=self.partition1(s[index:],1)
                if tmp1 != None:
                    i = 0
                    while i < len(tmp1):
                        tmp1[i].insert(0, k)
                        i += 1
                    res += tmp1
            tmp2=self.partition1(s,index+1)
            if tmp2!=None:
                res+=tmp2
            return res

s="aabcc"
c=Solution()
print(c.partition(s))