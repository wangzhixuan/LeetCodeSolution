# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        """
		O(N) time cost, O(N) space cost
		"""
        if head==None:
            return None
        
        index = head
        
        stack = []
        while index.next is not None:
            stack.append(index)
            index= index.next
            
        stack.append(index) 
        
        L1 = head
        n = len(stack)
        count = 0    
        while count < (n-1)/2:
            L2 = stack.pop()
            L2.next = L1.next
            L1.next = L2
            L1 = L2.next
            count += 1
        
        L2 = stack.pop()
        
        #assert((L1.next == L2) or (L1== L2))
        
        L2.next = None
        
        
        
        
        return head