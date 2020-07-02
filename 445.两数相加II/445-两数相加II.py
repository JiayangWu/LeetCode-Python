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
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        cur = ListNode(-1)
        while s1 or s2:
            value = carry
            if s1:
                value += s1.pop()
            if s2:
                value += s2.pop()

            carry = value > 9
            value %= 10
            
            cur.val = value
            pre = ListNode(-1)
            pre.next = cur
            cur = pre
            
        if carry: #处理可能的进位
            pre.val = 1
            return pre
        
        return pre.next