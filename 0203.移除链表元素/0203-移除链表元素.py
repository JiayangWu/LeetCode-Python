# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, cur = dummy, head
        while cur:
            if cur.val == val: #ÐèÒª±»É¾³ý
                pre.next = cur.next
                cur.next = None
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next