class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #G(n)表示n个节点的二叉搜索数个数
        #f(n)表示以n为根的二叉搜索数的个数
        #G(n)=f(1)+f(2)+...+f(n)
        #f(i)=G(i-1)*G(n-i)
        #G(n)=2(G(0)+G(1)+...+G(n-1))
        G=[1,1,2]
        for i in range(2,n+1):
            tmp=0
            left=0
            right=len(G)-1
            while left<right:
                tmp+=G[left]*G[right]
                left+=1
                right-=1
            tmp*=2
            if left==right:
                tmp+=G[left]*G[right]
            G.append(tmp)
        return G[n]
s=Solution()
print(s.numTrees(3))
