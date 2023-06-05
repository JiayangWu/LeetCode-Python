# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p, l = head, 0
        while p:
            l += 1
            p = p.next
        
        stack = []
        cur = 0
        p = head
        while cur < l // 2:
            cur += 1
            stack.append(p.val)
            p = p.next

        res = 0
        while cur < l:
            cur += 1
            res = max(res, p.val + stack.pop())
            p = p.next
        return res