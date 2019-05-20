# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head
        l = list()
        while(head):
            l.append(head.val)
            head = head.next
        
        def sortedArrayToBST(nums):
            if not nums:
                return None

            def dfs(start, end):
                if end < start:
                    return 

                mid = (end + start) // 2
                root = TreeNode(nums[mid])

                root.left = dfs(start, mid - 1)
                root.right = dfs(mid + 1, end)

                return root

            return dfs(0, len(nums) - 1)
        
        return sortedArrayToBST(l)
            
        
        