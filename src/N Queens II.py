class Solution:
    """
    My solution
    OJ time: 240ms
    """
    def dfs(self,row,n):
        if row == n:
            self.result+=1
            return
        for j in range(n):
            if j in self.used_col:
                continue
            diff = j-row
            if diff in self.used_diag1:
                continue
            sumup = j+row
            if sumup in self.used_diag2:
                continue
            
            self.used_col.append(j)
            self.used_diag1.append(diff)
            self.used_diag2.append(sumup)
            
            self.dfs(row+1, n)
            
            self.used_col.pop()
            self.used_diag1.pop()
            self.used_diag2.pop()
            
        
    # @return a list of lists of string
    def totalNQueens(self, n):
        self.result = 0
        self.used_col = []
        self.used_diag1 = []
        self.used_diag2 = []
        self.dfs(0,n)
        return self.result   
        
class Solution:
    """
    Online solution by us917
    https://oj.leetcode.com/discuss/3959/i-think-its-very-difficult-for-python-to-get-accepted
    OJ time: 152ms
    """
    ans, limit = 0, 0
    # @return an integer
    def totalNQueens(self, n):
        self.ans = 0
        self.limit = (1<<n) - 1
        self.dfs(0, 0, 0)
        return self.ans

    def dfs(self, h, r, l):
        if h == self.limit:
            self.ans += 1
            return
        pos = self.limit & (~(h|r|l))
        while pos:
            p = pos & (-pos)    #return most right bit 1
            pos -= p
     