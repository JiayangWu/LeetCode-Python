# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        slow, fast = head, head
        while k:
            k -= 1
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val