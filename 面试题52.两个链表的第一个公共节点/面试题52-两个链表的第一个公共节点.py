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
        la, lb = 0, 0
        
        p = headA
        while p:
            la += 1
            p = p.next
            
        p = headB
        while p:
            lb += 1
            p = p.next 
            
        if la < lb:
            headA, headB = headB, headA
            la, lb = lb, la
            
        cnt = la - lb
        p = headA
        while cnt:
            cnt -= 1
            p = p.next 
            
            
        while p != headB:
            p = p.next 
            headB = headB.next 
        return p