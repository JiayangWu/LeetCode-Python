# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        if not root:
            return 0
        queue = deque([root])
        while queue:
            res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
        return sum(res)