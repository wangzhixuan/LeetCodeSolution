class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        if numRows == 0:
            return result
        
        tmplst = [1]
        result.append([1])
        
        for i in range(1, numRows):
            for index in range(i, 0, -1):
                if index == i :
                    tmplst.append(1)
                else:
                    tmplst[index] += tmplst[index-1] 
            
            result.append(list(tmplst))
        
        return result        
