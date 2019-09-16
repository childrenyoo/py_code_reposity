class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        if n==0:
            return 0
        for row in range(1,len(triangle)):
            for index in range(len(triangle[row])):
                if index==0:
                    triangle[row][index]+=triangle[row-1][index]
                elif index==len(triangle[row])-1:
                    triangle[row][index]+=triangle[row-1][index-1]
                else:
                    triangle[row][index]+=min(triangle[row-1][index],triangle[row-1][index-1])
        return min(triangle[-1])
