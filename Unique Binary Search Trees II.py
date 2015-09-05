class Solution:
    """
    OJ time: 191ms
    """
    def generateTreesWithSeq(self, seq):
        if len(seq) == 0:
            return [None]
        
        result = []
        for i,element in enumerate(seq):
            lefts = self.generateTreesWithSeq(seq[:i])
            rights = self.generateTreesWithSeq(seq[i+1:])
            
            for l_tree in lefts:
                for r_tree in rights:
                    new_tree = TreeNode(element)
                    new_tree.left = l_tree
                    new_tree.right = r_tree
                    result.append(new_tree)
        return result
    
    # @return a list of tree node
    def generateTrees(self, n):
        seq = [i+1 for i in range(n)]
        
        return self.generateTreesWithSeq(seq)