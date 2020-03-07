"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mapping = {} # key is the old node, val is the new node

        p = head 
        while p:
            mapping[p] = Node(p.val)
            p = p.next 

        p = head 
        while p:
            if p.next:
                mapping[p].next = mapping[p.next]
            if p.random:
                mapping[p].random = mapping[p.random]
            p = p.next

        return mapping[head] if head else head