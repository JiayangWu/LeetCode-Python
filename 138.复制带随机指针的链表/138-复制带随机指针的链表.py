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
        cur = head
        mapping = dict()
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
            
        for cur, copy in mapping.items():
            if cur.next:
                copy.next = mapping[cur.next]
            if cur.random:
                copy.random = mapping[cur.random]
        return mapping[head] if head else head