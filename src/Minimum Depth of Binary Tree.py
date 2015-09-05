# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        self.mindepth = float("inf")
        return self.my_minDepth(root, 0)
        
    def my_minDepth(self, root, count):
        
        if count > self.mindepth:
            return self.mindepth + 1
        elif root == None:
            self.mindepth = count
            return count
        elif root.left == None and root.right == None:
            self.mindepth = count + 1
            return count + 1
        elif root.left == None:
            return self.my_minDepth(root.right, count + 1)
        elif root.right == None:
            return self.my_minDepth(root.left, count + 1)
        else:
            return min(self.my_minDepth(root.left, count + 1), self.my_minDepth(root.right, count + 1))
        
        
        