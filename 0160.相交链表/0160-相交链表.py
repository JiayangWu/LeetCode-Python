# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        la, lb = 0, 0
        while pa:
            la += 1
            pa = pa.next
        
        while pb:
            lb += 1
            pb = pb.next
            
        if la < lb:
            la, lb, headA, headB = lb, la, headB, headA
            
        n = la - lb
        pa, pb = headA, headB
        while n:
            pa = pa.next
            n -= 1
            
        while pa:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None