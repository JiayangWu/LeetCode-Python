# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        
        record = {0:dummy}
        pre_sum = 0
        
        while head:
            pre_sum += head.val
            if pre_sum in record:
                record[pre_sum].next = head.next
            else:
                record[pre_sum] = head
            head = head.next
        return dummy.next