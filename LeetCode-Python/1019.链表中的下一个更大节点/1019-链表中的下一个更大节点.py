# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = [] # [(2, 0)] (node.val, node.index)
        p, l = head, 0
        while p:
            l += 1
            p = p.next
        res = [0] * l

        p = head
        cur_index = 0
        while p:
            while stack and stack[-1][0] < p.val:
                last_index = stack[-1][1]
                res[last_index] = p.val
                stack.pop()
            stack.append((p.val, cur_index))
            p = p.next
            cur_index += 1
        return res