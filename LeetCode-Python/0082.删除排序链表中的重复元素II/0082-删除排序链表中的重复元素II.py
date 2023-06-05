# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        
        while cur:
            tail = cur.next
            if cur and tail and cur.val == tail.val:
                while cur.next and cur.val == cur.next.val:
                    tail = cur.next.next
                    cur = cur.next
                
                prev.next = tail
                cur = tail
            else:
                prev, cur = cur, tail
        
        return dummy.next