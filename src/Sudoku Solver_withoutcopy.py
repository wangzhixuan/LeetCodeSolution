def deepcopy(ob):
    if isinstance(ob, list):
        rt = []
        for item in ob:
            rt.append(deepcopy(item))
    elif isinstance(ob, dict):
        rt = {}
        for item in ob:
            rt[item] = deepcopy(ob[item])
    elif isinstance(ob, set):
        rt = set()
        for item in ob:
            rt.add(deepcopy(item))
    elif isinstance(ob, str):
        rt = ""
        for item in ob:
            rt += item
    else: # single element
        rt = ob
    return rt


class Sudoku:
    def __init__(self, board=None):
        
        self.set0 = set("123456789")  
        self.board = board
        self.board_row = []
        self.board_col = []
        self.board_block = []

        if board == None:
            return
        assert len(board)==9
        assert len(board[0])==9

        
        for dummy in range(9):
            self.board_row.append(set())
            self.board_col.append(set())
            self.board_block.append(set())

        not_valid_message = "Not a Valid Sudoku!"
        
        for row in range(9):
            for col in range(9):
                element = self.board[row][col]
                if element is ".":
                    continue
                
                assert (element not in self.board_row[row]), not_valid_message
                self.board_row[row].add(element)
                assert (element not in self.board_col[col]), not_valid_message
                self.board_col[col].add(element)
                block = (row/3) * 3 + col/3
                assert (element not in self.board_block[block]), not_valid_message
                self.board_block[block].add(element)
        
        self.to_exclude = {i:{j:set() for j in range(9)} for i in range(9)}
        for i in range(9):
            self.to_exclude[i] = {}
            for j in range(9):
                self.to_exclude[i][j] = set()
              
        
        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element is not ".":
                    self.to_exclude[row][col] = set([-1])
                else:
                    block = (row/3) * 3 + col/3
                    self.to_exclude[row][col] = (self.board_row[row].union(self.board_col[col])).union(self.board_block[block])
                    #print row,col,to_exclude[row][col]
        
    def clone(self):
        newobject = Sudoku()
        newobject.board = deepcopy(self.board)
        newobject.board_row = deepcopy(self.board_row)
        newobject.board_col = deepcopy(self.board_col)
        newobject.board_block = deepcopy(self.board_block)
        newobject.to_exclude = deepcopy(self.to_exclude)
        return newobject

    def copy(self, other):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    self.update(row, col, other.board[row][col])
        
        
    def __str__(self):
        output = " \n"
        for i in range(9):
            outputline = ""
            for j in range(9):
                outputline += self.board[i][j]
                outputline += " "
                if j in (2,5):
                    outputline += "| "
            outputline += " \n"
            if i in (2,5):
                outputline += "-------------------- \n"
            output += outputline
        return output

    def update(self, row, col, element, output=True):
        print "FIND! Row:", row+1, "and Col:", col+1, "should be", element

        self.board[row] = self.board[row][:col] + element + self.board[row][col+1:]
        self.board_row[row].add(element)
        self.board_col[col].add(element)
        block = (row/3)*3 +col/3
        self.board_block[block].add(element)
        self.to_exclude[row][col] = set([-1])
        for row1 in range(9):
            if -1 not in self.to_exclude[row1][col]:
                self.to_exclude[row1][col].add(element)
        for col1 in range(9):
            if -1 not in self.to_exclude[row][col1]:
                self.to_exclude[row][col1].add(element)
        for i in range(3):
            for j in range(3):
                row2 = row/3 * 3 + i
                col2 = col/3 * 3 + j
                #print row2, col2
                if -1 not in self.to_exclude[row2][col2]:
                    self.to_exclude[row2][col2].add(element)
        if output:
            print self
                                
        return False


    def solved(self):
        
        for i in range(9):
            if not (self.board_row[i] == self.set0):
                return False
        return True

    def showanswer(self):
        print " ~~~~ Final Solution ~~~~ "
        print self
        print self.board[0][0], self.board[0][1], self.board[0][2]
                                        
    def solve(self):
        finished = False
        while not finished:
            finished = True

            #easy check 1
            for row in range(9):
                for col in range(9):
                    if -1 in self.to_exclude[row][col]:
                        continue
                    if len(self.to_exclude[row][col])>=9:#,
                        print "Nothing is allowed in Row: "+str(row)+" and Col: "+str(col)
                        return False
                    elif len(self.to_exclude[row][col])==8:
                        finished = False
                        # the missing element
                        for element in self.set0.difference(self.to_exclude[row][col]):
                            break
                        finished = self.update(row,col,element)

            # easy check 2
            for block in range(9):
                for num in self.set0:
                    if num in self.board_block[block]:
                        continue
                    possible_position = []
                    for i in range(3):
                        row = (block/3)*3 + i
                        if num in self.board_row[row]:
                            continue
                        for j in range(3):
                            col = (block%3)*3 + j
                            if num in self.board_col[col]:
                                continue
                            elif self.board[row][col] is not ".":
                                continue
                            else:
                                possible_position.append((row,col))
                    if len(possible_position) ==0:
                        print "ERROR! No possible position for "+ num + " in block: "+str(block+1)
                        return False
                    if len(possible_position) ==1:
                        (row,col) = possible_position[0]
                        finished =self.update(row,col,num)

        
            if finished:
                if self.solved():
                    self.showanswer()
                    return True
                else: # easy checks cannot advance any more
                    print "Not solved. Now try brute force!"
                    
                    for row in range(9):
                        for col in range(9):
                            if self.board[row][col] == ".":
                                options = self.set0.difference(self.to_exclude[row][col])
                                for element in options:
                                    print " ##################################### "
                                    print " ## Try ", element, " in row: ", row+1, " and col: ", col+1
                                    new_sudoku = self.clone()
                                    new_sudoku.update(row, col, element)
                                    if new_sudoku.solve():
                                        self.copy(new_sudoku)
                                        self.showanswer()
                                        return True
                                    else:
                                        print new_sudoku
                                        
                    print " ######################################"
                    return False

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        
              
        # initialization
        sudoku = Sudoku(board)
        
        # solve
        sudoku.solve()

        print sudoku                          
s = Solution()
#test = Sudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
#print test
s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
 # expected : ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
s.solveSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])
 # expected : ["534678923","672195348","198342567","859761423","426853791","713924856","961537284","287419635","345286179"]
