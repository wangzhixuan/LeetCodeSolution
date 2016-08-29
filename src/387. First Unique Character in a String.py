"""
LeetCod OJ time: 228ms
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        result = -1
        for i,c in enumerate(s):
            if counts[c]==1:
                result = i
                break
            
        return result
