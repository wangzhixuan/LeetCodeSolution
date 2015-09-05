# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        p = self
        out = "{"
        while p.next is not None:
            out+= (str(p.val) + ", ")
            p = p.next
        if p is not None:
            out += str(p.val)
        out += "}"
        return out

def list_of_nodes(lst):
    head = ListNode(lst[0])
    p = head
    index = 1
    while index < len(lst):
        p.next = ListNode(lst[index])
        p = p.next
        index += 1
    return head
        
        
        
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None:
            return head
        
        stack = []
        p = head
        newhead = None
        
        while (p is not None):
            stack.append(p)
            temp_p = p.next
            #print p.val, len(stack)
            if len(stack) == k:
                while len(stack)>0:
                    #print stack
                    if newhead == None:
                        newhead = stack.pop()
                        index = newhead
                    else:
                        index.next = stack.pop()
                        index = index.next
                index.next = None
                #print newhead
            if temp_p is None:
                break
            else:
                p = temp_p
        
        while len(stack)>0:
            if newhead == None:
                newhead = stack.pop(0)
                index = newhead
            else:
                index.next = stack.pop(0)
                index = index.next
                
        return newhead
    
s = Solution()
a = list_of_nodes([1,2,3])
print s.reverseKGroup(a,2)
