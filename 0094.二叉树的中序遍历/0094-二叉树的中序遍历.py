# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        cur = root
        res = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left 
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right 
        return res

