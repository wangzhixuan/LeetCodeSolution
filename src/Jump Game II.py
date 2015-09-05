class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        
        n = len(A)
        if n <2 :
            return 0
        
        nstep = 0
        limit = [0]
        
        for i in range(n):
            if i > limit[-1]:
                # unreachable
                return -1
            
            if i > limit[nstep]:
                nstep += 1
            
            right = i + A[i]
            if nstep == len(limit) - 1:
                test_limit = limit[-1]
            else:
                test_limit = limit[nstep + 1]
                
            if right>test_limit:
                if right >= n - 1:
                    return nstep +1
                elif nstep == len(limit)-1:
                    limit.append(right)
                else:
                    for k in range(nstep+1, len(limit)):
                        limit[k] = right