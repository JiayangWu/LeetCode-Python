# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        to_delete = set(to_delete)
        
        res = []
        
        self.roots = []
        if root.val not in to_delete:
            self.roots = [root]
        else: #如果连根节点都要删掉
            if root.left and root.left.val not in to_delete:
                self.roots += [root.left]
            if root.right and root.right.val not in to_delete:
                self.roots += [root.right]
        
        def dfs(node):
            if not node:
                return

            if node.left and node.left.val in to_delete:  #左节点要删
                dfs(node.left)
                if node.left.left: #左节点的左节点还在，不需要删
                    self.roots += [node.left.left]
                if node.left.right: #左节点的右节点还在，不需要删
                    self.roots += [node.left.right]
                
                node.left = None
                
            if node.right and node.right.val in to_delete:#右节点要删
                dfs(node.right)
                if node.right.left: #右节点的左节点还在，不需要删
                    self.roots += [node.right.left]
                if node.right.right: #右节点的右节点还在，不需要删
                    self.roots += [node.right.right]
                
                node.right = None

            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.roots
            
            