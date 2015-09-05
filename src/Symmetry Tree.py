# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.isReverse(root.left, root.right)
    
    def isReverse(self, p1, p2):
        if p1 == None:
            return (p2 == None)
        elif p2 == None:
            return False
        else:
            if p1.val == p2.val:
                return self.isReverse(p1.left, p2.right) and self.isReverse(p1.right, p2.left)
            else:
                return False