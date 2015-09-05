class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        
        if start == end:
            return 0
        
        dict.add(end)
        totalcount = len(dict)
        lengthcount = 2
        
        thisLevel = set([start])
        nextLevel = set()
        dist = set()
        
        char = [chr(c+97) for c in range(26)]
        
        while True:
            for word in thisLevel:
                for index in range(len(word)):
                    for letter in char:
                        new_word = word[:index] + letter + word[index+1:]
                        if new_word == end:
                            return lengthcount
                        elif new_word in dict:
                            nextLevel.add(new_word)
                            dict.remove(new_word)
                            totalcount -= 1
                            if totalcount==0: 
                                return 0
            if len(nextLevel) == 0:    
                return 0
            
            thisLevel = nextLevel
            lengthcount += 1
            nextLevel = set()