def median(lst):
    """
    return the median of a sorted list "lst", as a float
    """
    
    length = len(lst)
    if (length == 0):
        return None
    elif (length % 2 == 1):
        return float(lst[length/2])
    else:
        return (lst[length/2] + lst[length/2 - 1])/2.0

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        """
        Given two sorted list A and B
        return the median of combined list (A+B), as a float
        """

############################################################
#       Trivial solution with O(N log(N)) time cost
#       LeetCode timer: 640ms 
############################################################
#        tmp  = A + B
#        tmp.sort()
#        
#        totallength = len(tmp)
#        halfindex = totallength / 2 
#        
#        if totallength == 1:
#            return float(tmp[0])
#        elif totallength % 2 == 0 :
#            return (tmp[halfindex] + tmp[halfindex - 1 ])/2.0
#        else:
#            return float(tmp[halfindex])
##############################################################

        if len(A)>len(B):
            lst1 = B
            lst2 = A
        else:
            lst1 = A
            lst2 = B
        
        # so that m <= n
        m = len(lst1)
        n = len(lst2)
        
        return  self.find_median2(lst1, lst2, m,n)
    
    def find_median2(self, lst1, lst2, m,n):
        """
        Given two sorted list lst1 and lst2
        return the median of combined list (lst1+lst2), as a float
        m = len(lst1)
        n = len(lst2)
        it is garuanteed that m <= n
        """
        if (m == 0):
            return median(lst2)
        elif (m <= 3):
            next_lst1 = lst1
            if (n <=  m+3):
                next_lst2 = lst2
            else:
                # cut off (n-m)/2 -1 numbers from both end of lst2
                # which does not affect the median at all
                next_lst2 = lst2[(n-m)/2 -1: 1- (n-m)/2]
            
            tmplst = next_lst1 + next_lst2
            tmplst.sort()
            
            return median(tmplst)
        else:
            mid1 = median(lst1)
            mid2 = median(lst2)

            cutoff = m/2 
            if ((m+n)%2 == 0) and (m % 2 == 0):
            # for example
            # lst2 = [1,    ,6]
            # lst1 = [  3,4]
            # here m = 2 and and cutoff = 1                
            # the median = (3+4)/2
            # but if cutoff = 1 then either 3 or 4 will be cut
                cutoff -= 1
            # The main effect of this line is that
            # sometimes m can only be reduced to 3
            # Because 3/1 -1 = 0. So no further cutoff will happen
            # which is the reason I added the section (m<=3) above                
            
            if (mid1 == mid2):
                return mid1
            elif (mid1 > mid2):
                next_lst1 = lst1[0: -cutoff]
                next_lst2 = lst2[cutoff:]
            else:
                next_lst1 = lst1[cutoff  :]
                next_lst2 = lst2[0: -cutoff]
                
            next_m = m - cutoff
            next_n = n - cutoff
        
        return self.find_median2(next_lst1, next_lst2, next_m, next_n)

############################################################
#   Self test section, which is not needed on leetcode
############################################################
# sol = Solution()   
# list1 = [1,2,3,5,7]
# list2 = [2,3,4]
# print sol.findMedianSortedArrays( list1, list2)
#############################################################
