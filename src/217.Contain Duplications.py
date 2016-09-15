"""
LeetCode OJ time: 45ms
"""


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num]=1
        return False
