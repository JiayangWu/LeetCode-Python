# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        has_loop = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                has_loop = True
                break    
        if not has_loop:
            return None
        
        fast = head
        while 1:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
