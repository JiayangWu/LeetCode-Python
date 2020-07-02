# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = list()
        while queue:
            nextqueue = list()
            layer = list()
            for node in queue:
                if node.left:
                    nextqueue.append(node.left)
                if node.right:
                    nextqueue.append(node.right)
                layer.append(node.val)
                
            queue = nextqueue[:]
            res.append(layer)
        return res
        