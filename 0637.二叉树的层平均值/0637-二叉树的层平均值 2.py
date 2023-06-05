# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque 
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            layer = []
            for _ in range(len(queue)):
                cur = queue.popleft() 
                if cur:
                    layer.append(cur.val)
                    queue += [cur.left, cur.right] 
            if layer:
                res.append(sum(layer) * 1.0 / len(layer))
        return res
