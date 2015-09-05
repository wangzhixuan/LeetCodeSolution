class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        
        ls = len(s)
        lp = len(p)
        result = True

        if (lp == 0):
            return (ls ==0)
        
        index_p = 0
        
        if ls == 0:
            # the case of lp == 0 already excluded
            # "" can match expressions like "a*b*c*.*"
            if (lp) % 2 == 1 :
                return False
            else:
                while index_p < lp :
                    if p[index_p + 1] == '*':
                        index_p += 2
                        continue
                    else:
                        return False
                return True                    

        else:
            if p[0] == '.':
                if lp > 1 and p[1] == '*':
                    # ".*" matches any expression 
                    if lp == 2:
                        return True
                    else:
                        # search for the next meaningful character
                        # basically ".*a*b*" is the same as ".*"
                        # ".*..a*" matches any expression with length longer than 2
                        index_p = 0
                        index_s = 0
                        while index_p < lp:
                            if (index_p + 1 < lp) and p[index_p +1 ] == '*':
                                index_p += 2
                            elif (p[index_p] == "."):
                                index_p += 1
                                index_s += 1
                                if (index_s >= ls):
                                    return False
                            else:
                                break
                        
                        if index_p == lp:
                            # if no-meaningful character until end, then return true
                            return True
                        
                        index_s = 0
                        while index_s < ls:
                            # there can be multiple ways to compare ".*c" with "abcbc"
                            # the first match compares "c" with "cbc", which returns False
                            # the second match compares "c" with "c", which returns True
                            if s[index_s] == p[index_p]:
                                if self.isMatch(s[index_s:], p[index_p:]):
                                    return True
                            index_s += 1
                            
                        # seems redundant here
                        # should always return False
                        # the cases when self.isMatch("", p[index_p:])==True
                        # is already included in (if index_p == lp) condition above
                        ########################################
                        # return self.isMatch("", p[index_p:])
                        ##########################################
                        return False
                else:
                    # if starting with "." but not ".*"
                    # compare the next one
                    return self.isMatch(s[1:],p[1:])
            elif lp == 1:
                # p has only one letter which is not "."
                if ls == 1:
                    return (s[0] == p[0])
                else:
                    return False
            elif p[1] != '*':
                # p should have at least two letters here.
                # If it does not starts with "x*", simple case
                if s[0] == p[0]:
                    return self.isMatch(s[1:],p[1:])
                else:
                    return False
            else:
                # If it does start with "x*"
                if ((lp > 3) and (p[3] == '*') and (p[2]==p[0])) or (s[0] != p[0]):
                # First condition ((lp > 3) and (p[3] == '*') and (p[2]==p[0]))
                # check redundant expression in p, because "a*a*" == "a*"
                # Second condition (s[0] != p[0])
                # represents the simple case: compare "b" with "a*b"
                    return self.isMatch(s, p[2:])
                else:
                # consider the case "aaa" compares with "a*c*a", or "a*."    
                    return self.isMatch(s, p[2:]) or self.isMatch(s[1:],p)    
                    
                    
                

        
        
sol = Solution()
print sol.isMatch("","a*")
