# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        slow, fast = p, p
        while(n):
            n -= 1
            fast = fast.next
        if fast is None:
            return p.next    
        while(fast and fast.next):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return p
        
        