# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Definition for a binary tree node.

        if not root:
            return []
        node = [root]
        node_val = list(list())
        self.generate(node, node_val)
        return node_val[::-1]
    
    def generate(self, node, node_val):
        new_node = []
        new_node_val = []
        for node in node:
            if node.left:
                new_node.append(node.left)
            if node.right:
                new_node.append(node.right)
            new_node_val.append(node.val)
        node_val.append(new_node_val)
        if len(new_node) == 0:
            return
        self.generate(new_node, node_val)
        
        
        
        
    