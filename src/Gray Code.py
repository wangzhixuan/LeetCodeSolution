class Solution:
    """
    OJ time: 208ms
    """
    def dfs(self, code, n):
        base = 1
        number = 0
        for i in range(n-1, -1, -1):
             number += code[i]*base
             base *= 2
        
        # add the number into the sequence if it is valid
        if number in self.set0:
            return False
        else:
            self.set0.add(number)
            self.sequence.append(number)
        
        if len(self.sequence)==self.total:
            return True
        
        for i in range(n-1, -1, -1): # "for i in range(n):" should also work
            code[i] = 1- code[i]
            if self.dfs(code, n):
                return True
            code[i] = 1- code[i]
        
        # if the code run through here, then there is no solution with this sequence
        self.set0.discard(number)
        self.sequence.pop()
        return False
        
    
    # @return a list of integers
    def grayCode(self, n):
        self.set0 = set()
        self.sequence = []
        self.total = 2**n
        
        code = [0 for i in range(n)]
        if self.dfs(code, n):
            return self.sequence