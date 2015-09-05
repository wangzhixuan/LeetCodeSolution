class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s) ==0:
            return 0
        
        hit_space = False


        for j in range(len(s)):
            if s[-j-1] != " ":
                break
        
        if s[-j-1] ==" ":
            return 0

        for i in range(j, len(s)):

            if s[-i - 1]==" ":
                hit_space = True
                break
        
        if hit_space:
            return i - j
        else:
            return len(s) - j