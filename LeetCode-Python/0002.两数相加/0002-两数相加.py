# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1

        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(-1)
        p = dummy
        while l1 and l2:
            s = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            if s > 9:
                s -= 10
                carry =  1
            else:
                carry = 0

            p.next = ListNode(s)
            p = p.next
        
        while l1:
            s = l1.val + carry
            if s > 9:
                s -= 10
                carry =  1
            else:
                carry = 0
            l1 = l1.next
            p.next = ListNode(s)
            p = p.next

        while l2:
            s = l2.val + carry
            if s > 9:
                s -= 10
                carry =  1
            else:
                carry = 0
            l2 = l2.next
            p.next = ListNode(s)
            p = p.next
        
        if carry:
            p.next = ListNode(1)
        return dummy.next