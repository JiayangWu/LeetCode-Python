# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # if len(nums) == 1:
        #     return TreeNode(nums[0])

        index = len(nums) // 2
        root = TreeNode(nums[index], self.sortedArrayToBST(nums[:index]), self.sortedArrayToBST(nums[index + 1:]))
        return root