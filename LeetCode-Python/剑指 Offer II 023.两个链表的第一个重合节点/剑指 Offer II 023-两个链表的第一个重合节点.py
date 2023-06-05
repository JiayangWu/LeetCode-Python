# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        la, lb = 0, 0
        p = headA
        while p:
            la += 1
            p = p.next
        
        p = headB
        while p:
            lb += 1
            p = p.next

        if la > lb:
            headA, headB = headB, headA
            la, lb = lb, la

        diff = lb - la
        pa, pb = headA, headB
        while diff:
            pb = pb.next
            diff -= 1

        while pa and pb:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next

        return None
