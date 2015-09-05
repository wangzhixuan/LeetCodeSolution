class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        dim = len(triangle)
        
        tmplist = list(triangle[-1])
        
        for row in range(dim-2,-1,-1):
            for col in range(row + 1):
                tmplist[col] = min(tmplist[col], tmplist[col+1]) + triangle[row][col]
        
        return tmplist[0]        