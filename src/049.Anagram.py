class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def groupAnagrams(self, strs):
        
        dict_of_tuples = {}
        
        for index in range(len(strs)):
            string = strs[index]
            tmplst = [0] * 26
            for letter in string:
                tmplst[ord(letter)-97]+= 1

            tmptuple = tuple(tmplst)

            if dict_of_tuples.has_key(tmptuple):
                dict_of_tuples[tmptuple].append(index)
            else:
                dict_of_tuples[tmptuple]=[index]

        result = []
        for tup in dict_of_tuples:
            group = dict_of_tuples[tup]
            group.sort(key=lambda x:strs[x])
            result.append([strs[index] for index in group])

        return result

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])