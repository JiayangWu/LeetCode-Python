# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow, fast = head, head
        
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast:
                return True
        return False