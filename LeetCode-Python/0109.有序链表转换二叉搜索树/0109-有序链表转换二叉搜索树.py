# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        p = head
        array = []
        while p:
            array.append(p.val)
            p = p.next

        return self.sortedArrayToBST(array)


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        index = len(nums) // 2
        root = TreeNode(nums[index], self.sortedArrayToBST(nums[:index]), self.sortedArrayToBST(nums[index + 1:]))
        return root