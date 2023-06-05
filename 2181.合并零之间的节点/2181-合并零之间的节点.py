# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p_new = dummy

        p = head
        cur_sum = 0
        while p:
            if p.val == 0:
                if cur_sum:
                    node = ListNode(cur_sum)
                    p_new.next = node
                    p_new = p_new.next
                cur_sum = 0
            else:
                cur_sum += p.val
            p = p.next

        return dummy.next