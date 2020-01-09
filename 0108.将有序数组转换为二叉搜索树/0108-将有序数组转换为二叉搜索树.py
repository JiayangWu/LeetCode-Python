# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        rootIdx = len(nums)//2
        rootVal = nums[rootIdx]
        
        root = TreeNode(rootVal)
        root.left = self.sortedArrayToBST(nums[:rootIdx])
        root.right = self.sortedArrayToBST(nums[rootIdx + 1:])
        
        return root