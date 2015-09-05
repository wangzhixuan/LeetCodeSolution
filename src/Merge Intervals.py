# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        
        index = 0
        while index<len(sorted_intervals)-1:
            current = sorted_intervals[index]
            next = sorted_intervals[index+1]
            
            if next.start > current.end:
                index += 1
            else:
                current.end = max(next.end, current.end)
                sorted_intervals.pop(index+1)
        
        return sorted_intervals        
            
            
        