# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(-9999999999)
        dummy.next = head
        p = head
        while p:
            while p and p.next and p.val < p.next.val:
                p = p.next
            
            if not p.next:
                break
            cur = p.next
            tail = cur.next
            p.next = tail
            cur.next = None
            
            tmp = dummy
            while tmp and tmp.next and tmp.next.val < cur.val:
                tmp = tmp.next
                
            tmp2 = tmp.next
            tmp.next = cur
            cur.next = tmp2
            
            # self.printList(dummy.next)
            
        return dummy.next
        
    def printList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print res