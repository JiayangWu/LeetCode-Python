# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1 
        list1 = []
        list2 = []
        while p:
            list1.append(p.val)
            p = p.next 
        p = l2
        while p:
            list2.append(p.val)
            p = p.next 

        l3 = sorted(list1 + list2)

        dummy = ListNode(-1)
        p = dummy 
        for num in l3:
            p.next = ListNode(num)
            p = p.next
        
        return dummy.next