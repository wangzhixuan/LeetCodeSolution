class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        
        if m <= 2 or n <= 2:
            return board
        
        circles = set()
        sur_cir = set()
        
        this_block = set()
        
        direction = ((1,0), (-1,0), (0,1), (0,-1))
        
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'X' or (row,col) in circles:
                    continue
                
                if row in [0, m -1] or col in [0, n-1]:
                    circles.add((row,col))
                
                this_block = set([(row,col)])
                thislevel = set()
                nextlevel = set([(row,col)])
                
                surrounded = True
                while (len(nextlevel) != 0):
                    thislevel = nextlevel
                    nextlevel = set()
                    
                    for point in thislevel:
                        if point[0] in [0, m-1] or point[1] in [0, n-1]:
                            surrounded = False
                        
                        for index in range(4):
                            new_row = min(m-1, max(0, point[0] + direction[index][0]))
                            new_col = min(n-1, max(0, point[1] + direction[index][1]))
                            
                            if board[new_row][new_col] == "O" and ( not (new_row, new_col) in circles):
                                circles.add((new_row, new_col))
                                nextlevel.add((new_row, new_col))
                        
                    this_block.update(nextlevel)
                
                if surrounded:
                    sur_cir.update(this_block)
        
        for point in sur_cir:
            board[point[0]][point[1]] = "X"
        
        return board   