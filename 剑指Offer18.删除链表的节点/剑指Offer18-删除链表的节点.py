# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head 

        p = dummy
        while p:
            if p.next and p.next.val == val:
                p.next = p.next.next 
                break 
            p = p.next 
        return dummy.next