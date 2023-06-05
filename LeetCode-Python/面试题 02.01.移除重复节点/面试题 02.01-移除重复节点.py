# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head

        # dummy = ListNode(-1)
        # prev, cur = dummy, head
        # dummy.next = cur
        # while cur:
        #     p_find_duplicate = head
        #     while p_find_duplicate:
        #         if p_find_duplicate.val == cur.val:
        #             break
        #         p_find_duplicate = p_find_duplicate.next
        #     if p_find_duplicate and p_find_duplicate!= cur:
        #         prev.next = cur.next
        #         cur = cur.next
        #     else:
        #         prev, cur = cur, cur.next
        # return head
        if not head:
            return head
        visited = {head.val}
        p = head
        while p.next:
            cur = p.next
            if cur.val not in visited:
                visited.add(cur.val)
                p = p.next
            else:
                p.next = p.next.next
        return head
        
