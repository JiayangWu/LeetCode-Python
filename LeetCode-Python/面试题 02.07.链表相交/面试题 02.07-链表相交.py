# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        if not headA or not headB:
            return None

        la, lb = 0, 0
        while pa:
            la += 1
            pa =  pa.next
        while pb:
            lb += 1
            pb = pb.next

        if la < lb:
            headA, headB = headB, headA
            la, lb = lb, la

        diff = la - lb
        pa = headA
        while diff:
            pa = pa.next
            diff -= 1

        pb = headB
        while pa and pb and pa != pb:
            pa = pa.next
            pb = pb.next

        return pa if pa == pb else None