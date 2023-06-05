# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        
        p = head
        pre = None
        while p:
            if p.val in visited:
                pre.next = p.next
                p = p.next
            else:
                visited.add(p.val)
                pre = p
                p = p.next
        return head
                