"""
Leetcode OJ time: 52ms
"""


class Solution(object):
    disappear = set([4,16,24,42,89,145,37,73])
    happy = set([1,10,100,68,86,28,82,19,91,31,13])
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n in self.happy:
            return True
        elif n in self.disappear:
            return False
        
        next_n = 0        
        while n>0:
            next_n += (n%10)**2
            n /=10
        
        return self.isHappy(next_n)