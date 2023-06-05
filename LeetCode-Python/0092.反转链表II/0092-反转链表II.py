# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-501)
        dummy.next = head
        p = dummy.next
        before_left = None
        tail = None
        prev, cur, count = dummy, p, 0
        left_node, right_node = None, None
        while prev and cur:
            count += 1
            if count == left:
                before_left = prev
                left_node = cur
            if count == right:
                tail = cur.next
                right_node = cur
                right_node.next = None
                break
            prev = cur
            cur = cur.next

        self.reverse(left_node)
        before_left.next = right_node
        left_node.next = tail
        return dummy.next
        
    def reverse(self, node):
        if not node or not node.next:
            return node
        
        tmp = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return tmp