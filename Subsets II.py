class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        
        sorted_S = sorted(S)
        
        tupleresult = self.my_subsets(sorted_S)
        
        result = [[]]
        for tup in tupleresult:
            tmplst = list(tup)
            result.append(tmplst)
        
        return result    
        
    
    def my_subsets(self,S):
        if len(S)==0:
            return set([])
        elif len(S) == 1:
            return set([tuple(S)])
        
        number = S.pop()
        
        result = self.my_subsets(S)
        
        backup = list(result)
        backup.append([])
        
        for tmplst in backup:
            tmplst2 = list(tmplst)
            tmplst2.append(number)
            tmptuple = tuple(tmplst2)
            if not tmptuple in result:
                result.add(tmptuple)
                
        return result    