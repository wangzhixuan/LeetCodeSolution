"""
LeetCode OJ time:   160ms
"""


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        m = len(matrix)
        if m==0:
            return 0
        n = len(matrix[0])

        # initialize matrix
        tmplist = [0]*n
        tmpmatrix = []
        for i in range(m):
            tmpmatrix.append(list(tmplist))

        # update the possibility matrix
        for row in range(m):
            previous0 = True
            for col in range(n):

                if (matrix[row][col]=="1" and previous0):
                    previous0 = False
                    start = col
                elif matrix[row][col]=="0":
                    tmpmatrix[row][col]=0
                    if (not previous0):
                        previous0 = True
                        tmpmatrix[row][start:col] = range(col-start, 0, -1)

                if col==n-1 and (not previous0) and (matrix[row][col]=="1"):
                    tmpmatrix[row][start:col+1] = range(col-start+1,0,-1)

        # calculate the maximum
        max_edge = 0
        for row in range(m-1, -1, -1):
            for col in range(n):
                if tmpmatrix[row][col]<=max_edge:
                    continue

                max_possible=tmpmatrix[row][col]
                tmprow = row
                while (row -tmprow + 1 <= max_possible):
                    if tmprow<0:
                        max_possible = row+1
                        break

                    max_possible = min(tmpmatrix[tmprow][col], max_possible)
                    if max_possible <= max_edge:
                        break
                    elif (row-tmprow+1) > max_edge:
                        max_edge = row-tmprow + 1

                    tmprow -= 1

                max_edge = max(max_possible, max_edge)

        return max_edge*max_edge
