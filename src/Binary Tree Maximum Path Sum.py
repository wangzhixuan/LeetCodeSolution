# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum0(self, root):
        if root is None:
            return [0,-float("inf")]
        
        [linkl, suml] = self.maxPathSum0(root.left)
        [linkr, sumr] = self.maxPathSum0(root.right)

        link = max(linkl, linkr, 0) + root.val
        summ = max(linkl + linkr + root.val, suml, sumr, link)
        
        return [link, summ]
            
        
    
    def maxPathSum(self, root):
        result = self.maxPathSum0(root)
        return result[1]
        