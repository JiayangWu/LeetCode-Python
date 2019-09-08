# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                
            if slow == fast:
                break
        if slow != fast:
            return None
        
        fast = head
        while slow:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
            