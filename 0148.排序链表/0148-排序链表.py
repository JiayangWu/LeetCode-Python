# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #1. 一分为二
        #2. 各自排序
        #3. 合二为一
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            
        first = head
        second = pre.next
        pre.next = None
        # print first.val, second.val
        sortedfirst = self.sortList(first)
        sortedsecond = self.sortList(second)
        
        return self.merge(sortedfirst, sortedsecond)
        
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            tmp = ListNode(l1.val)
            tmp.next = self.merge(l1.next, l2)
        else:
            tmp = ListNode(l2.val)
            tmp.next = self.merge(l1, l2.next)
            
        return tmp