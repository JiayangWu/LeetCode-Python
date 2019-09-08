# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import *
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next
            
        dummy = ListNode(1)
        p = dummy
        while pq:
            val, idx = heappop(pq)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heappush(pq, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next
            