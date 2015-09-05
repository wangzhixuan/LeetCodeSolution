class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n < 2:
            return True
            
        right_most = 0
        
        for i in range(n):
            if (i <= right_most):
                tmp = i + A[i]
                right_most = max(tmp, right_most)
            else:
                return False

        return True