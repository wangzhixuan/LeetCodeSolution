class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        newhead = head
        tmpNode = head
        
        if head == None:
            return head
        elif head.next == None:
            return head
        elif k ==0:
            return head
        
        
        count = 1
        while (tmpNode.next != None):
            count+=1
            tmpNode = tmpNode.next
        
        index0 = count - (k)%count 
        
        if index0==count:
            return head
        
        tmpNode = head
        index = 0
        while (tmpNode.next !=None):
            if (index<index0-1):
                index+=1
                tmpNode = tmpNode.next
            elif (index==index0-1):
                newhead = tmpNode.next
                tmpNode.next = None
                tmpNode = newhead
                index+=1
            else:
                tmpNode = tmpNode.next
            
        
        tmpNode.next = head

            
        return newhead