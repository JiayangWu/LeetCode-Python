# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next

        count = l - k + 1
        p = head
        while 1:
            count -= 1
            if count == 0:
                break
            p = p.next

        return p