"""
Leetcode OJ time: 53ms
"""


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        number = 5
        count = 0

        while number <= n:
            count += (n/number)
            number *= 5

        return count
