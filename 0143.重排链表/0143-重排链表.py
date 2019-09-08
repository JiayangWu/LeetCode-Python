# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast and fast.next:
            # print slow.val, fast.val
            slow = slow.next
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
        
        # print slow.val, fast.val
        
        tail = slow.next
        slow.next = None
        first = head
        last = self.reverseList(tail)
        
        while last:
            tmp = first.next
            first.next = last
            tmp2 = last.next
            last.next = tmp
            first = first.next.next
            
            last = tmp2
        return head
        
        
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p