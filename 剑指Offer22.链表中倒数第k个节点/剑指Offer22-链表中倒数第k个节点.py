# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p1, p2 = head, head 
        while k:
            k -= 1
            p2 = p2.next 

        while p2:
            p1 = p1.next 
            p2 = p2.next 
        
        return p1