# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reverse = 0
        queue = [root]
        res = []
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if node:
                    layer.append(node.val)
                    next_queue += [node.left, node.right]
            queue = next_queue[:]
            if layer:
                if not reverse:
                    res.append(layer[:])
                else:
                    res.append(layer[::-1])
                reverse = 1 - reverse
        return res