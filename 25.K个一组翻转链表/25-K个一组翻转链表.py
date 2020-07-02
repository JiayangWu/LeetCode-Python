# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        cnt = 0
        p = head
        while p:
            cnt += 1
            if cnt == k:
                break
            p = p.next
            
        if cnt < k:
            return head
        
        tail = p.next
        p.next = None
        
        tmp = self.reverseKGroup(tail, k)
        newhead = self.reverseLL(head)
        head.next = tmp
        
        return newhead
        
        
        
    def reverseLL(self, head):
        if not head or not head.next:
            return head
        p = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return p