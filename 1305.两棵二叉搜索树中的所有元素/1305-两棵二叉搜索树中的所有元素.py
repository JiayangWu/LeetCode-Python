# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        l1 = inorder(root1)
        l2 = inorder(root2)

        return sorted(l1 + l2)