# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

        
def find_position(intervals,newInterval):
    """
    Insert newInterval into intervals (a list of intervals sorted according to their start times)
    If there are multiple interval with the same start time with newInterval,
    return the first such position
    """
    
    begin = 0
    end = len(intervals)-1
    
    if intervals[begin].start >= newInterval.start:
        return 0
    elif intervals[end].start <= newInterval.start:
        return end + 1
    
    while begin < end-1:
        middle = (begin+ end)/2
        if intervals[middle].start == newInterval.start:
            return middle
        elif intervals[middle].start < newInterval.start:
            begin = middle
        else:
            end = middle
        
        if intervals[begin].start == intervals[end].start:
            break
    
    index = end
    while index>0 and intervals[index].start == intervals[index-1].start:
        index -= 1
    
    return index
    

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
            
        position = find_position(intervals, newInterval)
        
        intervals.insert(position, newInterval)
        
        index = max(position-1,  0)
        
        for dummy in range(2):
            interval = intervals[index]
            index += 1
        
            while (index < len(intervals)) and (interval.end >= intervals[index].start):
                interval.end = max(interval.end, intervals[index].end)
                intervals.pop(index)
            
        return intervals

        
        
        