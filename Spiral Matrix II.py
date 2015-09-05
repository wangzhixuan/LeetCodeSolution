def tuple_add(tuple1, tuple2):
    n = len(tuple1)
    return [tuple1[i] + tuple2[i] for i in range(n)]    

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        tmpindex = (0,0)
        
        direction = ((0,1),(1,0),(0,-1),(-1,0))
        
        tmplst = [0] * n
        result = []
        for dummy_index in range(n):
            result.append(list(tmplst))
        
        direction_index = 0
        for i in range(1, n ** 2+1):
            result[tmpindex[0]][tmpindex[1]] = i
            if (i == n**2):
                break
            while (True) : 
                new_index = tuple_add(tmpindex, direction[direction_index])
                if not (new_index[0] in range(n)):
                    direction_index = (direction_index + 1) % 4
                elif not (new_index[1] in range(n)):
                    direction_index = (direction_index + 1) % 4
                elif result[new_index[0]][new_index[1]] != 0:
                    direction_index = (direction_index + 1) % 4
                else:
                    break
                    
            tmpindex = tuple(new_index)    
                    
        return result

sol = Solution()
print     sol.generateMatrix(2)
