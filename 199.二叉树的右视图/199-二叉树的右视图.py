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
        last_element = None
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft() 
                last_element = cur.val 
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(last_element)

        return res