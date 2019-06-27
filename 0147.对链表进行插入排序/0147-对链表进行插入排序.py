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
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = head #pre始终指着排序好链表的最后一个节点
        cur = head.next #cur始终指着未排序链表的第一个节点
        while cur:
            tail = cur.next
            pre.next = tail  #把cur这个节点拿出来
            
            p = dummy
            while p.next and p.next.val < cur.val: #找到插入的位置
                p = p.next
                
            cur.next = p.next #把cur插入到p和p.next之间
            p.next = cur
            cur = tail
            
            if p == pre:#如果刚插入到了已排序链表的末尾
                pre = pre.next #那么就更新pre
        return dummy.next