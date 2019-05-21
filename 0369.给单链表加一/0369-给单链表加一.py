# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp
    
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode 
        """
        head = self.reverseList(head)
        tmp = head
        head.val += 1
        while(head.val > 9):
            head.val -= 10
            if head.next:
                head.next.val += 1
                head = head.next
            else:
                head.next = ListNode(1)
                break
        return self.reverseList(tmp)