class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if (n==0):
            return None
        elif (n==1):
            return matrix
        
        for i in range(n/2):
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]  
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1] 
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]  
                matrix[j][n-i-1] = tmp
                
        return matrix
