class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = {}
        for element in A:
            if element in dic:
                dic[element] = False
            else:
                dic[element] = True
                
        for element in A:
            if dic[element]:
                return element