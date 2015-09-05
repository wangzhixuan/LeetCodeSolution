class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = {}
        for element in A:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1
                
        for element in A:
            if dic[element] is not 3:
                return element        