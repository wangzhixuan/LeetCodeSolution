class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        
        m = len(matrix)
        if m ==0:
            return 0
        n = len(matrix[0])
        if n ==0:
            return 0
        
        height_pos = []
        height = []
        for col in range(n):
            height.append(0)
        
        max_area = 0
        
        for row in range(m):
            height_pos = []
            for col in range(n):
                pre_position = col
                if matrix[row][col] == "0":
                    height[col] = 0
                else:
                    height[col] += 1
                    
                while len(height_pos)>0 and (height[col] < height_pos[-1][0]):
                    h = height_pos[-1]
                    area = h[0] * (col -h[1])
                    pre_position = h[1]
                    max_area = max(max_area, area)
                    height_pos.pop()
                if len(height_pos)==0 or (height[col] > height_pos[-1][0]):
                    height_pos.append((height[col], pre_position))
            
            for h in height_pos:
                area = h[0] * (n - h[1])
                max_area = max(area, max_area)        
        
        return max_area            

            
                    
                    
                        
                        
                
            
        
            