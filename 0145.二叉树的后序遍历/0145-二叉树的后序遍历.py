# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # left right mid
        # mid right left [::-1]
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        return res[::-1]
            
        