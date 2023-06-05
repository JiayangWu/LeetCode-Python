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
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head
        pre = head
        while fast and fast.next:        
            pre = slow
            slow = slow.next
            fast = fast.next.next
            # print slow.val, fast.val, pre.val
        pre.next = None
        part1 = head
        part2 = slow.next
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(part1)
        root.right = self.sortedListToBST(part2)
        return root
        