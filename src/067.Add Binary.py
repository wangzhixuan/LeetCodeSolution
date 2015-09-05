class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        
        if len(a)>len(b):
            s1 = b
            s2 = a
            l1 = len(b)
            l2 = len(a)
        else:
            s1 = a
            s2 = b
            l1 = len(a)
            l2 = len(b)
            
        
        result = ""
        index = 1
        number = 0
        while index <= l1:
            number /= 2
            n1 = int(s1[-index])
            n2 = int(s2[-index])
            
            number += (n1 + n2)
            result = str(number % 2) + result
            index += 1
        
        while index <= l2:
            number /= 2
            n2 = int(s2[-index])
            number += n2
            result = str(number %2) + result
            index += 1
        
        if number >1:
            result = "1" + result
        
        return result    
            
        