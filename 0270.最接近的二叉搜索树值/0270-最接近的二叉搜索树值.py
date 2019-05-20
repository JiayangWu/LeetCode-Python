# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        nums = inorder(root)
        res = root.val
        minum = 2 ** 32
        # print nums
        for i, x in enumerate(nums):
            distance = abs(target - x)
            print distance, minum, res
            if distance < minum:
                res = x
                minum = distance
        return res