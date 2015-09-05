
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i = 0
        while (i < (len(A))):
            if A[i] == elem:
                A.pop(i)
            else:
                i += 1    
        return len(A)        