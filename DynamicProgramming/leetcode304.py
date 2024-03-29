class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp=[]
        m=len(matrix)
        if m==0:
            return
        n=len(matrix[0])
        if n==0:
            return
        self.dp=[[0 for j in range(n)]for i in range(m)]
        self.dp[0][0]=matrix[0][0]
        for j in range(1,n):
            self.dp[0][j]=matrix[0][j]+self.dp[0][j-1]
        for i in range(1,m):
            self.dp[i][0]=self.dp[i-1][0]+matrix[i][0]
        for i in range(1,m):
            for j in range(1,n):
                self.dp[i][j]=self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]+matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res=self.dp[row2][col2]
        if row1!=0 :
            res-=self.dp[row1-1][col2]
        if col1!=0:
            res-=self.dp[row2][col1-1]
        if row1!=0 and col1!=0:
            res+=self.dp[row1-1][col1-1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
matrix=[[-1]]
row1=0
col1=0
row2=0
col2=0#[1,2,2,4]]
s=NumMatrix(matrix)
print(s.sumRegion(row1,col1,row2,col2))