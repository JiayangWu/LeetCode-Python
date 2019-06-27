# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1, l2 = head, self.reverseList(slow.next)
        slow.next = None
        # self.printList(l1)
        # self.printList(l2)
        while l1 and l2:
            cur = l2
            l2 = l2.next

            cur.next = l1.next
            l1.next = cur
            l1 = l1.next.next

        return head
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    
    def printList(self, head):
        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next
        print l