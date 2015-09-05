class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        
        n = len(height)
        if n==0:
            return 0
        
        height_position = []
        max_area = 0
        
        for i in range(n):
            pre_position = i
            while len(height_position)>0 and (height[i] < height_position[-1][0]):
                h = height_position[-1]
                area = h[0] * (i-h[1])
                pre_position = h[1]
                max_area = max(area, max_area)
                height_position.pop()
            if len(height_position)==0 or (height[i] > height_position[-1][0]):
                height_position.append((height[i],pre_position))

            
        for h in height_position:
            area = h[0] * (i - h[1] + 1)
            max_area = max(area, max_area)

        
        return max_area 
            
                