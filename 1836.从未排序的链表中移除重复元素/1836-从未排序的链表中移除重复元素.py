# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        visited = set()
        duplicates = set()
        p = head
        while p:
            if p.val not in visited:
                visited.add(p.val)
            else:
                duplicates.add(p.val)
            p = p.next

        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val in duplicates:
                prev.next = cur.next
                cur = cur.next
            else:
                prev, cur = cur, cur.next

        return dummy.next
