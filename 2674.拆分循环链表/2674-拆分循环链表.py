# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        
        l, p = 0, head
        last = None
        flag = False
        while not flag or p != head:
            flag = True
            l += 1
            if p.next == head:
                last = p
            p = p.next
        # print(l, last)
        mid = math.ceil(l / 2)

        cnt, p = 1, head
        while cnt < mid:
            p = p.next
            cnt += 1

        next_head = p.next
        p.next = head 
        last.next = next_head
        return [head, next_head]
