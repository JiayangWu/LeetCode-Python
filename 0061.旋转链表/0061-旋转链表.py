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
        if k <= 0:
            return head
        l = 0
        ptr = head
        while(ptr != None):
            ptr = ptr.next
            l += 1
        # print l
        if l <= 1:
            return head
        k = k % l
        if k == 0:
            return head
        
        fast = head
        slow = head
        while(k != 0):
            fast  = fast.next
            k-= 1
        while(fast.next != None):
            fast = fast.next
            slow = slow.next
        # print fast.val, slow.val
        ptr = slow.next
        fast.next = head
        slow.next = None
        return ptr