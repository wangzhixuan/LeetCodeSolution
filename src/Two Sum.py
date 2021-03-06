class Solution():
    def twoSum(self, num, target):
        """
        A better solution
        """
        d = {}
        for i,number in enumerate(num):
            if d.has_key(number):
                return (d[number]+1, i+1)
            else:
                d[target - number] = i
        
        # no such combination if the codes comes to this line
        return None


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n = len(num)

        if (n==2):
            return [0,1]

        # at least 2 intervals
        # sqrt(n) is the optimized number of intervals if all input are positive
        num_interval = max(int(math.floor(math.sqrt(n))),2)

        l_of_lists = []
        l_of_indices = []
        
        interval = target / num_interval
        
        if (interval ==0):
            if (target >0):
                interval = 1
                num_interval = target

        for i in range(num_interval+2):
            l_of_lists.append([])
            l_of_indices.append([])

        
        
        threshold = [0]*(num_interval+1)
        threshold[num_interval ]= target - 1
        for i in range(1,num_interval/2 + 1):
            threshold[i] = interval * i
            threshold[-i-1] = target - threshold[i] - 1
        
        if (target % 2 == 0):
            if (num_interval % 2 == 0) or (target == 0):
                if target/2 in num:
                    index1 = num.index(target/2)
                    tmplist = list(num)
                    tmplist.remove(target/2)
                    if target/2 in tmplist:
                        index2 = tmplist.index(target/2)
                        if (index2>= index1):
                            index2 += 1
                            return [index1+1, index2+1]  
                        else:
                            return [index2+1, index1+1]

        for i in range(n):
            number = num[i]
            if (number<= threshold[0]):
                index = 0
            elif (number > threshold[num_interval]):
                index = num_interval + 1
            else:
                testindex = number/ interval
                index = max(min(testindex,num_interval),1)
                
                while (number <= threshold[index-1]) or (number > threshold[index]):
                    if (number <= threshold[index-1]):
                        index -= 1
                    else:
                        index += 1
            l_of_lists[index].append(number)        
            l_of_indices[index].append(i)
        
        for l_index in range(num_interval/2 + 2):
            l1 = len(l_of_lists[l_index])
            l2 = len(l_of_lists[num_interval + 1 - l_index])

            if (l1 * l2 ==0):
                continue
            
            for i1 in range(l1):
                for i2 in range(l2):
                    item1 = l_of_lists[l_index][i1]
                    item2 = l_of_lists[num_interval + 1 - l_index][i2]
                    if (item1 + item2 == target):
                        index10 = l_of_indices[l_index][i1]+1
                        index20 = l_of_indices[num_interval+1-l_index][i2] + 1
                        index1 = min(index10, index20)
                        index2 = max(index10, index20)
                        return [index1, index2]
        
