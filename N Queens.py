class Solution:
    """
    Solution by  wang.yelei  
    https://oj.leetcode.com/discuss/3861/solved-with-backtracing
    OJ time: 540ms
    """
    def dfs(self,ret,pos,row,n):
        if row == n:
            ret.append([''.join('Q' if pos[i] == j else '.'for j in range(n)) for i in range(n)])
            return
        for j in range(n):
            if j not in pos \
                and all(map(lambda r: pos[r] != j - (row - r), range(row))) \
                and all(map(lambda r: pos[r] != j + (row - r), range(row))):  
                    pos.append(j)
                    self.dfs(ret,pos,row+1,n)
                    pos.pop()

    # @return a list of lists of string
    def solveNQueens(self, n):
        ret=[]
        self.dfs(ret,[],0,n)
        return ret
        

class Solution:
    """
    Solution by   us917 
    https://oj.leetcode.com/discuss/3861/solved-with-backtracing
    OJ time: 224ms
    """

    """
    Explanation:
         backtrace program using bit-wise operation to speed up calculation.
         'limit' is all '1's.
         'h'  is the bits all the queens vertically projected on a row. If h==limit, then it's done, answer++.
         'r'   is the bits all the queens anti-diagonally projected on a row.
         'l'   is the bits all the queens diagonally projected on a row.
         h|r|l  is all the occupied bits. Then pos = limit & (~(h|r|l)) is all the free positions.
         p = pos & (-pos)  gives the right most '1'. pos -= p means we will place a queen on this bit 
                                     represented by p.
         'h+p'  means one more queue vertically projected on next row.
         '(r+p)<<1'  means one more queue anti-diagonally projected on next row. Because we are
                           moving to next row and the projection is skew from right to left, we have to 
                           shift left one position after moved to next row.
         '(l+p)>>1'  means one more queue diagonally projected on next row. Because we are 
                          moving to next row and the projection is skew from left to right, we have to 
                          shift right one position after moved to next row.
    """
    
    
    board, ans, limit = None, None, 0
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.ans = []
        self.limit = (1<<n) - 1
        self.dfs(0, 0, 0, 0)
        return self.ans

    def dfs(self, h, r, l, row):
        if h == self.limit:
            A = []
            for line in self.board:
                A.append(''.join(line))
            self.ans.append(A)
            return
        pos = self.limit & (~(h|r|l))
        index = -1
        while pos:
            p = pos & (-pos)    #return most right bit 1
            pos -= p
            for i in range(index+1, 32):
                if p == 1<<i:
                    index = i
                    break
            self.board[row][index] = 'Q'
            self.dfs(h+p, (r+p)<<1, (l+p)>>1, row+1)   #no shift needed for h, left shift for anti diagonal
            self.board[row][index] = '.'      


 class Solution:
    """
    My solution
    OJ time: 284ms
    """
 
    def dfs(self,row,n):
        if row == n:
            self.result.append([''.join('Q' if self.used_col[i] == j else '.'for j in range(n)) for i in range(n)])
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
    def solveNQueens(self, n):
        self.result = []
        self.used_col = []
        self.used_diag1 = []
        self.used_diag2 = []
        self.dfs(0,n)
        return self.result            


# Original bit operation solution 
# found on https://oj.leetcode.com/discuss/743/whats-your-solution
class Solution {
    public:
        /* backtrace program using bit-wise operation to speed up calculation.
         * 'limit' is all '1's.
         * 'h'  is the bits all the queens vertically projected on a row. If h==limit, then it's done, answer++.
         * 'r'   is the bits all the queens anti-diagonally projected on a row.
         * 'l'   is the bits all the queens diagonally projected on a row.
         * h|r|l  is all the occupied bits. Then pos = limit & (~(h|r|l)) is all the free positions.
         * p = pos & (-pos)  gives the right most '1'. pos -= p means we will place a queen on this bit 
         *                             represented by p.
         * 'h+p'  means one more queue vertically projected on next row.
         * '(r+p)<<1'  means one more queue anti-diagonally projected on next row. Because we are
         *                   moving to next row and the projection is skew from right to left, we have to 
         *                   shift left one position after moved to next row.
         * '(l+p)>>1'  means one more queue diagonally projected on next row. Because we are 
         *                  moving to next row and the projection is skew from left to right, we have to 
         *                  shift right one position after moved to next row.
         */
        int totalNQueens(int n) {
            ans = 0;
            limit = (1<<n) - 1;
            dfs(0, 0, 0);
            return ans;
        }
        void dfs(int h, int r, int l) {
            if (h == limit) {
                ans++;
                return;
            }
            int pos = limit & (~(h|r|l));
            while (pos) {
                int p = pos & (-pos);
                pos -= p;
                dfs(h+p, (r+p)<<1, (l+p)>>1);
            }
        }
        int ans, limit;
};
        