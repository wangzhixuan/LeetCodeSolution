class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        
        result = self.my_convert(s,nRows)
        one_string = ""
        for string in result:
            one_string += string
                
        return one_string        
            
       
    def my_convert(self, s, nRows):    
        block = nRows * 2 - 2
        result = [""]* nRows
        
        l = len(s)

        end_in_one_block = (l <= block)
        
        for i in range(nRows):
            if (not end_in_one_block) or (l > i):
                result[i] += s[i]
            if (i > 0) and (i < nRows -1):
                if (not end_in_one_block) or (l > block - i):
                    result[i] += s[block - i]
        
        if (not end_in_one_block):
            appending = self.my_convert(s[block:], nRows)
            for i in range(nRows):
                result[i] += appending[i]
        
        return result       
            