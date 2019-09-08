# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(1)
        dummy.next = head

        first = head
        second = head.next
        
        tail = second.next
        first.next = self.swapPairs(tail)
        second.next = first
        dummy.next = second
        
        return dummy.next