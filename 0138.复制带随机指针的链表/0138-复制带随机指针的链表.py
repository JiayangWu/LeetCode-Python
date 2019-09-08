"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #133变种题， 图换成链表
        mapping = dict()
        
        p = head
        while p:
            mapping[p] = Node(p.val, None, None)
            p = p.next
            
        for key, val in mapping.items(): #key是老结点， val是新节点
            if key.next:
                val.next = mapping[key.next]
            if key.random and key.random in mapping:
                val.random = mapping[key.random]
            
        return mapping[head] if head else head
        
        