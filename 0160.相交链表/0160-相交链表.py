# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = 0
        lb = 0
        pa = headA
        pb = headB
        while(pa!= None):
            la += 1
            pa = pa.next
        while(pb!= None):
            lb += 1
            pb = pb.next
        
        # print la,lb
        pb = headB
        pa = headA
        if lb > la:
            k = lb-la 
            while(k > 0):
                k -= 1
                pb = pb.next
        else:
            k = la - lb
            while(k > 0):
                k -= 1
                pa = pa.next
        # print pb.val
        # print pa.val
        
        while(pb != None):
            # print pa.val, pb.val
            if pb == pa:
                return pa
            else:
                pa = pa.next
                pb = pb.next
            
        return None