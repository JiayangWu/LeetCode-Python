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
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur: 
            tmp = cur.next #保存尾部
            cur.next = pre #逆转局部
            pre = cur #pre后移
            cur = tmp #cur后移
        return pre

        