class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = set()
        
        dic0 = {}
        
        for num in candidates:
            if num >=target:
                continue
            elif target-num in dic0: #if it is a solution
                for comb in dic0[target-num]:
                    tmplst = list(comb)
                    tmplst.append(num)
                    tmplst.sort()
                    tmplst = tuple(tmplst)
                    if tmplst not in result:
                        result.add(tmplst)
            
            dic1 = dict(dic0)
            for temp_sum in dic1:
                new_sum = temp_sum + num
                if new_sum > target:
                    continue
                new_comb = list(dic0[temp_sum])
                new_comb.append(num)
                new_comb.sort()
                new_comb = tuple(new_comb)
                if new_sum in dic1:
                    dic0[new_sum].add(new_comb)
                else:
                    dic0[new_sum] = set([new_comb])
            
            new_sum = num
            new_comb = (num,)
            if new_sum in dic0:
                dic0[new_sum].add(new_comb)
            else:
                dic0[new_sum] = set([new_comb])

        return result
        
        
class Solution:
    """
    by ChunTaoLiu at
    https://oj.leetcode.com/discuss/17932/dp-solution-in-python
    Leetcode OJ time: 68ms
    """
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])