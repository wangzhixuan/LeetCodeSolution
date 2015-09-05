class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        low = 0
        high = len(matrix)-1
        
        row = None
        if high ==-1 or target < matrix[0][0]:
            return False
        elif target ==matrix[high][0] or target == matrix[low][0]:
            return True
        elif target > matrix[high][0]:
            row = high    
        
        while (low<high-1) and (row ==None):
            mid = (low+high)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0]<target:
                low = mid
            else:
                high = mid
        
        if row== None:
            row = low
            
        left = 0
        right = len(matrix[0])-1
        
        if target > matrix[row][right]:
            return False
        elif target == matrix[row][right]:
            return True
        
        while (left<right-1):
            mid = (left + right)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]<target:
                left = mid
            else:
                right = mid
        return False