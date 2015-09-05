class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
            
        pre2 = nums[0]
        pre1 = max(nums[0], nums[1])
        ContainLast =  (nums[1]>nums[0])
        
        current_max = 0
        for i in range(2,len(nums)):
            if not ContainLast:
                current_max = pre1 + nums[i]
                ContainLast = True
            else:
                if pre1>(pre2+nums[i]):
                    current_max = pre1
                    ContainLast = False
                else:
                    current_max = pre2+nums[i]
                    ContainLast = True
            pre2 = pre1
            pre1 = current_max
                    
        return current_max