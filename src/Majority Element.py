class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dic = {}
        for element in num:
            if element in dic:
                dic[element]+=1
            else:
                dic[element] = 1
                
        for element in dic:
            if dic[element] >  (len(num) / 2):
                return element