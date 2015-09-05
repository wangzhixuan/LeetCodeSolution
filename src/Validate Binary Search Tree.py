# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.my_isValidBST(root, -float("inf"), float("inf"))
    
    def my_isValidBST(self, root, lowbound, highbound):
        if root==None:
            return True
        elif root.left==None and root.right==None:
            return (root.val<highbound) and (root.val>lowbound)
        elif root.left==None:
            if root.val <= lowbound:
                return False
            else:
                return self.my_isValidBST(root.right, root.val, highbound)
        elif root.right == None:
            if root.val >= highbound:
                return False
            else:
                return self.my_isValidBST(root.left, lowbound, root.val)
        else:
            return self.my_isValidBST(root.left, lowbound, root.val) and self.my_isValidBST(root.right, root.val, highbound)
        