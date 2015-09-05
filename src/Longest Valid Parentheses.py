class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        totallength = len(s)
        
        if totallength <2:
            return 0
        
        start = {}
        length = 0
        max_val = 0
        min_val = 0
        value = 0
        
        for index in range(totallength):
            if len(start)==0 and s[index] == ")":
                continue
            elif s[index] == "(":
                if not start.has_key(value):
                    start[value] = index
                value += 1
            elif s[index] == ")":
                if start.has_key(value):
                    del start[value]
                value -= 1
                if start.has_key(value):
                    length = max(length,index - start[value] + 1)
                    
                
            else:
                return 
            
        return length    