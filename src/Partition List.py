# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        
        if head==None:
            return head
        
        # starting point:
        if head.val < x:
            start = head
            left_end = start
            right_start = None
            right_end = None
        else :
            right_start = head
            right_end = right_start
            while (right_end.next != None):
                if right_end.next.val < x:
                    start = right_end.next
                    left_end = start
                    break
                else:
                    right_end = right_end.next
            # in case all values are greater or equal to x
            if right_end.next == None:
                return head
        
        # continue on the left_end:
        while (left_end.next != None):
            if left_end.next.val < x:
                left_end = left_end.next
            else:
                if (right_start == None):
                    right_start = left_end.next
                    right_end = right_start
                else:    
                    right_end.next = left_end.next
                    right_end = right_end.next
                left_end.next = left_end.next.next
        
        
        left_end.next = right_start
        if right_start != None:
            right_end.next = None
        
        return start
        