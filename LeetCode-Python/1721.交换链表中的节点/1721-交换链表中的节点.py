# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        l = 0
        while p:
            l += 1
            p = p.next

        reversed_k = l - k + 1

        count = 0
        p = head
        while p:
            count += 1
            if count == k:
                left_node = p
            if count == reversed_k:
                right_nnode = p 
            p = p.next

        left_node.val, right_nnode.val = right_nnode.val, left_node.val

        return head 