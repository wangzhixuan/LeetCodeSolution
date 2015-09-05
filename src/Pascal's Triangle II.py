class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        
        result = [1]*(rowIndex+1)
        
        for index in range(rowIndex):
            for index2 in range(index, 0, -1):
                result[index2] += result[index2-1]
        
        return result        