# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #层序遍历返回最后一层第一个
        from collections import deque
        if not root:
            return None
        queue = deque([root])
        while queue:
            res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res[0]
                    