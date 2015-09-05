class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])    
        if n == 0:
            return 0
        
        tmplst = [0] * n
        
        for index0 in range(m):
            for index1 in range(n):
                if index1 == 0:
                    tmplst[index1] += grid[index0][index1]
                elif index0 ==0:
                    tmplst[index1] = grid[index0][index1] + tmplst[index1-1]
                else:
                    tmplst[index1] = grid[index0][index1] + min(tmplst[index1], tmplst[index1-1])
                
                
        return tmplst[n-1]  
