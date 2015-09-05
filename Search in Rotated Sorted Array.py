class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        length = len(A)
        
        if length<4:
            for index, element in enumerate(A):
                if element == target:
                    return index
            return -1
        
        direction = 0
        for index in range(3):
            if A[index+1]-A[index]>0:
                direction += 1
            else:
                direction -= 1
        
        target0 = target*direction

        if A[0] == target:
            return 0
        else:
            num1 = A[0]*direction
            if num1 > target0:
                wait_for_pivot = True
            else:
                wait_for_pivot = False
                

        for index, element in enumerate(A[1:]):        
            num0 = num1
            num1 = element*direction
            
            if num1==target0:
                return index+1

            # pivot point
            if num1<num0:
                wait_for_pivot = False
                if target0 > num0:
                    return -1
                elif target0 < num1:
                    return -1
                else:
                    continue
            # regular point
            elif num1 < target0:
                continue
            elif wait_for_pivot:
                continue                
            else:
                return -1
            
        return -1    
        
