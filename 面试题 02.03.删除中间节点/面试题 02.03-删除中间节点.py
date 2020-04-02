# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        while p and p.next:
            p.val = p.next.val
            if not p.next.next:
                p.next = None
            p = p.next
            