# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        l = []
        while p:
            l.append(p.val)
            p = p.next
        if len(l) <= 1:
            return head
        k = k % len(l)
        if not k:
            return head
        
        l = l[-k:] + l[:-k]
        print l
        newhead = ListNode(-1)
        p = newhead
        for item in l:
            p.next = ListNode(item)
            p = p.next
        return newhead.next