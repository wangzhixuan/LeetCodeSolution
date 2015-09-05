class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        if m==0:
            return
        n = len(matrix[0])
        
        col0 = 1
        for row in range(m):
            if matrix[row][0] ==0:
                col0 = 0
            for col in range(n):
                if matrix[row][col] ==0:
                    matrix[row][0] = 0
                    if col>0:
                        matrix[0][col] = 0
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, 0, -1):
                if  matrix[row][0] == 0 or matrix[0][col] ==0:
                    matrix[row][col] = 0
                    
        if col0 == 0:
            for row in range(m):
                matrix[row][0] = 0
        
        
                    
        