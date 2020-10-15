# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        values = set()

        self.result = False
        def inorderTraversal(node):
            if not node:
                return []
            if not self.result:
                if k - node.val in values:
                    self.result = True
                    return
                values.add(node.val)

                inorderTraversal(node.left)
                inorderTraversal(node.right)
        inorderTraversal(root)
        return self.result
                