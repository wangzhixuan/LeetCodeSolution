# brute force solution 
# provided by MissMary
# https://oj.leetcode.com/discuss/16619/python-runs-computer-typeerror-include-accepted-recursive


UNKNOWN = 9

class Solution:    
    def getValidNums(self, board, row, col):
        valid = [True] * 10
        for rc in range(9):
            valid[board[rc][col]] = False
            valid[board[row][rc]] = False

        ROW, COL = row/3*3, col/3*3
        for row in range(ROW, ROW + 3):
            for col in range(COL, COL + 3):
                valid[board[row][col]] = False

        return [num for num in range(9) if valid[num]]

    def solve(self, board, row, col):
        if row == 8 and col == 9:
            return True

        if col == 9:
            row, col = row + 1, 0

        if board[row][col] != UNKNOWN:
            return self.solve(board, row, col + 1)

        for trynum in self.getValidNums(board, row, col):
            board[row][col] = trynum
            if self.solve(board, row, col + 1):
                return True

        board[row][col] = UNKNOWN

        return False

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        for row in range(9):
            for col in range(9):
                board[row][col] = ord(board[row][col]) - ord('1') \
                                    if board[row][col] != '.' else UNKNOWN

        self.solve(board, 0, 0)

        for row in range(9):
            for col in range(9):
                board[row][col] = chr(board[row][col] + ord('1')) \
                                    if board[row][col] != UNKNOWN else '.'
        