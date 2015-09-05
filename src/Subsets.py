class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        
        sorted_S = sorted(S)
        
        return self.my_subsets(sorted_S)
    
    def my_subsets(self,S):
        if len(S)==0:
            return [[]]
        elif len(S) == 1:
            return [S,[]]
        
        number = S.pop()
        
        result = self.my_subsets(S)
        backup = list(result)
        
        for tmplst in backup:
            tmplst2 = list(tmplst)
            tmplst2.append(number)
            result.append(tmplst2)
            
        return result    