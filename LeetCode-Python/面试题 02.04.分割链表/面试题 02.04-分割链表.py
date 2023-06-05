# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1, dummy2 = ListNode(-1), ListNode(-2)

        smaller, larger = dummy1, dummy2
        p = head
        while p:
            if p.val < x:
                smaller.next = ListNode(p.val)
                smaller = smaller.next
            else:
                larger.next = ListNode(p.val)
                larger = larger.next

            p = p.next
        
        smaller.next = dummy2.next
        return dummy1.next