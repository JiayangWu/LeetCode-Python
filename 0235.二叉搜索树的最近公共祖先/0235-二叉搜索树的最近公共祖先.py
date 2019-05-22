# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        p_path = list()
        q_path = list()
        self.findPath(root, p, p_path)
        self.findPath(root, q, q_path)
        # for node in range(len(p_path)):
        #     print p_path[node].val
        # for node in range(len(q_path)):
        #     print q_path[node].val
        l = min(len(p_path), len(q_path))
        
        for node in range(l):
            if p_path[node].val != q_path[node].val:
                break
                
        if p_path[node].val == q_path[node].val:    
            return p_path[node]
        else:
            return p_path[node - 1]
    def findPath(self, root, node, path):
        if not root:
            return None
        path.append(root)
        if root.val == node.val:
            return 
        if root.val > node.val:
            self.findPath(root.left, node, path)
        if root.val < node.val:
            self.findPath(root.right, node, path)
        
        return