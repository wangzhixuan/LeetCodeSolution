# leetcode OJ time: 282ms

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            new_nums = nums[:i] + nums[i+1:]
            candidates = self.twoSum(new_nums, -num)
            candidates = map(lambda x:self.append(x, num), candidates)
            candidates = set(map(tuple, map(self.sort, candidates)))
            result |= candidates
        
        return map(list, list(result))
    
    def append(self, l, num):
        l.append(num)
        return l
    
    def sort(self, l):
        l.sort()
        return l
            
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]        
        """
        result = []
        tmp_set = set()
        for i, num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                if num*2 == target:
                    result.append([num, num])
                continue
            if target - num in tmp_set:
                result.append([num, target-num])
            tmp_set.add(num) 
            
        return result
