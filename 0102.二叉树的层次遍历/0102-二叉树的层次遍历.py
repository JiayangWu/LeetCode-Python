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
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            layer = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    layer.append(cur.val)
                    queue += [cur.left, cur.right]
            res.append(layer)
        return res[:-1]
                