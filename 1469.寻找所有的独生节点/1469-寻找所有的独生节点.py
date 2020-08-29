# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def dfs(node, siblings_cnt):
            if not node:
                return

            if siblings_cnt == 1:
                self.res.append(node.val)

            siblings_cnt = 0
            if node.left:
                siblings_cnt += 1
            if node.right:
                siblings_cnt += 1
            dfs(node.left, siblings_cnt)
            dfs(node.right, siblings_cnt)

        dfs(root, 0)
        return self.res