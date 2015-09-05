"""
Non-recursive solution: Leetcode time: 208ms
"""
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        pre_count = 0
        pre_count2 = 0
        
        length = len(s)
        if length==0:
            return 0
            
            
        index =length-1
        
        while index >=0:
            if s[index] == "0":
                if index==0:
                    return 0
                elif (s[index-1] != "1") and (s[index-1]!="2"):
                    return 0
                elif index == length-1:
                    current_count = 1
                    pre_count = 1
                    index -= 2
                else:
                    current_count  = pre_count
                    pre_count = current_count
                    pre_count2 = 0
                    index -= 2
            else:
                if index == length-1:
                    current_count = 1
                elif int(s[index:index+2])>26:
                    current_count = pre_count
                elif index == length-2:    
                    current_count = pre_count +1    
                else:    
                    current_count = pre_count + pre_count2
                    
                pre_count2 = pre_count
                pre_count = current_count
                index -= 1
        
        return current_count  
        
"""
Recursive solution: Leetcode time: 320ms
"""		
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        length = len(s)
        if length == 0:
            return 0
        elif s[0] == "0":
            return 0
        elif length ==1:
            return 1
        elif length ==2:
            if (int(s)>26) and (int(s) % 10 ==0):
                return 0
            elif (int(s)>26) or (int(s) % 10 ==0):
                return 1
            else:
                return 2
        
        count = 0
        if (int(s[0:2])>26):
            return self.numDecodings(s[1:])
        elif (int(s[0:2])%10 ==0):
            return self.numDecodings(s[2:])
        elif int(s[1])>2:    
            return self.numDecodings(s[2:]) *2 
        else:
            return self.numDecodings(s[2:]) + self.numDecodings(s[1:])
        