# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    """
	Solution with lower space requirement
	"""
    def pathSum(self, root, sum):
        if root is None:
            return []
            
        new_sum = sum - root.val
        if new_sum==0 and root.left==None and root.right==None:
            return [[root.val]]
        
        left_path = self.pathSum(root.left, new_sum)
        right_path = self.pathSum(root.right, new_sum)
        
        result = []
        total_path = left_path
        total_path.extend(right_path)
        
        for path in total_path:
            path.insert(0, root.val)
            result.append(path)
        
        return result
		
		
		
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def path(self,root):
        if root is None:
            return []
        left_path = self.path(root.left)
        right_path = self.path(root.right)
        total_path = left_path
        total_path.extend(right_path)
        
        if len(total_path)==0:
            return [[root.val]]
        
        result = []
        for path0 in total_path:
            path0.insert(0, root.val)
            result.append(path0)
        
        return result
            
    def pathSum(self, root, sum0):
        all_path = self.path(root)
        
        result = []
        
        for path0 in all_path:
            if sum(path0) == sum0:
                result.append(path0)
        
        return result