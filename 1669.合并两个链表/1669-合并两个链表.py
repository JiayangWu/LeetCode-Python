# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = list1
        prev, cur = dummy, list1
        left, right = None, None
        count = 0
        while cur:
            if count == a:
               left = prev

            if count == b:
                right = cur.next
            
            count += 1
            prev, cur = cur, cur.next

        left.next = list2
        p = list2
        while p and p.next:
            p = p.next
        p.next = right
        return dummy.next