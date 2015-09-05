class Solution:
    # @return a boolean
    def isValid(self, s):
        
        dic0 = {"(":")", "{":"}", "[":"]"}
        
        stack = []
        
        for index in range(len(s)):
            if dic0.has_key(s[index]):
                stack.append(dic0[s[index]])
            elif len(stack) == 0:
                return False
            elif s[index] == stack[-1]:
                stack.pop()
            else:
                return False
        
        
        return (len(stack)==0)