class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        length = len(A)
        
        if length ==0:
            return 0
        elif target > A[length-1]:
            return length
        elif target <= A[0]:
            return 0
        
        
        highbound = length - 1
        lowbound = 0
        
        while (highbound>lowbound + 1):
            mid_position = (highbound + lowbound)/2
            if (target <= A[mid_position]):
                highbound = mid_position
            else:
                lowbound = mid_position
        
        return lowbound + 1
                
        