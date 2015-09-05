"""
Accepted Solution.
"""
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        Grid = obstacleGrid
        
        m = len(Grid)
        if m == 0:
            return 0
        
        n = len(Grid[0])    
        if n == 0:
            return 0
        
        tmplst = [0] * n
        tmplst[0] = 1
        
        for row in Grid:
            for index in range(n):
                if row[index]==1:
                    tmplst[index]=0
                elif index > 0:
                    tmplst[index] += tmplst[index-1]
                
                
        return tmplst[n-1]  

"""
Recursive solution: got Time LImit Exceeded. 
Too much repeated calculation
"""
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        return my_uniquePath(obstacleGrid,0,0,m,n)
        
    def my_uniquePath(Grid, istart, jstart, iend, jend):
        if (Grid[istart][jstart]==1) or (Grid[iend][jend]==1):
            return 0
        elif (istart > iend) or (jstart > jend):
            return 0
        elif (istart == iend):
            if sum(Grid[istart][jstart:jend+1])>0:
                return 0
            else:
                return 1
        elif (jstart == jend):
            tmp_sum = 0
            for i in range(istart, iend + 1):
                tmp_sum += Grid[i][jstart]
            if tmp_sum > 0:
                return 0
            else:
                return 1
            
        imiddle = (istart + iend)/2
        maxi_sum = sum(Grid[imiddle][istart:iend + 1]) 
        
        for i in range(istart, iend + 1):
            tmp_sum = sum(Grid[imiddle][istart:iend + 1])
            if (tmp_sum> maxi_sum):
                maxi_sum = tmp_sum
                imiddle = i

        result = 0

        iend2 = max(imiddle - 1, istart)
        istart2 = min(imiddle + 1, iend)


        for j in range(jstart, jend+1):
            if (Grid[imiddle][j] == 1):
                continue
            else:
                tmp1 = my_uniquePath(Grid, istart, jstart, iend2, j)
                if (tmp1 == 0):
                    continue
                tmp2 = my_uniquePath(Grid, istart2, j, iend, jend)
                result += tmp1 * tmp2

         return result       




sol = Solution()
print sol.uniquePathsWidthObstacles([[0,0,0],[0,1,0],[0,0,0]])
