class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive1(self, A):
        """
        My O(n) time and O(n) space solution
        Well, the requirement is O(1) space

        OJ time: 216ms
        
        """

        if len(A) ==0:
            return 1
        
        set0 = set()
        
        for num in A:
            if num <=0:
                continue
            elif num not in set0:
                set0.add(num)
        
        num = 1
        while True:
            if num not in set0:
                return num
            else:
                num += 1


    def firstMissingPositive2(self, A):
        """
        Solution by ChuntaoLi
        https://oj.leetcode.com/discuss/19011/python-solution-with-bit-manipulation


        OJ time: 95ms

        Explanation:
        the ith digit of num denotes whether i exists in list A,

        a pass through A registers all the elements
        at corresponding postions in num,

        and the while loop checks from the least significant digit of num
        and returns once a 0 digit is found.



        
        """
        num = 0
        for i in A:
            if i > 0:
                num = num | (1 << i)
        x = 1
        while True:
            if (1 << x) & num == 0:
                return x
            x += 1

    
    def firstMissingPositive3(self, A):
        """
        Solution by yuyibestman
        https://oj.leetcode.com/discuss/8763/share-my-o-n-time-o-1-space-solution


        The basic idea is for any k positive numbers (duplicates allowed),
        the first missing positive number must be within [1,k+1].
        The reason is like you put k balls into k+1 bins,
        there must be a bin empty, the empty bin can be viewed as
        the missing number.

        OJ time: 77ms
        """

    
        def swap(i,j):
            if i==j:
                return
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        
        if len(A)==0:
            return 1
        
        # partition the list so that the positive are in the front
        totalp = 0
        for i,num in enumerate(A):
            if num >0:
                swap(totalp, i)
                totalp+=1
        
        # so A[:totalp+1] are all positive numbers
        A.insert(totalp, A[0])


        # the missing number must exist within [1, totalp+1]
        # so mark the (i-1)th place negative if i is in the list
        for num in A[:totalp]:
            if abs(num) <= totalp+1:
                if A[num-1]>0:# unnecessary IF there is no duplicates
                    A[num-1]*=-1
        
        # the first positive position in the list
        # is the first missing positive number
        for i in range(0,totalp+1):
            if A[i]>=0:
                return i+1
        
        return 1


