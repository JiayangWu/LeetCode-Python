# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        p = newhead
        while(l1 and l2):
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        
        if l1:
            p.next = l1
        else:
            p.next = l2
        return newhead.next
            
            