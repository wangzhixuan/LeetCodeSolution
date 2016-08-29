"""
Leetcode OJ time: 45ms
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
    """
    It is easy to find out that the solution is a Fibonacci series
    So instead of iterating from i = 1 to n
    there is a O(1) solution from mathematics
    """

        alpha = math.sqrt(5)
        a0 = (5 + alpha)/10.0
        b0 = (5 - alpha)/10.0 
        
        x1 = (1 + alpha)/2.0
        x2 = (1 - alpha)/2.0
		
        # to avoid problmes caused by accuracy
		# for example int(0.999999999)  = 0
        result = int (a0 * pow(x1,n) + b0 * pow(x2,n)  + 0.1)
        
        return result