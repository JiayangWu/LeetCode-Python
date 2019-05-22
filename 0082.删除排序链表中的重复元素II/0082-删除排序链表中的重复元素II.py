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
        new_head = ListNode(1)
        new_head.next = head
        pre = new_head
        cur = head
        while cur:
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next;
            if cur == pre.next:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
                
        return new_head.next