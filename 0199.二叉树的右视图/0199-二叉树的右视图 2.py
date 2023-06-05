# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque 
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            tmp = None
            for _ in range(len(queue)):
                cur = queue.popleft() 
                if cur:
                    tmp = cur.val 
                    queue += [cur.left, cur.right] 
            if tmp:
                res.append(tmp)
        return res
