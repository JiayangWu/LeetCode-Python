# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        queue = deque([root])
        
        layer = 1
        res = 1
        max_values = 0
        while queue:
            values = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    values += node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if values > max_values:
                max_values = values
                res = layer
            layer += 1
        return res
                    