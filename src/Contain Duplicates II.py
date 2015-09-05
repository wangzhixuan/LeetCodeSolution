class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i-dic[num] <= k:
                return True
            else:
                dic[num] = i
        return False