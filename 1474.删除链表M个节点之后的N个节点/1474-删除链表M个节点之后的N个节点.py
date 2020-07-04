# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        p = head
        tm = m - 1
        while tm and p:
            tm -= 1
            p = p.next
        if p:
            pp = p.next
            tn = n
            while tn and pp:
                tn -= 1
                pp = pp.next

            p.next = self.deleteNodes(pp, m, n)
        return head