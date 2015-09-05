# leetcode run time: 168 ms

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        lists = [[[]]]
        
        for largest_number in range(1, n+1):
            
            max_index = min(largest_number, k)
            min_index = max(0, largest_number - n + k -1)
            for index_k in range(max_index, min_index, -1):
                if (index_k < largest_number):
                    for tmplist in lists[index_k - 1]:
                        tmplist2 = list(tmplist)
                        tmplist2.append(largest_number)
                        lists[index_k].append(tmplist2)
                else:
                    lists.append([range(1,largest_number+1)])
                    
        return lists[-1]