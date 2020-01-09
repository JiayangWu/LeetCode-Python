# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt = 0
        cur, stack = root, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cnt += 1
                cur = stack.pop()
                if cnt == k:
                    return cur.val
                cur = cur.right