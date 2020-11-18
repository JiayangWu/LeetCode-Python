# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getLinkedListLength(l):
            length = 0
            while l:
                l = l.next
                length += 1
            return length

        def printLL(node):
            l = []
            while node:
                l.append(node.val)
                node = node.next
            print(l)

        def reverseLL(node):
            if not node or not node.next:
                return node
            p = reverseLL(node.next)
            node.next.next = node
            node.next = None
            return p

        length1 = getLinkedListLength(l1)
        length2 = getLinkedListLength(l2)

        if length1 < length2:
            l1, l2 = l2, l1
            length1, length2 = length2, length1

        dummy = ListNode(-1)
        p = dummy

        n = length1 - length2
        while n:
            p.next = ListNode(l1.val)
            l1 = l1.next
            p = p.next
            n -= 1

        while l2:
            p.next = ListNode(l1.val + l2.val)
            p = p.next
            l1 = l1.next
            l2 = l2.next


        dummy.next = reverseLL(dummy.next)

        p = dummy.next
        carry = 0
        pre = dummy
        while p:
            p.val += carry
            if p.val > 9:
                p.val -= 10
                carry = 1
            else:
                carry = 0
            p = p.next
            pre = pre.next

        if carry:
            pre.next = ListNode(1)
        
        return reverseLL(dummy.next)
