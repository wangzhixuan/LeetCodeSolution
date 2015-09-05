class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        diction = {}
        
        start = 0
        max_length = 0
        
        for index in range(len(s)):
            letter = s[index]
            
            if not diction.has_key(letter):
                diction[letter] = index
            else:
                if start <= diction[letter]:
                    length = index - start
                    start = diction[letter] + 1
                    max_length = max(max_length, length)
                
                diction[letter] = index    
        max_length = max(len(s) - start, max_length)
        
        return max_length
                