# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)

        smaller_list = dummy1
        larger_list = dummy2
        p = head
        while p:
            if p.val < x:
                new_node = ListNode(p.val)
                smaller_list.next = new_node
                smaller_list = smaller_list.next
            else:
                new_node = ListNode(p.val)
                larger_list.next = new_node
                larger_list = larger_list.next
            p = p.next
        
        smaller_list.next = dummy2.next
        return dummy1.next
