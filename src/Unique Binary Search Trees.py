class Solution:
    # @return an integer
    def numTrees(self, n):
        seq = [1,1,2]
        if n <= 2:
            return seq[n]
        
        level = 3
        while level < n+1:
            count = 0
            for i in range(0, level):
                count += seq[i] * seq[level-i-1]
            
            seq.append(count)
            level += 1
        
        return seq[-1]