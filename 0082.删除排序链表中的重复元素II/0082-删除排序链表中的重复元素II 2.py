# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head            
        newhead = ListNode(-1)
        newhead.next = head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            p = head
            while p and p.val == head.val:
                p = p.next
            newhead.next = self.deleteDuplicates(p)
            
        return newhead.next
        
            
        