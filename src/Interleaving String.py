"""
Recursive Solution: TLE
"""

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        
        if (len(s3)!=(len(s1)+len(s2))):
            return False
        elif len(s1)==0:
            return s2==s3
        elif len(s2)==0:
            return s1==s3
        
        if s1[0] == s2[0]:
            if s1[0] == s3[0]:
                return self.isInterleave(s1[1:],s2, s3[1:]) or self.isInterleave(s1,s2[1:],s3)
            else:
                return False
        elif s1[0] == s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif s2[0] == s3[0]:
            return self.isInterleave(s1,s2[1:],s3[1:])
        else:
            return False

"""
Dynamic Programming: Accepted with 304ms
"""

			
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        
        l2 = len(s2)
        l1 = len(s1)
        l3 = len(s3)
        
        if (l3 != l1 + l2):
            return False
        elif l1==0:
            return s2==s3
        elif l2==0:
            return s1==s3
        
        
        tmplst = []
        for index in range(l2+1):
            tmplst.append(s2[:index] == s3[:index])
        
        dp = [tmplst]        
        
        for index in range(1,l1+1):
            tmplst = list([True]*(l2+1))
            tmplst[0] = s1[:index] == s3[:index]
            dp.append(tmplst)
        
        
        for index1 in range(1,l1+1):
            for index2 in range(1,l2+1):
                index3 = index1 + index2 - 1
                dp[index1][index2] = (dp[index1-1][index2] and s1[index1-1]==s3[index3])
                dp[index1][index2] = dp[index1][index2] or (dp[index1][index2-1] and s2[index2-1] == s3[index3])
        
        return dp[l1][l2] 			