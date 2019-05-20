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
        if  head is None or head.next is None :
            return head
        
        dummyhead = ListNode(0)
        dummyhead.next = pre = head
        cur = pre.next
        while(cur):
            # print cur.val, cur.next.val, pre.val
            pre.next = cur.next 
            cur.next = dummyhead.next
            dummyhead.next = cur
            cur = pre.next
            
        return dummyhead.next
        
        
        
        