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
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        ptr = head
        while(ptr != None):
            if ptr.val != val:
                pre = pre.next
                ptr = ptr.next
            else:
                # print pre.val, ptr.val
                pre.next = ptr.next
                ptr = pre.next
        return dummy.next
        