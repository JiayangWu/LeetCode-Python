# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        stack = [] # [node]
        nodes_to_be_deleted = set()
        p = head
        while p:
            while stack and stack[-1].val < p.val:
                nodes_to_be_deleted.add(stack[-1])
                stack.pop()
            stack.append(p)
            p = p.next

        p = dummy
        while p.next:
            if p.next in nodes_to_be_deleted:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next

