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
        if not head.next:
            return []
        p = head
        if n == 1:
            while(p.next.next):
                p = p.next
            p.next = None
        else:
            fast = head
            slow = head
            for i in range(n-1):
                fast = fast.next
            print fast.val,slow.val
            while(fast.next):
                fast = fast.next
                slow = slow.next
            print fast.val,slow.val 
            slow.val = slow.next.val
            slow.next = slow.next.next
        return head