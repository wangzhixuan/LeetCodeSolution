# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if (l1 ==None) or (l2 == None):
            return None
            
        p1 = l1
        p2 = l2
        
        i=0
        
        tmpnumber1 = 0
        tmpnumber2 = 0
        
        while (p1 != None) or (p2!=None):
            number = tmpnumber2
            if (p1 != None):
                number += p1.val
                p1 = p1.next
            
            if (p2 != None):
                number += p2.val
                p2 = p2.next
            
            tmpnumber1 = number % 10
            tmpnumber2 = number / 10 
            
            tmpNode = ListNode(tmpnumber1)
            if (i==0):
                result = tmpNode
                p0 = result
            else:
                p0.next = tmpNode
                p0 = p0.next
            i += 1
        
        if (tmpnumber2==1):
            tmpNode = ListNode(1)
            p0.next = tmpNode

        return result         