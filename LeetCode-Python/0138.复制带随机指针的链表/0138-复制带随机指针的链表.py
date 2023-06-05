"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head 
        
        old2new = dict()
        p = head
        while p:
            cur_node = p
            new_node = Node(cur_node.val)
            old2new[cur_node] = new_node
            p = p.next
            
        p = head
        while p:
            cur_node = p
            new_node = old2new[cur_node]
            
            if cur_node.next:
                new_node.next = old2new[cur_node.next]
            if cur_node.random:
                new_node.random = old2new[cur_node.random]
            p = p.next
        return old2new[head]