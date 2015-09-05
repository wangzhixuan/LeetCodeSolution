def output(board):        
    for i in range(9):
        outputline = ""
        for j in range(9):
            outputline += board[i][j]
            outputline += " "
            if j in (2,5):
                outputline += "| "
        print outputline
        if i in (2,5):
            print "--------------------"

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def update(row, col, element):
            print "FIND! Row:", row+1, "and Col:", col+1, "should be", element
            #print "a", row, col, element
            
            
            board[row] = board[row][:col] + element + board[row][col+1:]
            board_row[row].add(element)
            board_col[col].add(element)
            board_block[block].add(element)
            to_exclude[row][col] = set([-1])
            for row1 in range(9):
                if -1 not in to_exclude[row1][col]:
                    to_exclude[row1][col].add(element)
            for col1 in range(9):
                if -1 not in to_exclude[row][col1]:
                    to_exclude[row][col1].add(element)
            for i in range(3):
                for j in range(3):
                    row2 = row/3 * 3 + i
                    col2 = col/3 * 3+ j
                    #print row2, col2
                    if -1 not in to_exclude[row2][col2]:
                        to_exclude[row2][col2].add(element)
            output(board)
                                    
            return False
        
        
        output(board)
        
        set0 = set("123456789")
        
        # initialization
        board_row = []
        board_col = []
        board_block = []
        
        for dummy in range(9):
            board_row.append(set())
            board_col.append(set())
            board_block.append(set())


        not_valid_sudoku = "Not a Valid Sudoku!"

        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element is ".":
                    continue
                
                assert (element not in board_row[row]), not_valid_sudoku
                board_row[row].add(element)

                assert (element not in board_col[col]), not_valid_sudoku
                board_col[col].add(element)

                block = (row/3) * 3 + col/3
                assert (element not in board_block[block]), not_valid_sudoku
                board_block[block].add(element)

                
        to_exclude = {i:{j:set() for j in range(9)} for i in range(9)}
        
        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element is not ".":
                    to_exclude[row][col] = set([-1])
                else:
                    block = (row/3) * 3 + col/3
                    to_exclude[row][col] = (board_row[row].union(board_col[col])).union(board_block[block])
                    #print row,col,to_exclude[row][col]
                
      
        # solve
        finished = False
        while not finished:
            finished = True
            
            # easy check 1
            for row in range(9):
                for col in range(9):
                    if -1 in to_exclude[row][col]:
                        continue
                    block = (row/3)*3 +col/3
                    if len(to_exclude[row][col])==8:
                        # the missing element
                        for element in set0.difference(to_exclude[row][col]):
                            break
                        finished = update(row,col,element)
                        print finished
                        #print to_exclude[1][3]
                    elif len(to_exclude[row][col])>8:
                        print row, col, to_exclude[row][col]
            
            # easy check 2
            for block in range(9):
                for num in set0:
                    if num in board_block[block]:
                        continue
                    possible_position = []
                    for i in range(3):
                        row = (block/3)*3 + i
                        if num in board_row[row]:
                            continue
                        for j in range(3):
                            col = (block%3)*3 + j
                            if num in board_col[col]:
                                continue
                            elif board[row][col] is not ".":
                                continue
                            else:
                                possible_position.append((row,col))
                    if len(possible_position)==0:
                        print "ERROR! no possible position for ", num
                    elif len(possible_position) ==1:
                        (row,col) = possible_position[0]
                        finished =update(row,col,num)
                                
            # if there is any update
                if finished:
                    solved = True
                    for row in range(9):
                        for col in range(9):
                            if -1 not in to_exclude[row][col]:
                                solved = False
                                break
                            
        if solved: # actually solved
            pass
        else:
            return "not solved"
                                  
s = Solution()
s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
 # expected : ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
s.solveSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])
 # expected : ["534678923","672195348","198342567","859761423","426853791","713924856","961537284","287419635","345286179"]
