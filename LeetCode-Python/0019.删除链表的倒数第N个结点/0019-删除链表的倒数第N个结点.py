# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next

        count = l - n + 1

        dummy = ListNode(-1)
        dummy.next = head
        cur = -1
        p = dummy
        while p:
            cur += 1
            if cur == count - 1:
                node_to_be_deleted = p.next
                p.next = node_to_be_deleted.next
                break
            p = p.next
        
        return dummy.next