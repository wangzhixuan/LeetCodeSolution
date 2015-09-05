def find_position(number,lst):
    
    begin = 0
    end = len(lst)-1
    
    if lst[begin] == number:
        result = begin
    elif lst[end] == number:
        result =  end
    
    while begin < end-1:
        middle = (begin+ end)/2
        if lst[middle] == number:
            result =  middle
            break
        elif lst[middle] < number:
            begin = middle
        else:
            end = middle

    while lst[result] == lst[result+1]:
        result += 1
    
    return result    
    


class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        l = len(num) 
        if l < 2:
            return num
        
        if num[-1] > num[-2]:
            tmp = [num[-1], num[-2]]
            num[l-2:] = tmp
            return num
        
        index = l -2
        while (index>=0) and (num[index + 1] <= num[index]):
            index -= 1
        
        if index == -1:
            return num[::-1]
        else:
            tmpnumber = num[index]
            tmplst = sorted(list(num[index:]))
            index0 = find_position(tmpnumber, tmplst) + 1
            num[index] = tmplst.pop(index0 )
            num[index+1:] = tmplst
        
        return num    