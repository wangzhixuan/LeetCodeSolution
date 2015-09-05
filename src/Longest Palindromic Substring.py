"""
There are several ways to tackle this problem.
Detailed description can be found at
http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html
http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
Here we implement the best solution discussed there, which  
has a time cost of O(N) and space cost of O(N).
"""

def pre_processing(s):
	"""
	This function add a "#" between any two letters of s
	For example: "abcd"  -> "#a#b#c#d#" 
	"""
    length = len(s)
    if length ==0:
        return "#"
    else:
        result = ""
        for i in range(length):
            result += ("#"+s[i])
        result += "#"
        
    return result        
    
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        

        str1 = pre_processing(s)    

        length1 = len(str1)

        Palindrome = [0] * length1
        right = 0
        center = 0

        max_len = 0
        max_pos = 0

        for i in range(length1):

            if i < right:
                mirror_position = center * 2 - i
                if Palindrome[mirror_position]< right - i:
                    Palindrome[i] = Palindrome[mirror_position]
                    continue
                else   :
                    start = right - i -1
            elif str1[i] == "#":
                start = 0
            else:
                start = 1
            
            length_p = start

            max_possible_length = min(i, length1 - i - 1)
            
            while (length_p < max_possible_length):
                if (str1[i + length_p + 1] != str1[i - length_p - 1]):
                    break
                length_p += 1

            Palindrome[i] = length_p
            if (length_p>max_len):
                max_len = length_p
                max_pos = (i - length_p)/2
            
            if i+length_p > right:
                right = i+length_p
                center = i

        return s[max_pos : max_pos + max_len]                  

###################
# test section
#####################
sol = Solution()
print sol.longestPalindrome("believeilab")

