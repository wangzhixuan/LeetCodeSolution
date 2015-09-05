class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        dict_start2end = {}
        dict_end2start = {}
        
        def add(num):
            if num in dict_end2start:
                start = dict_end2start.pop(num)
                dict_start2end[start] += 1
                assert dict_start2end[start] == num+1
                dict_end2start[num+1] = start
            else:
                dict_start2end[num] = num+1
                dict_end2start[num+1] = num

        def merge(num):
            if num+1 in dict_start2end:
                new_end = dict_start2end.pop(num+1)
                start = dict_end2start.pop(num+1)
                dict_start2end[start] = new_end
                dict_end2start[new_end] = start
                
                
                
        for num in list(set(nums)):
            add(num)
            merge(num)
            
        max_length = 1
        for start in dict_start2end:
            max_length = max(dict_start2end[start]-start, max_length)
        
        return max_length
        
        
            