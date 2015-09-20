"""
Leetcode OJ time: 56ms
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root==None:
            return []
        
        
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        
        if len(left)>len(right):
            longer = left
            shorter = right
            left_is_longer = True
        else:
            longer = right
            shorter = left
            left_is_longer = False
        
        for j, fromshorter in enumerate(shorter):
            if left_is_longer:
                longer[j].extend(fromshorter)
            else:
                longer[j][0:0] = fromshorter
        longer.insert(0,[root.val])
        return longer
