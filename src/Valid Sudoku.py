class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):

        board_col = []
        board_block = []
        
        for dummy in range(9):
            board_col.append(set())
            board_block.append(set())
        
        set0 = set("123456789")
        
        for row in range(9):
            #if set(board[row]).difference(set0) is not set("."):
            #    return False
            board_row = set()
            for col in range(9):
                element = board[row][col]
                
                if element is ".": # can be anything
                    continue
                elif element not in set0:  
                    return False
                
                if element in board_row:
                    return False
                else:
                    board_row.add(element)
                
                if element in board_col[col]:
                    return False
                else:
                    board_col[col].add(element)
                
                block = int(row/3) * 3 + col/3
                if element in board_block[block]:
                    return False
                else:
                    board_block[block].add(element)
        
        #for i in range(9):
        #    if (board_col[i].difference(set0) is not set()) or (board_block[i].difference(set0) is not set()):
        #        return False
                
        return True